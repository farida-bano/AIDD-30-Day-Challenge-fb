# Scientific Calculator - Web-Based Tool

## 📋 Project Overview
**Name:** Farida Bano  
**Roll No:** 00217635  

A **web-based scientific calculator** built using **Python** and **Streamlit** that performs both basic arithmetic and advanced scientific computations through an intuitive interface.

---

## 🎯 About the Project

This Scientific Calculator provides a **free, accessible, and reliable tool** for students, engineers, and professionals. With its user-friendly interface, users can perform both simple and complex calculations efficiently. Built with Streamlit, it runs directly in a web browser with minimal setup requirements.

### **Key Features**

#### 🧮 **Basic Arithmetic Operations**
- **Addition** (+)
- **Subtraction** (-)
- **Multiplication** (*)
- **Division** (/)

#### 🔬 **Scientific Functions**
- **Trigonometric:** sin, cos, tan, and their inverses (asin, acos, atan)
- **Logarithmic:** Base 10 (log) and natural (ln)
- **Exponential:** Power (^)
- **Roots:** Square root (√)
- **Factorial:** (!)

#### ⚙️ **Control & Utilities**
- **Constants:** π (pi) and e (Euler's number)
- **Parentheses:** Group expressions using ( and )
- **Backspace:** Delete last input (<-)
- **Clear:** Reset display (C)
- **Mode Switching:** Toggle between Degrees (DEG) and Radians (RAD)
- **History Tab:** View last 10 calculations
- **Answer Memory:** Reuse previous result using Ans button

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python |
| **Web Framework** | Streamlit |
| **Numerical Operations** | NumPy |
| **Math Functions** | Python's math module |

---

## 📖 How to Use

### 1. **Input Method**
- Click on-screen buttons to build your expression
- Use parentheses for complex expressions

### 2. **Calculation**
- Press **=** to evaluate the expression
- Use **Ans** button to insert previous result

### 3. **Mode Selection**
- Choose **DEG** or **RAD** before using trigonometric functions
- Default mode is **DEG**

### 4. **History Management**
- Review previous calculations in History tab
- Clear history when needed

---

## 🚀 Installation & Setup

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package installer)

### **Step-by-Step Setup**

```bash
# 1. Clone the Repository
git clone <repository-url>
cd <repository-directory>

# 2. Create Virtual Environment
python3 -m venv venv

# 3. Activate Virtual Environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install Dependencies
pip install -r requirements.txt

# 5. Run the Application
streamlit run calculator.py
```

### **Required Packages**
Create `requirements.txt` with:
```
streamlit==1.28.0
numpy==1.24.3
```

---

## 📁 Project Structure

```
scientific-calculator/
│
├── calculator.py              # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── history/                   # Calculation history logs
│   └── prompts/
│
└── specs/                     # Project planning documents
    ├── adr.md                # Architecture Decision Records
    ├── checklist.md          # Development checklist
    ├── plan.md              # Project plan
    └── tasks.md             # Task breakdown
```

---

## 🎨 Interface Components

### **Main Calculator Layout**
1. **Display Screen** - Shows current expression and result
2. **Number Pad** - Digits 0-9 and decimal point
3. **Basic Operations** - +, -, *, /
4. **Scientific Functions** - Trig, log, power, roots
5. **Control Buttons** - Clear, backspace, equals
6. **Mode Selector** - DEG/RAD toggle
7. **Constants** - π, e
8. **History Panel** - Previous calculations

---

## 🔧 Development Features

### **Error Handling**
- Division by zero prevention
- Invalid expression detection
- Overflow/underflow handling

### **User Experience**
- Responsive design
- Intuitive button layout
- Real-time expression validation
- Visual feedback for operations

### **Performance**
- Fast computation using NumPy
- Efficient memory usage
- Quick history access

---

## 📊 Sample Calculations

| Operation | Input | Result |
|-----------|--------|---------|
| Basic | `5 + 3 * 2` | `11` |
| Scientific | `sin(45)` | `0.7071` (in DEG) |
| Logarithmic | `log(100)` | `2` |
| Exponential | `2^8` | `256` |
| Factorial | `5!` | `120` |

---

## 🎯 Target Audience

### **1. Students**
- Mathematics and science homework
- Engineering calculations
- Physics problems

### **2. Professionals**
- Engineers
- Scientists
- Data analysts
- Researchers

### **3. Casual Users**
- Quick everyday calculations
- Financial computations
- Unit conversions

---

## 💡 Future Enhancements

### **Planned Features**
1. **Unit Conversion** - Length, weight, temperature
2. **Equation Solver** - Linear and quadratic equations
3. **Graphing Capabilities** - Function plotting
4. **Matrix Operations** - Addition, multiplication, determinant
5. **Statistics Functions** - Mean, median, standard deviation
6. **Custom Functions** - User-defined operations
7. **Themes** - Dark/light mode switching
8. **Mobile Optimization** - Touch-friendly interface

### **Technical Improvements**
- Database integration for history persistence
- User authentication for personalized settings
- API for third-party integration
- Export capabilities (CSV, PDF)

---

## 📝 Code Quality Standards

### **Testing**
- Unit tests for all mathematical functions
- Integration tests for user interactions
- Error scenario testing

### **Documentation**
- Comprehensive code comments
- User manual
- Developer guide

### **Performance**
- Load time optimization
- Memory efficiency
- Responsive interface

---

## 🤝 Contribution Guidelines

### **For Developers**
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

### **Code Style**
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings for functions
- Maintain consistent formatting

---

## 🏆 Summary

This project demonstrates how **Python** and **Streamlit** can be combined to create a powerful, interactive, and visually appealing scientific calculator. It serves as:

✅ **Educational Tool** - Learning mathematical concepts  
✅ **Professional Utility** - Quick and accurate computations  
✅ **Development Example** - Web application with Python  
✅ **Open Source Project** - Community-driven improvements  

The calculator is **ideal** for:
- Educational institutions
- Professional workplaces
- Personal use
- Development learning

---



**Developer:** Farida Bano  

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Last Updated: December 3, 2025*
