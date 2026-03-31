import pandas as pd
import matplotlib.pyplot as plt
import os

files = os.listdir("data")
csv_files = [f for f in files if f.startswith("cleaned_trends") and f.endswith(".csv")]

if not csv_files:
    print("No cleaned CSV file found. Run Task 2 first.")
    exit()

file_path = os.path.join("data", csv_files[0])

df = pd.read_csv(file_path)

if not os.path.exists("plots"):
    os.makedirs("plots")

posts_count = df["subreddit"].value_counts()

plt.figure()
posts_count.plot(kind="bar")
plt.title("Number of Posts per Subreddit")
plt.xlabel("Subreddit")
plt.ylabel("Number of Posts")
plt.xticks(rotation=45)

plt.savefig("plots/posts_per_subreddit.png")
plt.close()

avg_score = df.groupby("subreddit")["score"].mean()

plt.figure()
avg_score.plot(kind="bar")
plt.title("Average Score per Subreddit")
plt.xlabel("Subreddit")
plt.ylabel("Average Score")
plt.xticks(rotation=45)

plt.savefig("plots/avg_score_per_subreddit.png")
plt.close()

plt.figure()
df["score"].plot(kind="hist", bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.savefig("plots/score_distribution.png")
plt.close()

print("Visualizations saved in 'plots/' folder")