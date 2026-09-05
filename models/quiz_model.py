"""
models/quiz_model.py
Defines the QuizModel class representing the application's data layer in the MVC pattern.
Responsible for managing quiz state, tracking score, evaluating answers, and calculating statistics.
"""

from typing import Any, Dict, List, Optional, Tuple


class QuizModel:
    """
    Model layer of the Quiz Application.
    
    Encapsulates all quiz-related data and business logic without any direct 
    user interaction or terminal output.
    """

    def __init__(self, questions: List[Dict[str, Any]]):
        """
        Initialize the quiz model with a list of questions and default state.
        
        :param questions: List of question dictionaries.
        """
        self.questions: List[Dict[str, Any]] = questions
        self.user_name: str = ""
        self.current_question_index: int = 0
        self.score: int = 0
        self.correct_answers: int = 0
        self.wrong_answers: int = 0

    def set_user_name(self, name: str) -> None:
        """Store the user's name."""
        self.user_name = name.strip()

    def get_user_name(self) -> str:
        """Return the user's name."""
        return self.user_name

    def get_total_questions(self) -> int:
        """Return the total number of questions."""
        return len(self.questions)

    def get_current_question_number(self) -> int:
        """Return the 1-based index of the current question."""
        return self.current_question_index + 1

    def has_more_questions(self) -> bool:
        """Check if there are remaining questions to answer."""
        return self.current_question_index < len(self.questions)

    def get_question(self) -> Optional[Dict[str, Any]]:
        """
        Retrieve the current question dictionary.
        
        :return: Question dictionary or None if all questions have been answered.
        """
        if self.has_more_questions():
            return self.questions[self.current_question_index]
        return None

    def increment_score(self) -> None:
        """Increase the user's score by 1 point."""
        self.score += 1

    def check_answer(self, user_answer: str) -> Tuple[bool, str, str]:
        """
        Validate the user's answer against the current question's correct answer.
        Updates score, correct_answers, and wrong_answers counters accordingly.
        
        :param user_answer: The letter choice entered by the user (e.g. 'A', 'B', 'C', 'D').
        :return: A tuple of (is_correct, correct_letter, correct_option_text).
        """
        current_q = self.get_question()
        if not current_q:
            return False, "", ""

        correct_letter = current_q["correct_answer"].strip().upper()
        correct_text = current_q["options"].get(correct_letter, "")
        user_choice = user_answer.strip().upper()

        if user_choice == correct_letter:
            self.increment_score()
            self.correct_answers += 1
            is_correct = True
        else:
            self.wrong_answers += 1
            is_correct = False

        return is_correct, correct_letter, correct_text

    def next_question(self) -> None:
        """Advance the question pointer to the next question."""
        self.current_question_index += 1

    def get_score(self) -> int:
        """Return the current score."""
        return self.score

    def get_result(self) -> Dict[str, Any]:
        """
        Calculate and return the final quiz summary including score, percentage,
        and performance feedback message.
        
        :return: Dictionary containing comprehensive quiz results.
        """
        total = self.get_total_questions()
        percentage = (self.correct_answers / total * 100) if total > 0 else 0.0

        # Performance evaluation rules
        if percentage >= 80.0:
            performance = "Excellent performance!"
        elif percentage >= 60.0:
            performance = "Good job!"
        elif percentage >= 40.0:
            performance = "Keep practicing!"
        else:
            performance = "You need more practice."

        return {
            "name": self.user_name,
            "total_questions": total,
            "correct_answers": self.correct_answers,
            "wrong_answers": self.wrong_answers,
            "score": self.score,
            "percentage": percentage,
            "performance": performance
        }

    def reset_quiz(self) -> None:
        """Reset the quiz state counters to allow replaying."""
        self.current_question_index = 0
        self.score = 0
        self.correct_answers = 0
        self.wrong_answers = 0
