import os
from src.extract_reddit import extract_reddit_data
from src.extract_kaggle import extract_kaggle_ev_data
from src.extract_trends import extract_google_trends


def save_processed_data(df, base_filename):
    """Helper to save data in both CSV and JSON formats as required."""
    processed_path = "src/data/processed"
    os.makedirs(processed_path, exist_ok=True)

    # Save CSV
    df.to_csv(os.path.join(processed_path, f"{base_filename}.csv"), index=False)
    # Save JSON
    df.to_json(os.path.join(processed_path, f"{base_filename}.json"), orient="records", indent=4)
    print(f"Stored {base_filename} in CSV and JSON formats.")


def main():
    print("--- Starting Modern ELT Pipeline: Smart Mobility ---")

    # 1. Extract from Reddit (API)
    print("\n[1/3] Extracting Reddit Data...")
    reddit_df = extract_reddit_data(query="Electric Vehicle sales", limit=50)
    save_processed_data(reddit_df, "reddit_ev_processed")

    # 2. Extract from Kaggle (Public Dataset)
    print("\n[2/3] Extracting Kaggle Data...")
    kaggle_df = extract_kaggle_ev_data()
    save_processed_data(kaggle_df, "kaggle_ev_processed")

    # 3. Extract from Google Trends
    print("\n[3/3] Extracting Google Trends Data...")
    trends_df = extract_google_trends()
    if trends_df is not None:
        # CRITICAL FIX: Ensure date is a column, not an index
        if 'date' not in trends_df.columns:
            trends_df = trends_df.reset_index()
        save_processed_data(trends_df, "trends_ev_processed")

    print("\n--- Pipeline Execution Complete ---")
    print("Check 'data/raw/' and 'data/processed/' for outputs.")


if __name__ == "__main__":
    main()
