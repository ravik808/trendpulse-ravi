import json
import csv
import os
from datetime import datetime


date_str = datetime.now().strftime("%Y%m%d")
input_file = f"data/trends_{date_str}.json"
output_file = f"data/cleaned_trends_{date_str}.csv"

cleaned_data = []


try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Input JSON file not found. Run Task 1 first.")
    exit()


for post in data:
    post_id = post.get("post_id")
    title = post.get("title")
    subreddit = post.get("subreddit")
    score = post.get("score")
    num_comments = post.get("num_comments")
    author = post.get("author")
    collected_at = post.get("collected_at")

    
    if not post_id or not title:
        continue

   
    title = title.strip().replace("\n", " ")

    
    if not author:
        author = "unknown"

   
    try:
        score = int(score)
    except:
        score = 0

    try:
        num_comments = int(num_comments)
    except:
        num_comments = 0

    cleaned_data.append({
        "post_id": post_id,
        "title": title,
        "subreddit": subreddit,
        "score": score,
        "num_comments": num_comments,
        "author": author,
        "collected_at": collected_at
    })


if not os.path.exists("data"):
    os.makedirs("data")


with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=cleaned_data[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_data)

print(f"Cleaned data saved to {output_file}")
print(f"Total cleaned records: {len(cleaned_data)}")