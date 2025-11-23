import json
import os

import chainlit as cl
from chainlit.input_widget import TextInput
from openai import OpenAI

# --- Constants and Configuration ---
PROFILES_DIR = "user_profiles"
os.makedirs(PROFILES_DIR, exist_ok=True)

# --- Tool Definitions ---


def read_user_profile(user_id: str) -> dict:
    """
    Reads the user's profile from a dedicated JSON file.

    Args:
        user_id (str): The unique identifier of the user.

    Returns:
        dict: The user's profile data.
    """
    profile_path = os.path.join(PROFILES_DIR, f"{user_id}.json")

    try:
        with open(profile_path, "r") as f:
            profile_data = json.load(f)
            if not profile_data:
                return {
                    "message": "Your profile is currently empty. You can add to it by telling me things to remember."
                }
            return profile_data
    except FileNotFoundError:
        return {
            "message": "You don't have a profile yet. You can create one by telling me something to remember."
        }
    except json.JSONDecodeError:
        return {"error": "Failed to read your profile. It might be corrupted."}


def update_user_profile(user_id: str, key: str, value: str):
    """
    Updates or adds a key-value pair to the user's profile.

    Args:
        user_id (str): The unique identifier of the user.
        key (str): The profile attribute to update (e.g., "name", "preference").
        value (str): The value to set for the attribute.
    """
    profile_path = os.path.join(PROFILES_DIR, f"{user_id}.json")
    profile_data = {}

    # Read existing data if the file exists and is not empty
    if os.path.exists(profile_path):
        try:
            with open(profile_path, "r") as f:
                content = f.read()
                if content:
                    profile_data = json.loads(content)
        except json.JSONDecodeError:
            return {
                "error": "Could not update profile because the existing file is corrupted."
            }

    # Update data and write back to the file
    profile_data[key] = value
    try:
        with open(profile_path, "w") as f:
            json.dump(profile_data, f, indent=4)
        return {"message": f"Successfully updated your profile: {key} is now {value}."}
    except Exception as e:
        return {"error": f"Failed to write to your profile file: {e}"}


# --- Main Chat Logic ---


@cl.on_chat_start
async def on_chat_start():
    """
    Initializes the chatbot session, setting up the Gemini agent.
    """
    # Configure the Gemini model through the OpenAI SDK compatibility layer
    client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    # System prompt to define the agent's behavior
    system_prompt = (
        "You are a personal assistant. "
        "You have access to tools to read and update a user's profile. "
        "When a user asks you to remember something, use the update_user_profile tool. "
        "When they ask what you know about them, use the read_user_profile tool. "
        "Be friendly and helpful."
    )

    cl.user_session.set("client", client)
    cl.user_session.set("system_prompt", system_prompt)

    # Store tools in the user session
    cl.user_session.set("tools", [
        cl.Tool(
            name="read_user_profile",
            description="Reads the user's profile from a dedicated JSON file.",
            parameters=[
                {
                    "name": "user_id",
                    "type": "string",
                    "description": "The unique identifier of the user.",
                }
            ],
            func=read_user_profile,
        ),
        cl.Tool(
            name="update_user_profile",
            description="Updates or adds a key-value pair to the user's profile.",
            parameters=[
                {
                    "name": "user_id",
                    "type": "string",
                    "description": "The unique identifier of the user.",
                },
                {
                    "name": "key",
                    "type": "string",
                    "description": "The profile attribute to update (e.g., 'name', 'preference').",
                },
                {
                    "name": "value",
                    "type": "string",
                    "description": "The value to set for the attribute.",
                },
            ],
            func=update_user_profile,
        ),
    ])

    # Greet the user
    await cl.Message(
        content="Hello! I'm your personal assistant. I can remember things for you. What's on your mind?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """
    Handles incoming user messages, interacts with the agent, and sends back responses.
    """
    client = cl.user_session.get("client")
    system_prompt = cl.user_session.get("system_prompt")
    tools = cl.user_session.get("tools")

    # Create OpenAI tool definitions from the cl.Tool objects
    openai_tools = []
    for tool in tools:
        openai_tools.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": {
                    "type": "object",
                    "properties": {param["name"]: {"type": param["type"], "description": param["description"]} for param in tool.parameters},
                    "required": [param["name"] for param in tool.parameters if param.get("required", True)], # Assuming all parameters are required by default if not specified
                },
            },
        })

    # Add the user's message to the conversation history
    history = cl.user_session.get(
        "history", [{"role": "system", "content": system_prompt}]
    )
    history.append({"role": "user", "content": message.content})

    # Create the message for the API call
    msg = cl.Message(content="")
    await msg.send()

    # --- Agent Interaction Loop ---
    while True:
        response = client.chat.completions.create(
            model="gemini-1.5-flash-latest",
            messages=history,
            tools=openai_tools,
            tool_choice="auto",
        )

        response_message = response.choices[0].message

        # Check for tool calls
        if response_message.tool_calls:
            tool_call = response_message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            # Find and execute the corresponding tool
            tool_found = False
            for tool in tools:
                if tool.name == tool_name:
                    tool_found = True
                    # Get user_id from session and add it to tool_args
                    if "user_id" not in tool_args:
                        tool_args["user_id"] = cl.user_session.get("id")

                    with cl.Step(type="tool", name=tool_name, args=tool_args) as step:
                        step.input = tool_args
                        tool_output = await cl.make_async(tool.func)(**tool_args)
                        step.output = tool_output

                        # Append tool output to history for context
                        history.append(
                            {
                                "role": "assistant",
                                "content": "",
                                "tool_calls": response_message.tool_calls,
                            }
                        )
                        history.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "name": tool_name,
                                "content": json.dumps(tool_output),
                            }
                        )
                    break
            if not tool_found:
                await cl.Message(content=f"Error: Tool '{tool_name}' not found.").send()
                break
        else:
            # If no tool call, it's a direct message response
            msg.content = response_message.content
            history.append({"role": "assistant", "content": msg.content})
            await msg.update()
            break  # Exit loop after sending the final message

    cl.user_session.set("history", history)
