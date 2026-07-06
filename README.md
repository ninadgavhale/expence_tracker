# Expense Tracker (CLI)

A command-line Expense Tracker built with Python that allows users to record, view, delete, and calculate expenses. The application stores data in a JSON file, ensuring that expenses persist across multiple program executions.

---

## Project Overview

This project was developed to strengthen core Python programming concepts, including:

* Functions and modular programming
* Lists and dictionaries
* File handling
* JSON serialization and deserialization
* Exception handling
* Basic CRUD (Create, Read, Update, Delete) operations

---

## Features

* Add new expenses
* View all saved expenses
* Delete expenses by description
* Calculate total expenses
* Automatically save data to a JSON file
* Automatically load saved data when the application starts
* Handle invalid numeric input using exception handling

---

## Project Structure

```text
expense_tracker/
│
├── expense_tracker.py
├── storage.json
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python 3
* JSON
* File Handling
* Exception Handling

---

## How It Works

1. The application loads previously saved expenses from `storage.json`.
2. Users interact with the application through a menu-driven interface.
3. Expenses are stored in memory as a list of dictionaries.
4. Whenever an expense is added or deleted, the updated list is automatically saved to the JSON file.
5. On the next execution, the saved expenses are loaded back into the application.

---

## Example Menu

```text
Expense Tracker Menu

1. Add Expense
2. View Expenses
3. Delete Expense
4. Show Total Expenses
5. Exit
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/ninadgavhale/expense_tracker.git
```

### Navigate to the project directory

```bash
cd expense_tracker
```

### Run the application

```bash
python expense_tracker.py
```

---

## Example Expense Format

```json
[
    {
        "amount": 250,
        "description": "Food"
    },
    {
        "amount": 1200,
        "description": "Fuel"
    }
]
```

---

## Skills Demonstrated

* Python Programming
* Problem Solving
* Modular Code Design
* JSON Data Storage
* File I/O
* Exception Handling
* Data Structures (Lists & Dictionaries)

---

## Future Improvements

* Validate negative expense amounts
* Add expense categories
* Add timestamps for each expense
* Search expenses by keyword
* Edit existing expenses
* Export expenses to CSV
* Build a graphical user interface (GUI)

---

## Author

**Ninad Gavhale**

This project is part of my Python learning journey and demonstrates the application of core programming concepts through a practical command-line application.
