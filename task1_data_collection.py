import requests
import time
import json
import os
from datetime import datetime


subreddits = ["technology", "worldnews", "sports", "science", "entertainment"]


BASE_URL = "https://www.reddit.com/r/{}/hot.json?limit=25"


headers = {
    "User-Agent": "TrendPulse/1.0"
}

all_posts = []


for subreddit in subreddits:
    url = BASE_URL.format(subreddit)
    print(f"Fetching data from r/{subreddit}...")

    try:
        response = requests.get(url, headers=headers)

       
        if response.status_code != 200:
            print(f"Failed to fetch r/{subreddit} (Status Code: {response.status_code})")
            continue

        data = response.json()

        
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
               
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            all_posts.append(extracted)

    except Exception as e:
       
        print(f"Error fetching r/{subreddit}: {e}")

    
    time.sleep(2)


if not os.path.exists("data"):
    os.makedirs("data")


date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"


with open(file_path, "w", encoding="utf-8") as f:
    json.dump(all_posts, f, indent=4)


print(f"Collected {len(all_posts)} posts. Saved to {file_path}")