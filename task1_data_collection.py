import requests
import time
import json
import os
from datetime import datetime

# List of subreddits to fetch data from
subreddits = ["technology", "worldnews", "sports", "science", "entertainment"]

# Reddit API base URL
BASE_URL = "https://www.reddit.com/r/{}/hot.json?limit=25"

# Header to avoid being blocked by Reddit
headers = {
    "User-Agent": "TrendPulse/1.0"
}

# Store all collected posts
all_posts = []

# Loop through each subreddit
for subreddit in subreddits:
    url = BASE_URL.format(subreddit)
    print(f"Fetching data from r/{subreddit}...")

    try:
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to fetch r/{subreddit} (Status Code: {response.status_code})")
            continue

        data = response.json()

        # Navigate through nested JSON: data → children → each post → data
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            post_data = post.get("data", {})

            extracted = {
                "post_id": post_data.get("id"),
                "title": post_data.get("title"),
                "subreddit": post_data.get("subreddit"),
                "score": post_data.get("score"),
                "num_comments": post_data.get("num_comments"),
                "author": post_data.get("author"),
                # Add current timestamp
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            all_posts.append(extracted)

    except Exception as e:
        # Handle any unexpected errors without crashing
        print(f"Error fetching r/{subreddit}: {e}")

    # Wait 2 seconds between API calls
    time.sleep(2)

# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Create filename with current date
date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"

# Save data to JSON file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(all_posts, f, indent=4)

# Print final output
print(f"Collected {len(all_posts)} posts. Saved to {file_path}")