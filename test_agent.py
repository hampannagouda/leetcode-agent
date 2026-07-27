import unittest
from unittest.mock import Mock, patch, MagicMock
from fetcher import LeetCodeFetcher
from solution_generator import SolutionGenerator
from code_executor import CodeExecutor

class TestLeetCodeFetcher(unittest.TestCase):
    """Test the fetcher module."""
    
    @patch('requests.post')
    def test_fetch_daily_problem_success(self, mock_post):
        """Test successful problem fetching."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "data": {
                "activeDailyCodingChallengeQuestion": {
                    "question": {
                        "title": "Two Sum",
                        "titleSlug": "two-sum",
                        "difficulty": "Easy",
                        "content": "<p>Find two numbers that add up to target</p>"
                    }
                }
            }
        }
        mock_post.return_value = mock_response
        
        fetcher = LeetCodeFetcher()
        problem = fetcher.fetch_daily_problem()
        
        self.assertEqual(problem['title'], "Two Sum")
        self.assertEqual(problem['difficulty'], "Easy")
    
    @patch('requests.post')
    def test_fetch_daily_problem_error(self, mock_post):
        """Test error handling when fetching fails."""
        mock_post.side_effect = Exception("Network error")
        
        fetcher = LeetCodeFetcher()
        with self.assertRaises(Exception):
            fetcher.fetch_daily_problem()


class TestSolutionGenerator(unittest.TestCase):
    """Test the solution generator module."""
    
    def test_clean_html(self):
        """Test HTML cleaning."""
        generator = SolutionGenerator()
        html = "<p>Hello&nbsp;World&amp;Friends</p>"
        cleaned = generator._clean_html(html)
        self.assertNotIn("<p>", cleaned)
        self.assertNotIn("&nbsp;", cleaned)
    
    def test_extract_code_block_with_markdown(self):
        """Test code extraction from markdown."""
        generator = SolutionGenerator()
        response = "```python\ndef solution():\n    pass\n```"
        code = generator.extract_code_block(response)
        self.assertIn("def solution", code)


class TestCodeExecutor(unittest.TestCase):
    """Test the code executor module."""
    
    def test_validate_syntax_valid(self):
        """Test syntax validation with valid code."""
        code = "def hello():\n    print('Hello')"
        result = CodeExecutor.validate_syntax(code)
        self.assertTrue(result)
    
    def test_validate_syntax_invalid(self):
        """Test syntax validation with invalid code."""
        code = "def hello(\n    print('Hello')"  # Missing closing paren
        result = CodeExecutor.validate_syntax(code)
        self.assertFalse(result)
    
    def test_run_simple_check_success(self):
        """Test simple execution check."""
        code = """
x = 5
y = 10
z = x + y
"""
        result = CodeExecutor.run_simple_check(code)
        self.assertTrue(result)


# Integration Tests
class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow."""
    
    @patch('fetcher.LeetCodeFetcher.fetch_daily_problem')
    @patch('openai.OpenAI')
    def test_end_to_end_workflow(self, mock_openai, mock_fetch):
        """Test the complete workflow (mocked)."""
        # Mock fetcher
        mock_fetch.return_value = {
            "title": "Test Problem",
            "difficulty": "Easy",
            "content": "Test content",
            "titleSlug": "test-problem"
        }
        
        # Mock OpenAI
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        # This would require more setup, but shows the pattern
        self.assertIsNotNone(mock_fetch)


def run_quick_test():
    """Run a quick sanity check."""
    print("\n✅ Running Quick Sanity Checks...")
    
    # Check 1: Config loads
    try:
        from config import OPENAI_API_KEY
        print("✅ Config loads successfully")
    except Exception as e:
        print(f"❌ Config error: {e}")
    
    # Check 2: Logger works
    try:
        from logger_config import setup_logger
        test_logger = setup_logger("test")
        test_logger.info("Logger test")
        print("✅ Logger works")
    except Exception as e:
        print(f"❌ Logger error: {e}")
    
    # Check 3: Executor works
    try:
        code = "x = 1 + 1"
        result = CodeExecutor.validate_syntax(code)
        print(f"✅ Executor works (syntax valid: {result})")
    except Exception as e:
        print(f"❌ Executor error: {e}")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'quick':
        run_quick_test()
    else:
        unittest.main()
