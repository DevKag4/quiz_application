"""
main.py
Application entry point for the Python MVC Command-Line Quiz Application.
"""

import sys
import os

# Ensure the project root directory is in sys.path when running main.py directly
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from data.questions import QUESTIONS
from models.quiz_model import QuizModel
from views.quiz_view import QuizView
from controllers.quiz_controller import QuizController


def main() -> None:
    """Instantiate MVC components and initiate the application lifecycle."""
    # 1. Initialize the Model with questions data
    model = QuizModel(questions=QUESTIONS)

    # 2. Initialize the View for terminal rendering & input
    view = QuizView()

    # 3. Initialize the Controller with Model and View
    controller = QuizController(model=model, view=view)

    # 4. Start the quiz application
    controller.start()


if __name__ == "__main__":
    main()
