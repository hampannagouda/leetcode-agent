import subprocess
import tempfile
import os
from logger_config import setup_logger

logger = setup_logger(__name__)

class CodeExecutor:
    """Executes and validates Python solutions."""
    
    @staticmethod
    def validate_syntax(code):
        """Check if code has valid Python syntax."""
        try:
            compile(code, '<string>', 'exec')
            logger.info("✅ Code syntax is valid")
            return True
        except SyntaxError as e:
            logger.error(f"❌ Syntax Error: {e}")
            return False
    
    @staticmethod
    def execute_with_test_cases(code, test_cases):
        """Execute code with test cases."""
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            results = []
            
            for i, (inputs, expected) in enumerate(test_cases):
                try:
                    # Create test script
                    test_script = f"""
import sys
sys.path.insert(0, '{os.path.dirname(temp_file)}')

{code}

# Run test
result = Solution().solve({inputs})
print(result)
"""
                    
                    result = subprocess.run(
                        ['python', '-c', test_script],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    
                    output = result.stdout.strip()
                    passed = str(output) == str(expected)
                    
                    results.append({
                        'test_case': i + 1,
                        'input': inputs,
                        'expected': expected,
                        'output': output,
                        'passed': passed
                    })
                    
                    status = "✅ PASS" if passed else "❌ FAIL"
                    logger.info(f"Test {i+1}: {status}")
                    
                except subprocess.TimeoutExpired:
                    logger.warning(f"Test {i+1}: ⏱️ TIMEOUT")
                    results.append({
                        'test_case': i + 1,
                        'passed': False,
                        'error': 'Timeout'
                    })
                except Exception as e:
                    logger.error(f"Test {i+1}: Error - {e}")
                    results.append({
                        'test_case': i + 1,
                        'passed': False,
                        'error': str(e)
                    })
            
            # Cleanup
            os.unlink(temp_file)
            
            return results
            
        except Exception as e:
            logger.error(f"Error executing tests: {e}")
            return []
    
    @staticmethod
    def run_simple_check(code):
        """Run a simple check to ensure code executes without errors."""
        try:
            exec(code, {})
            logger.info("✅ Code executes without errors")
            return True
        except Exception as e:
            logger.error(f"❌ Execution Error: {e}")
            return False
