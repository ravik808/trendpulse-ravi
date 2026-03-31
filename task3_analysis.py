import pandas as pd
from datetime import datetime


date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/cleaned_trends_{date_str}.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("CSV file not found. Run Task 2 first.")
    exit()


total_posts = len(df)


avg_score = df["score"].mean()


top_subreddit = df["subreddit"].value_counts().idxmax()


top_post = df.loc[df["score"].idxmax()]


avg_comments = df.groupby("subreddit")["num_comments"].mean()


print("\n📊 TrendPulse Analysis Report\n")

print(f"Total Posts: {total_posts}")
print(f"Average Score: {avg_score:.2f}")
print(f"Top Subreddit: {top_subreddit}")

print("\n🔥 Highest Scoring Post:")
print(f"Title: {top_post['title']}")
print(f"Subreddit: {top_post['subreddit']}")
print(f"Score: {top_post['score']}")

print("\n💬 Average Comments per Subreddit:")
print(avg_comments)

df["engagement"] = df["num_comments"] / (df["score"] + 1)

df["is_popular"] = df["score"] > df["score"].mean()

output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")