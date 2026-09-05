# Python MVC Command-Line Quiz Application

A robust, modular, and beginner-friendly command-line Quiz Application built in Python using the **Model-View-Controller (MVC)** architectural pattern. Designed with clean separation of concerns, zero external dependencies, robust input validation, and an interactive terminal experience.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Key Features](#key-features)
3. [Technologies Used](#technologies-used)
4. [Understanding MVC Architecture](#understanding-mvc-architecture)
5. [Project Structure](#project-structure)
6. [MVC Component Breakdown](#mvc-component-breakdown)
   - [Model Layer (`models/`)](#1-model-layer-modelsquiz_modelpy)
   - [View Layer (`views/`)](#2-view-layer-viewsquiz_viewpy)
   - [Controller Layer (`controllers/`)](#3-controller-layer-controllersquiz_controllerpy)
   - [Data Layer (`data/`)](#4-data-layer-dataquestionspy)
   - [Application Entry Point (`main.py`)](#5-entry-point-mainpy)
7. [Installation & Setup](#installation--setup)
8. [How to Run](#how-to-run)
9. [Example Terminal Output](#example-terminal-output)
10. [Score & Performance Evaluation Rules](#score--performance-evaluation-rules)
11. [Python Concepts Demonstrated](#python-concepts-demonstrated)
12. [Future Improvements](#future-improvements)

---

## Project Description

The **Python MVC Quiz Application** is an interactive, console-based quiz game that challenges users on core Python concepts including variables, data types, loops, functions, lists, dictionaries, exception handling, and more. 

The application is architected from the ground up following the industry-standard **Model-View-Controller (MVC)** design pattern. This architecture ensures that data management, user interface rendering, and application workflow are completely decoupled into distinct, maintainable modules.

---

## Key Features

- **Strict MVC Architecture:** Clean separation of concerns between data, presentation, and flow control.
- **Interactive Console UI:** Clean borders, formatted questions, and intuitive layout.
- **Robust Input Validation:**
  - Case-insensitive answer acceptance (`a`, `A`, `b`, `B`, `c`, `C`, `d`, `D`).
  - Gracefully catches invalid choices or empty inputs without crashing.
  - Re-prompts the user until a valid option is provided.
- **Real-Time Feedback:** Immediately informs the user if their choice was correct or incorrect, revealing the correct answer on mistakes.
- **Dynamic Score & Performance Calculation:**
  - Computes score, percentage, and tailored qualitative feedback (e.g., "Excellent performance!").
- **Replay Functionality:** Option to restart the quiz seamlessly without restarting the Python process.
- **Zero Third-Party Dependencies:** Built exclusively with the Python Standard Library.

---

## Technologies Used

- **Language:** Python (version 3.8 or higher recommended)
- **Standard Library Modules:** `sys`, `os`, `typing`, `unittest`
- **Dependencies:** None (No third-party packages required)

---

## Understanding MVC Architecture

The **Model-View-Controller (MVC)** pattern divides an application into three interconnected components:

```
                  +-----------------------+
                  |      User Action      |
                  +-----------------------+
                              |
                              v
                  +-----------------------+
                  |      Controller       |
                  | (quiz_controller.py)  |
                  +-----------------------+
                   /                     \
      Sends User Input / Updates     Fetches Data / Decides View
                 /                         \
                v                           v
     +---------------------+     +---------------------+
     |        Model        |     |        View         |
     |   (quiz_model.py)   |     |   (quiz_view.py)    |
     +---------------------+     +---------------------+
     - Stores State & Score      - Prints to Terminal
     - Checks Answers            - Captures User Input
     - Calculates Percentage     - Formats Result Card
```

### In Simple Terms:
- **Model:** *"What data do we have, and what are the rules?"* — It manages the questions, tracks the score, checks if answers are right or wrong, and calculates the final percentage. It does **not** print anything to the screen.
- **View:** *"How does it look to the user?"* — It prints banners, questions, menus, and results to the terminal, and prompts the user for text input. It has **no** business logic or scoring calculations.
- **Controller:** *"What should happen next?"* — It acts as the brain or traffic controller between the Model and View. It asks the View to display a question, captures the user's input, sends the input to the Model for checking, tells the View what feedback to show, and handles quiz replay or exit.

---

## Project Structure

```text
quiz_application/
│
├── main.py                  # Application entry point
│
├── models/                  # Model layer
│   ├── __init__.py
│   └── quiz_model.py        # Manages quiz state, scoring, and calculations
│
├── views/                   # View layer
│   ├── __init__.py
│   └── quiz_view.py         # Manages terminal presentation and user input
│
├── controllers/             # Controller layer
│   ├── __init__.py
│   └── quiz_controller.py   # Coordinates application flow between Model and View
│
├── data/                    # Quiz question data
│   ├── __init__.py
│   └── questions.py         # Curated list of Python multiple-choice questions
│
├── tests/                   # Automated unit & integration tests
│   └── test_quiz.py
│
├── README.md                # Project documentation
└── requirements.txt         # Dependency documentation (zero external dependencies)
```

### Role of Directories:
- `models/` = **Model layer** (manages state and data logic).
- `views/` = **View layer** (handles terminal I/O and display formatting).
- `controllers/` = **Controller layer** (orchestrates Model and View).
- `data/` = **Quiz question data** (stores raw questions and answers).
- `main.py` = **Application entry point** (instantiates and runs the application).

---

## MVC Component Breakdown

### 1. Model Layer (`models/quiz_model.py`)
The `QuizModel` class manages all data and business logic:
- Tracks `questions`, `current_question_index`, `user_name`, `score`, `correct_answers`, and `wrong_answers`.
- **Key Methods:**
  - `get_question()`: Retrieves the current question dictionary.
  - `check_answer(user_answer)`: Compares user choice with the correct answer, updates internal counters, and returns validation status.
  - `increment_score()`: Increases score count.
  - `get_score()`: Returns current score.
  - `get_result()`: Computes total questions, correct/wrong counts, percentage, and qualitative performance message.
  - `reset_quiz()`: Resets question index and counters for a fresh game.
- **Clean Architecture Principle:** Contains zero `print()` or `input()` calls.

### 2. View Layer (`views/quiz_view.py`)
The `QuizView` class is responsible for all visual output and console input:
- **Key Methods:**
  - `display_welcome()`: Renders the welcome banner.
  - `get_user_name()`: Prompts for the player's name and handles empty inputs.
  - `display_question()`: Neatly prints question number, question text, and options (A, B, C, D).
  - `get_answer()`: Prompts for user answer, validates input, and handles invalid or blank inputs gracefully.
  - `display_correct_message()` / `display_wrong_message()`: Displays contextual feedback.
  - `display_result()`: Prints the summary card with clean borders and aligned statistics.
  - `get_replay_choice()`: Validates whether the user wishes to replay (`yes`/`y`/`no`/`n`).
  - `display_goodbye()`: Displays exit farewell.
- **Clean Architecture Principle:** Contains zero score calculations or game state evaluations.

### 3. Controller Layer (`controllers/quiz_controller.py`)
The `QuizController` class manages application lifecycle:
- Accepts instances of `QuizModel` and `QuizView`.
- **Workflow:**
  1. Calls `view.display_welcome()`.
  2. Prompts user name via `view.get_user_name()` and sets it in `model`.
  3. Loops through questions:
     - Retrieves question from `model`.
     - Displays question using `view`.
     - Collects answer through `view`.
     - Evaluates answer via `model.check_answer()`.
     - Informs `view` to show correct/incorrect feedback.
     - Advances `model.next_question()`.
  4. Fetches final results from `model.get_result()` and instructs `view.display_result()`.
  5. Queries `view.get_replay_choice()`. Resets model if replaying, or terminates cleanly.

### 4. Data Layer (`data/questions.py`)
Stores the question bank as a list of dictionaries. Each question contains:
- `question`: The question text.
- `options`: A dictionary of options with keys `"A"`, `"B"`, `"C"`, and `"D"`.
- `correct_answer`: The letter key of the correct option.

### 5. Entry Point (`main.py`)
A lightweight, beginner-friendly entry point that initializes the Model, View, and Controller, and calls `controller.start()`.

---

## Installation & Setup

1. **Prerequisites:**
   Ensure Python 3.8 or higher is installed on your computer. You can check your version by running:
   ```bash
   python --version
   ```

2. **Clone / Download the Repository:**
   ```bash
   git clone https://github.com/your-username/quiz-application.git
   cd quiz-application
   ```

3. **Dependencies:**
   No external packages or `pip install` commands are needed!

---

## How to Run

Run the application using Python from your terminal:

```bash
python main.py
```

To run the automated tests:
```bash
python -m unittest discover -s tests
```

---

## Example Terminal Output

```text
========================================
        PYTHON QUIZ APPLICATION
========================================

Enter your name: Dev

Welcome Dev! Let's start the quiz.

----------------------------------------
Question 1/12
----------------------------------------

What is the correct file extension for Python files?

A. .java
B. .py
C. .html
D. .cpp

Enter your answer: B

Correct!

----------------------------------------
Question 2/12
----------------------------------------

Which keyword is used to define a function in Python?

A. func
B. define
C. def
D. function

Enter your answer: z

Invalid choice!
Please enter A, B, C, or D.

Enter your answer: c

Correct!

...

========================================
             QUIZ RESULT
========================================

Name: Dev
Total Questions: 12
Correct Answers: 10
Wrong Answers: 2
Score: 10/12
Percentage: 83.3%

Performance: Excellent performance!

========================================

Do you want to play again? (yes/no): no

Thank you for playing the Python Quiz! Happy coding!
```

---

## Score & Performance Evaluation Rules

The percentage is computed dynamically as:
$$\text{Percentage} = \left( \frac{\text{Correct Answers}}{\text{Total Questions}} \right) \times 100$$

Performance feedback is assigned according to the following thresholds:
| Percentage Range | Performance Message |
| :--- | :--- |
| **80% and above** | `"Excellent performance!"` |
| **60% – 79%** | `"Good job!"` |
| **40% – 59%** | `"Keep practicing!"` |
| **Below 40%** | `"You need more practice."` |

---

## Python Concepts Demonstrated

This project is tailored for beginners, freshers, and portfolio reviews, showcasing fundamental Python capabilities:

- **Object-Oriented Programming (OOP):** Class design, encapsulation, separation of concerns, `__init__` constructors, and methods.
- **Architectural Patterns:** Implementation of Model-View-Controller (MVC).
- **Data Structures:**
  - `List`: Storing sequence of questions.
  - `Dictionary`: Storing question text, option choices, and result statistics.
  - `Tuple`: Returning multiple values from methods cleanly.
- **Control Flow:** `while` loops for input loops and replays, `for` loops for iterating options, and `if/elif/else` conditional logic.
- **String Manipulation:** Case conversion (`.strip()`, `.upper()`, `.lower()`), string formatting (`f-strings`), and border creation.
- **Input Validation & Exception Handling:** Graceful recovery from empty strings, invalid choices, and `KeyboardInterrupt` / `EOFError`.
- **Modular Code Organization:** Python packages, `__init__.py`, and relative/absolute imports.

---

## Future Improvements

- **Question Categories / Difficulties:** Add filters for Beginner, Intermediate, and Advanced topics.
- **Timer Feature:** Introduce a countdown timer for each question.
- **Persistent High Scores:** Save player scores and leaderboards to a JSON or CSV file.
- **Randomized Questions:** Shuffle questions and answer choices on every round.
