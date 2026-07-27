import requests
from logger_config import setup_logger
from config import LEETCODE_API_URL

logger = setup_logger(__name__)

class LeetCodeFetcher:
    """Fetches daily LeetCode problem."""
    
    def __init__(self):
        self.api_url = LEETCODE_API_URL
    
    def fetch_daily_problem(self):
        """Fetch the daily LeetCode problem."""
        try:
            query = """
            query questionOfToday {
             activeDailyCodingChallengeQuestion {
               question {
                 title
                 titleSlug
                 difficulty
                 content
               }
             }
            }
            """
            
            response = requests.post(
                self.api_url,
                json={"query": query},
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            
            if "errors" in data:
                logger.error(f"GraphQL Error: {data['errors']}")
                raise Exception(f"GraphQL Error: {data['errors']}")
            
            problem = data.get("data", {}).get("activeDailyCodingChallengeQuestion", {}).get("question", {})
            
            if not problem:
                logger.error("No problem found")
                raise Exception("Could not fetch daily problem")
            
            logger.info(f"✅ Fetched problem: {problem['title']} ({problem['difficulty']})")
            return problem
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error fetching problem: {e}")
            raise
