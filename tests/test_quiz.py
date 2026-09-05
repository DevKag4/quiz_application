"""
tests/test_quiz.py
Unit and integration tests for the Python MVC Quiz Application.
Uses standard library unittest module.
"""

import unittest
from models.quiz_model import QuizModel
from views.quiz_view import QuizView
from controllers.quiz_controller import QuizController


class TestQuizModel(unittest.TestCase):
    """Test suite for QuizModel state management and logic."""

    def setUp(self):
        self.sample_questions = [
            {
                "question": "What is Python?",
                "options": {"A": "Snake", "B": "Programming Language", "C": "Car", "D": "Planet"},
                "correct_answer": "B"
            },
            {
                "question": "What is 2 + 2?",
                "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
                "correct_answer": "B"
            },
            {
                "question": "Which keyword defines a function?",
                "options": {"A": "func", "B": "def", "C": "function", "D": "define"},
                "correct_answer": "B"
            },
            {
                "question": "What is type(5)?",
                "options": {"A": "int", "B": "float", "C": "str", "D": "list"},
                "correct_answer": "A"
            },
            {
                "question": "What is type(5.0)?",
                "options": {"A": "int", "B": "float", "C": "str", "D": "list"},
                "correct_answer": "B"
            }
        ]
        self.model = QuizModel(self.sample_questions)
        self.model.set_user_name("Alice")

    def test_initial_state(self):
        self.assertEqual(self.model.get_user_name(), "Alice")
        self.assertEqual(self.model.get_total_questions(), 5)
        self.assertEqual(self.model.get_current_question_number(), 1)
        self.assertEqual(self.model.get_score(), 0)
        self.assertTrue(self.model.has_more_questions())

    def test_check_answer_correct_and_case_insensitive(self):
        # First question correct answer is 'B'
        is_correct, correct_letter, correct_text = self.model.check_answer("b")
        self.assertTrue(is_correct)
        self.assertEqual(correct_letter, "B")
        self.assertEqual(correct_text, "Programming Language")
        self.assertEqual(self.model.get_score(), 1)
        self.assertEqual(self.model.correct_answers, 1)
        self.assertEqual(self.model.wrong_answers, 0)

    def test_check_answer_incorrect(self):
        # Answer with 'A' instead of 'B'
        is_correct, correct_letter, correct_text = self.model.check_answer("a")
        self.assertFalse(is_correct)
        self.assertEqual(correct_letter, "B")
        self.assertEqual(self.model.get_score(), 0)
        self.assertEqual(self.model.correct_answers, 0)
        self.assertEqual(self.model.wrong_answers, 1)

    def test_next_question_and_termination(self):
        for i in range(5):
            self.assertTrue(self.model.has_more_questions())
            self.assertEqual(self.model.get_current_question_number(), i + 1)
            self.model.next_question()
        self.assertFalse(self.model.has_more_questions())
        self.assertIsNone(self.model.get_question())

    def test_reset_quiz(self):
        self.model.check_answer("B")
        self.model.next_question()
        self.assertEqual(self.model.get_score(), 1)
        self.assertEqual(self.model.current_question_index, 1)

        self.model.reset_quiz()
        self.assertEqual(self.model.get_score(), 0)
        self.assertEqual(self.model.current_question_index, 0)
        self.assertEqual(self.model.correct_answers, 0)
        self.assertEqual(self.model.wrong_answers, 0)
        self.assertEqual(self.model.get_user_name(), "Alice")

    def test_performance_tiers(self):
        # Test 100% -> "Excellent performance!"
        for _ in range(5):
            self.model.check_answer("B" if self.model.get_question()["correct_answer"] == "B" else "A")
            self.model.next_question()
        result = self.model.get_result()
        self.assertEqual(result["percentage"], 100.0)
        self.assertEqual(result["performance"], "Excellent performance!")

        # Test 60% -> "Good job!"
        self.model.reset_quiz()
        self.model.correct_answers = 3
        self.model.wrong_answers = 2
        self.model.score = 3
        result = self.model.get_result()
        self.assertEqual(result["percentage"], 60.0)
        self.assertEqual(result["performance"], "Good job!")

        # Test 40% -> "Keep practicing!"
        self.model.reset_quiz()
        self.model.correct_answers = 2
        self.model.wrong_answers = 3
        self.model.score = 2
        result = self.model.get_result()
        self.assertEqual(result["percentage"], 40.0)
        self.assertEqual(result["performance"], "Keep practicing!")

        # Test 20% -> "You need more practice."
        self.model.reset_quiz()
        self.model.correct_answers = 1
        self.model.wrong_answers = 4
        self.model.score = 1
        result = self.model.get_result()
        self.assertEqual(result["percentage"], 20.0)
        self.assertEqual(result["performance"], "You need more practice.")


class TestQuizControllerEndToEnd(unittest.TestCase):
    """Simulate end-to-end user interaction through the controller without terminal blocking."""

    def test_controller_round_execution(self):
        questions = [
            {
                "question": "Q1?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "correct_answer": "A"
            }
        ]
        model = QuizModel(questions)
        view = QuizView()
        controller = QuizController(model, view)

        # Mock view methods so input() isn't invoked during test
        view.display_welcome = lambda: None
        view.get_user_name = lambda: "TestUser"
        view.display_question = lambda q, c, t: None
        view.get_answer = lambda: "A"
        view.display_correct_message = lambda: None
        view.display_wrong_message = lambda c, t: None
        view.display_result = lambda r: None
        view.get_replay_choice = lambda: False
        view.display_goodbye = lambda: None

        controller.start()

        self.assertEqual(model.get_user_name(), "TestUser")
        self.assertEqual(model.get_score(), 1)
        self.assertEqual(model.correct_answers, 1)
        self.assertEqual(model.wrong_answers, 0)


if __name__ == "__main__":
    unittest.main()
