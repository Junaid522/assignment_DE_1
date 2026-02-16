import praw
import pandas as pd
import os
from dotenv import load_dotenv

# Load credentials from .env file (Requirement: No hard-coded keys)
load_dotenv()


def extract_reddit_data(query="EV sales 2010 2024", limit=100):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="DataEngineeringProject/1.0 by /u/YourUsername"
    )

    posts = []
    # Searching the 'electricvehicles' subreddit for specific keywords
    subreddit = reddit.subreddit("electricvehicles")

    for submission in subreddit.search(query, limit=limit, sort="top"):
        posts.append({
            "id": submission.id,
            "title": submission.title,
            "score": submission.score,
            "num_comments": submission.num_comments,
            "created_utc": submission.created_utc,
            "selftext": submission.selftext,
            "url": submission.url
        })

    return pd.DataFrame(posts)


# Execute and Save to data/raw/
df = extract_reddit_data()
os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/reddit_ev_sales_raw.csv", index=False)
