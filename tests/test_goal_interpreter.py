import unittest
from app.nlp.goal_interpreter import GoalInterpreter

class TestGoalInterpreter(unittest.TestCase):
    def test_interpretation_response(self):
        gi = GoalInterpreter()
        result = gi.interpret("I want to build muscle.")
        self.assertTrue(isinstance(result, str))
        self.assertIn("muscle", result.lower())

if __name__ == "__main__":
    unittest.main()