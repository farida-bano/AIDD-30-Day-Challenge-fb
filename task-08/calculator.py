import streamlit as st
import numpy as np
import math
import re

# Page configuration
st.set_page_config(layout="wide", page_title="Scientific Calculator")

# Custom CSS for styling
st.markdown("""
    <style>
        .st-emotion-cache-1z15u2o {
            font-size: 2.2rem;
            text-align: right;
        }
        .stButton>button {
            height: 70px;
            font-size: 1.4rem;
            border-radius: 10px;
            margin: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'history' not in st.session_state:
    st.session_state.history = []
if 'memory' not in st.session_state:
    st.session_state.memory = 0.0
if 'last_ans' not in st.session_state:
    st.session_state.last_ans = 0.0
if 'radians_mode' not in st.session_state:
    st.session_state.radians_mode = True

# Main display
st.markdown(f"<div class='st-emotion-cache-1z15u2o'>{st.session_state.display}</div>", unsafe_allow_html=True)

# --- Button Logic ---
def handle_click(value):
    st.session_state.display += str(value)

def handle_clear():
    st.session_state.display = ""

def handle_equals():
    try:
        expression = st.session_state.display
        # Replace special characters for eval
        expression = expression.replace("π", "math.pi").replace("e", "math.e").replace("^", "**")
        expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)

        # Handle trig functions based on mode
        if st.session_state.radians_mode:
            safe_namespace = {
                'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                'asin': np.arcsin, 'acos': np.arccos, 'atan': np.arctan,
                'log': np.log10, 'ln': np.log, 'sqrt': np.sqrt,
                'math': math, 'factorial': math.factorial
            }
        else: # Degrees mode
            safe_namespace = {
                'sin': lambda x: np.sin(np.deg2rad(x)),
                'cos': lambda x: np.cos(np.deg2rad(x)),
                'tan': lambda x: np.tan(np.deg2rad(x)),
                'asin': lambda x: np.rad2deg(np.arcsin(x)),
                'acos': lambda x: np.rad2deg(np.arccos(x)),
                'atan': lambda x: np.rad2deg(np.arctan(x)),
                'log': np.log10, 'ln': np.log, 'sqrt': np.sqrt,
                'math': math, 'factorial': math.factorial
            }

        result = eval(expression, {"__builtins__": None}, safe_namespace)
        st.session_state.last_ans = result
        st.session_state.history.insert(0, f"{expression} = {result}")
        if len(st.session_state.history) > 10:
            st.session_state.history.pop()
        st.session_state.display = str(result)
    except Exception as e:
        st.session_state.display = "Error"

# --- UI Layout ---
tab1, tab2, tab3 = st.tabs(["Calculator", "History", "Help"])

with tab1:
    # Mode Toggle
    col_mode1, col_mode2 = st.columns(2)
    with col_mode1:
        if st.button("DEG"):
            st.session_state.radians_mode = False
    with col_mode2:
        if st.button("RAD"):
            st.session_state.radians_mode = True
    st.write(f"Current Mode: {'RAD' if st.session_state.radians_mode else 'DEG'}")


    # Calculator buttons
    buttons = [
        ['sin', 'cos', 'tan', 'sqrt', '^'],
        ['asin', 'acos', 'atan', 'log', 'ln'],
        ['(', ')', 'π', 'e', '!'],
        ['7', '8', '9', '/', 'C'],
        ['4', '5', '6', '*', '<-'],
        ['1', '2', '3', '-', 'Ans'],
        ['0', '.', '%', '+', '=']
    ]

    for row in buttons:
        cols = st.columns(5)
        for i, label in enumerate(row):
            if label == "=":
                cols[i].button(label, on_click=handle_equals, use_container_width=True)
            elif label == "C":
                cols[i].button(label, on_click=handle_clear, use_container_width=True)
            elif label == "Ans":
                cols[i].button(label, on_click=handle_click, args=(st.session_state.last_ans,), use_container_width=True)
            elif label == "<-":
                if cols[i].button(label, use_container_width=True):
                    st.session_state.display = st.session_state.display[:-1]
            else:
                cols[i].button(label, on_click=handle_click, args=(label,), use_container_width=True)

with tab2:
    st.header("Calculation History")
    for item in st.session_state.history:
        st.write(item)
    if st.button("Clear History"):
        st.session_state.history = []

with tab3:
    st.header("Help")
    st.write("This is a scientific calculator.")
    st.write("Work in progress.")
