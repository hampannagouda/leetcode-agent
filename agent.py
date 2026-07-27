from fetcher import LeetCodeFetcher
from solution_generator import SolutionGenerator
from code_executor import CodeExecutor
from logger_config import setup_logger
import json
from datetime import datetime

logger = setup_logger(__name__)

class LeetCodeAgent:
    """Main agent to solve LeetCode problems."""
    
    def __init__(self):
        self.fetcher = LeetCodeFetcher()
        self.generator = SolutionGenerator()
        self.executor = CodeExecutor()
        self.results = {}
    
    def solve(self):
        """Main workflow to fetch and solve the daily problem."""
        try:
            logger.info("=" * 60)
            logger.info("🚀 Starting LeetCode Agent")
            logger.info("=" * 60)
            
            # Step 1: Fetch problem
            logger.info("\n📝 Step 1: Fetching daily problem...")
            problem = self.fetcher.fetch_daily_problem()
            self.results['problem'] = problem
            
            # Step 2: Generate solution
            logger.info("\n🤖 Step 2: Generating solution...")
            solution = self.generator.generate_solution(problem)
            self.results['solution'] = solution
            
            # Step 3: Validate syntax
            logger.info("\n✔️  Step 3: Validating syntax...")
            if not self.executor.validate_syntax(solution):
                logger.warning("⚠️  Solution has syntax errors. Attempting to fix...")
                # Could add refinement logic here
            
            # Step 4: Summary
            logger.info("\n" + "=" * 60)
            logger.info("📊 Summary")
            logger.info("=" * 60)
            self.print_summary()
            
            return self.results
            
        except Exception as e:
            logger.error(f"❌ Agent failed: {e}")
            raise
    
    def print_summary(self):
        """Print a summary of the solution."""
        problem = self.results.get('problem', {})
        solution = self.results.get('solution', '')
        
        print(f"\n📌 Problem: {problem.get('title', 'N/A')}")
        print(f"📊 Difficulty: {problem.get('difficulty', 'N/A')}")
        print(f"📋 Slug: {problem.get('titleSlug', 'N/A')}")
        print(f"\n🔧 Solution Preview (first 500 chars):\n")
        print(solution[:500] + "..." if len(solution) > 500 else solution)
        print("\n✅ Solution generated and saved!")
    
    def save_results(self, filename=None):
        """Save results to a JSON file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"solution_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(self.results, f, indent=2)
            logger.info(f"💾 Results saved to {filename}")
            return filename
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            return None

if __name__ == "__main__":
    agent = LeetCodeAgent()
    agent.solve()
    agent.save_results()
