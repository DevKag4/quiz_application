"""
data/questions.py
Contains beginner-friendly multiple-choice questions covering core Python fundamentals.
"""

QUESTIONS = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": {
            "A": ".java",
            "B": ".py",
            "C": ".html",
            "D": ".cpp"
        },
        "correct_answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "func",
            "B": "define",
            "C": "def",
            "D": "function"
        },
        "correct_answer": "C"
    },
    {
        "question": "What data type is the result of 10 / 2 in Python 3?",
        "options": {
            "A": "int",
            "B": "float",
            "C": "str",
            "D": "bool"
        },
        "correct_answer": "B"
    },
    {
        "question": "Which of the following data structures is immutable?",
        "options": {
            "A": "List",
            "B": "Dictionary",
            "C": "Set",
            "D": "Tuple"
        },
        "correct_answer": "D"
    },
    {
        "question": "How do you insert an element at the end of a list named 'my_list'?",
        "options": {
            "A": "my_list.add(5)",
            "B": "my_list.append(5)",
            "C": "my_list.insert_end(5)",
            "D": "my_list.push(5)"
        },
        "correct_answer": "B"
    },
    {
        "question": "What does the input() function always return by default in Python 3?",
        "options": {
            "A": "Integer (int)",
            "B": "Float (float)",
            "C": "String (str)",
            "D": "Boolean (bool)"
        },
        "correct_answer": "C"
    },
    {
        "question": "Which operator is used for integer (floor) division in Python?",
        "options": {
            "A": "/",
            "B": "//",
            "C": "%",
            "D": "**"
        },
        "correct_answer": "B"
    },
    {
        "question": "How do you access the value associated with key 'name' in dictionary 'student'?",
        "options": {
            "A": "student.name",
            "B": "student('name')",
            "C": "student['name']",
            "D": "student->name"
        },
        "correct_answer": "C"
    },
    {
        "question": "Which keyword is used to handle exceptions in a try block?",
        "options": {
            "A": "catch",
            "B": "except",
            "C": "error",
            "D": "handle"
        },
        "correct_answer": "B"
    },
    {
        "question": "What is the output of range(3) when converted into a list: list(range(3))?",
        "options": {
            "A": "[1, 2, 3]",
            "B": "[0, 1, 2]",
            "C": "[0, 1, 2, 3]",
            "D": "[1, 2]"
        },
        "correct_answer": "B"
    },
    {
        "question": "Which conditional keyword represents 'else if' in Python?",
        "options": {
            "A": "elseif",
            "B": "else if",
            "C": "elif",
            "D": "case"
        },
        "correct_answer": "C"
    },
    {
        "question": "What will be the output of len('Python')?",
        "options": {
            "A": "5",
            "B": "6",
            "C": "7",
            "D": "Error"
        },
        "correct_answer": "B"
    }
]
