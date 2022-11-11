import unittest
import run


class TestRun(unittest.TestCase):
    """
    Automated testing.
    """
    def test_InputParser(self):
        """
        Testing input_parser()
        """
        result = run.input_parser("/genre,horror")
        correct_result = ['_no_data*', '_no_data*', 'horror', '_no_data*', '_no_data*', '_no_data*']
        self.assertEqual(result, correct_result)
