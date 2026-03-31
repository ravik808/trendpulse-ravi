import pandas as pd
import matplotlib.pyplot as plt
import os


file_path = "data/trends_analysed.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("CSV file not found. Run Task 3 first.")
    exit()

if not os.path.exists("outputs"):
    os.makedirs("outputs")


top_posts = df.sort_values(by="score", ascending=False).head(10)

top_posts["short_title"] = top_posts["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure()
plt.barh(top_posts["short_title"], top_posts["score"])
plt.xlabel("Score")
plt.ylabel("Post Title")
plt.title("Top 10 Posts by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_posts.png")
plt.close()


subreddit_counts = df["subreddit"].value_counts()

plt.figure()
subreddit_counts.plot(kind="bar")
plt.xlabel("Subreddit")
plt.ylabel("Number of Posts")
plt.title("Posts per Subreddit")

plt.savefig("outputs/chart2_subreddits.png")
plt.close()


plt.figure()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()


fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].barh(top_posts["short_title"], top_posts["score"])
axs[0].set_title("Top Posts")
axs[0].invert_yaxis()

axs[1].bar(subreddit_counts.index, subreddit_counts.values)
axs[1].set_title("Posts per Subreddit")
axs[1].tick_params(axis='x', rotation=45)

axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[2].set_title("Score vs Comments")
axs[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in 'outputs/' folder")