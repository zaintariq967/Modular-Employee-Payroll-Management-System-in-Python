# Modular Employee Payroll Management System Using Python

A console-based **Employee Payroll Management System** developed in Python to demonstrate **modular programming**, reusable functions, and structured application design. The application automates payroll processing by collecting employee information, calculating bonuses, allowances, gross salary, and net salary, and generating a formatted salary slip. The project emphasizes clean code organization through separate modules, making it easy to understand, maintain, and extend.

---

## Features

- Employee information management
- Bonus calculation (10%)
- Allowance calculation (15%)
- Gross salary calculation
- Net salary calculation after tax deduction
- Formatted salary slip generation
- Modular project architecture
- Clean and reusable code

---

## Project Structure

```text
Employee-Payroll-Management-System-in-Python/
│
├── employee.py      # Employee input module
├── payroll.py       # Payroll calculations
├── main.py          # Main application
├── README.md
└── LICENSE
```

---

## Technologies Used

- Python 3
- Functions
- Modules
- Import Statements
- Import Aliasing
- Modular Programming
- f-Strings
- Console-Based Application

---

## Modules

### `employee.py`

Responsible for collecting employee information:

- Employee Name
- Employee ID
- Basic Salary

### `payroll.py`

Contains payroll-related calculations:

- Bonus Calculation
- Allowance Calculation
- Gross Salary Calculation
- Net Salary Calculation

### `main.py`

Acts as the main controller of the application by:

- Importing required modules
- Collecting employee details
- Performing payroll calculations
- Displaying the formatted salary slip

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/zaintariq967/Employee-Payroll-Management-System-in-Python.git
```

### 2. Navigate to the project directory

```bash
cd Employee-Payroll-Management-System-in-Python
```

### 3. Run the application

```bash
python main.py
```

---

## Sample Output

```text
===================================
          SALARY SLIP
===================================
Employee Name : Zain
Employee ID   : EMP101
Basic Salary  : 50000.00

Bonus         : 5000.00
Allowance     : 7500.00
Gross Salary  : 62500.00
Net Salary    : 59375.00
===================================
```

*Replace this section with a screenshot of your program output if desired.*

---

## Learning Outcomes

This project demonstrates:

- Python Functions
- Modules and Imports
- Import Aliasing
- Modular Programming
- User Input Handling
- Arithmetic Operations
- Formatted Output using f-Strings
- Console-Based Application Development
- Clean Code Organization

---

## Future Improvements

- Automatic Employee ID Generation
- File Handling for Employee Records
- Database Integration (SQLite/MySQL)
- Object-Oriented Programming (OOP) Implementation
- Graphical User Interface (Tkinter or PyQt)
- PDF Salary Slip Generation
- Employee Record Search and Management

---

## License

This project is open-source and intended for educational and learning purposes.
