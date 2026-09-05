"""
controllers/quiz_controller.py
Defines the QuizController class representing the Controller layer in the MVC pattern.
Coordinates communication between the QuizModel and QuizView to drive the application lifecycle.
"""

from models.quiz_model import QuizModel
from views.quiz_view import QuizView


class QuizController:
    """
    Controller layer of the Quiz Application.
    
    Acts as the intermediary between QuizModel and QuizView:
    - Obtains user inputs from the View.
    - Updates and queries the Model.
    - Instructs the View on what to present next.
    """

    def __init__(self, model: QuizModel, view: QuizView):
        """
        Initialize the controller with references to the Model and View.
        
        :param model: QuizModel instance managing data and state.
        :param view: QuizView instance managing terminal display and input.
        """
        self.model = model
        self.view = view

    def start(self) -> None:
        """
        Start and manage the main application lifecycle.
        Runs the quiz, delivers feedback, calculates results, and handles replays.
        """
        try:
            # 1. Display welcome banner
            self.view.display_welcome()

            # 2. Collect user's name and store in the model
            user_name = self.view.get_user_name()
            self.model.set_user_name(user_name)

            # 3. Main quiz loop (supports replaying)
            while True:
                self._run_quiz_round()

                # Display final result summary
                result_summary = self.model.get_result()
                self.view.display_result(result_summary)

                # Check if user wants to play again
                play_again = self.view.get_replay_choice()
                if play_again:
                    self.model.reset_quiz()
                    print("\nStarting a new quiz round...\n")
                else:
                    self.view.display_goodbye()
                    break

        except (KeyboardInterrupt, EOFError):
            print("\nExiting application. Goodbye!")

    def _run_quiz_round(self) -> None:
        """Run through all questions in the model for the current round."""
        total_questions = self.model.get_total_questions()

        while self.model.has_more_questions():
            current_num = self.model.get_current_question_number()
            question_data = self.model.get_question()

            # Render question via View
            self.view.display_question(question_data, current_num, total_questions)

            # Receive and validate input choice from user via View
            user_choice = self.view.get_answer()

            # Evaluate answer via Model
            is_correct, correct_letter, correct_text = self.model.check_answer(user_choice)

            # Display outcome feedback via View
            if is_correct:
                self.view.display_correct_message()
            else:
                self.view.display_wrong_message(correct_letter, correct_text)

            # Move to next question in Model
            self.model.next_question()
