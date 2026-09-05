"""
views/quiz_view.py
Defines the QuizView class representing the View layer in the MVC pattern.
Responsible for all user interface formatting, console rendering, and terminal input collection.
"""

from typing import Any, Dict


class QuizView:
    """
    View layer of the Quiz Application.
    
    Handles all console presentation and terminal input collection.
    Does NOT contain business logic or score calculation.
    """

    BORDER_LINE = "=" * 40
    SEPARATOR_LINE = "-" * 40
    VALID_OPTIONS = ("A", "B", "C", "D")

    def display_welcome(self) -> None:
        """Display the formatted application welcome banner."""
        print()
        print(self.BORDER_LINE)
        print("        PYTHON QUIZ APPLICATION")
        print(self.BORDER_LINE)
        print()

    def get_user_name(self) -> str:
        """
        Prompt the user for their name and ensure non-empty input.
        
        :return: Trimmed user name string.
        """
        while True:
            try:
                name = input("Enter your name: ").strip()
                if name:
                    print(f"\nWelcome {name}! Let's start the quiz.\n")
                    return name
                print("Name cannot be empty. Please enter your name.\n")
            except (KeyboardInterrupt, EOFError):
                print("\n\nSession cancelled by user. Exiting...")
                raise

    def display_question(self, question_data: Dict[str, Any], current_num: int, total_questions: int) -> None:
        """
        Render a single question and its options cleanly in the terminal.
        
        :param question_data: Dictionary containing 'question' and 'options'.
        :param current_num: 1-based index of the current question.
        :param total_questions: Total number of questions in the quiz.
        """
        print(self.SEPARATOR_LINE)
        print(f"Question {current_num}/{total_questions}")
        print(self.SEPARATOR_LINE)
        print()
        print(question_data["question"])
        print()

        options = question_data.get("options", {})
        for key in self.VALID_OPTIONS:
            if key in options:
                print(f"{key}. {options[key]}")
        print()

    def get_answer(self) -> str:
        """
        Prompt user to choose an answer option (A, B, C, or D).
        Validates the input and repeatedly prompts if invalid.
        
        :return: Normalized uppercase letter choice ('A', 'B', 'C', or 'D').
        """
        while True:
            try:
                user_input = input("Enter your answer: ").strip().upper()
                if user_input in self.VALID_OPTIONS:
                    return user_input
                
                print("\nInvalid choice!")
                print("Please enter A, B, C, or D.\n")
            except (KeyboardInterrupt, EOFError):
                print("\n\nInput cancelled. Exiting...")
                raise

    def display_correct_message(self) -> None:
        """Display positive feedback for a correct response."""
        print("\nCorrect!\n")

    def display_wrong_message(self, correct_answer: str, correct_option_text: str) -> None:
        """
        Display feedback for an incorrect response along with the correct choice.
        
        :param correct_answer: The correct letter option (e.g., 'B').
        :param correct_option_text: The description of the correct option.
        """
        print(f"\nIncorrect! The correct answer was {correct_answer}. {correct_option_text}\n")

    def display_result(self, result_data: Dict[str, Any]) -> None:
        """
        Display the final quiz summary card including score and performance rating.
        
        :param result_data: Dictionary containing name, total_questions, correct_answers,
                            wrong_answers, score, percentage, and performance.
        """
        percentage = result_data["percentage"]
        # Format percentage cleanly (e.g., 80% or 83.3%)
        pct_formatted = f"{percentage:.1f}%" if percentage % 1 != 0 else f"{int(percentage)}%"

        print(self.BORDER_LINE)
        print("             QUIZ RESULT")
        print(self.BORDER_LINE)
        print()
        print(f"Name: {result_data['name']}")
        print(f"Total Questions: {result_data['total_questions']}")
        print(f"Correct Answers: {result_data['correct_answers']}")
        print(f"Wrong Answers: {result_data['wrong_answers']}")
        print(f"Score: {result_data['score']}/{result_data['total_questions']}")
        print(f"Percentage: {pct_formatted}")
        print()
        print(f"Performance: {result_data['performance']}")
        print()
        print(self.BORDER_LINE)
        print()

    def get_replay_choice(self) -> bool:
        """
        Prompt user whether they wish to replay the quiz.
        Accepts 'yes', 'y', 'no', 'n' (case-insensitive).
        
        :return: True if user wants to play again, False otherwise.
        """
        while True:
            try:
                choice = input("Do you want to play again? (yes/no): ").strip().lower()
                if choice in ("yes", "y"):
                    return True
                if choice in ("no", "n"):
                    return False
                
                print("Invalid input! Please enter 'yes' or 'no'.\n")
            except (KeyboardInterrupt, EOFError):
                print("\n\nInput cancelled. Exiting...")
                return False

    def display_goodbye(self) -> None:
        """Display exit farewell message."""
        print("\nThank you for playing the Python Quiz! Happy coding!\n")
