import requests

url = "https://leetcode.com/graphql"

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
    url,
    json={"query": query}
)

print(response.json())