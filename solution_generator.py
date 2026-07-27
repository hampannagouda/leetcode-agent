import re
from openai import OpenAI
from logger_config import setup_logger
from config import OPENAI_API_KEY, OPENAI_MODEL, TEMPERATURE

logger = setup_logger(__name__)

class SolutionGenerator:
    """Generates Python solutions using OpenAI."""
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL
        self.temperature = TEMPERATURE
    
    def generate_solution(self, problem):
        """Generate a solution for the given problem."""
        try:
            title = problem.get("title", "Unknown Problem")
            content = problem.get("content", "")
            difficulty = problem.get("difficulty", "Unknown")
            
            logger.info(f"🤖 Generating solution for: {title}")
            
            # Create prompt
            system_prompt = """You are an expert competitive programmer. 
Generate a clean, efficient Python solution for LeetCode problems.
- Include docstring with approach explanation
- Add comments for complex logic
- Return ONLY valid Python code without markdown formatting
- Ensure the solution is optimal for the problem"""
            
            user_prompt = f"""
Problem Title: {title}
Difficulty: {difficulty}

Problem Description:
{self._clean_html(content)}

Generate a complete Python solution with:
1. Function definition matching LeetCode interface
2. Comprehensive docstring
3. Optimal algorithm approach
"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=self.temperature,
                max_tokens=2000
            )
            
            solution = response.choices[0].message.content
            logger.info(f"✅ Solution generated successfully")
            return solution
            
        except Exception as e:
            logger.error(f"Error generating solution: {e}")
            raise
    
    @staticmethod
    def _clean_html(content):
        """Remove HTML tags from problem content."""
        # Remove HTML tags
        clean = re.sub(r'<[^>]+>', '', content)
        # Decode common HTML entities
        clean = clean.replace("&nbsp;", " ")
        clean = clean.replace("&quot;", '"')
        clean = clean.replace("&amp;", "&")
        return clean.strip()
    
    def extract_code_block(self, response_text):
        """Extract Python code from response (with or without markdown)."""
        # Try to find code block with python markdown
        match = re.search(r'```python\s*(.*?)\s*```', response_text, re.DOTALL)
        if match:
            return match.group(1)
        
        # Try to find generic code block
        match = re.search(r'```\s*(.*?)\s*```', response_text, re.DOTALL)
        if match:
            return match.group(1)
        
        # If no markdown, assume the whole thing is code
        return response_text
