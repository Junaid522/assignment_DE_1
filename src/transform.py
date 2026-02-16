import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


def clean_and_transform():
    # Load processed datasets
    kaggle_df = pd.read_csv("data/processed/kaggle_ev_processed.csv")
    trends_df = pd.read_csv("data/processed/trends_ev_processed.csv")

    # --- 1. Data Quality Assessment ---
    print("--- Data Quality Report ---")
    for name, df in [("Kaggle", kaggle_df), ("Trends", trends_df)]:
        print(f"\n{name} Dataset:")
        print(f"Missing Values:\n{df.isnull().sum()}")
        print(f"Duplicate Records: {df.duplicated().sum()}")

    # --- 2. Transformation and Cleaning ---

    # Fix Trends 'date' issue: Handle index if 'date' is not a column
    if 'date' not in trends_df.columns:
        trends_df = trends_df.reset_index()

    # Standardize Dates [cite: 112]
    trends_df['date'] = pd.to_datetime(trends_df['date'])
    kaggle_df['year'] = pd.to_datetime(kaggle_df['year'], format='%Y')

    # Handle Missing Values: Drop critical nulls in Kaggle, fill 0 in Trends [cite: 110]
    kaggle_df = kaggle_df.dropna(subset=['value'])
    trends_df = trends_df.fillna(0)

    # Remove Duplicates (Handles the 206 duplicates in Trends)
    kaggle_df = kaggle_df.drop_duplicates()
    trends_df = trends_df.drop_duplicates()

    # Generate Summary Statistics [cite: 113]
    print("\n--- Summary Statistics (Kaggle) ---")
    print(kaggle_df.describe())

    # --- 3. Save Cleaned Data to data/cleaned/  ---
    os.makedirs("data/cleaned", exist_ok=True)
    kaggle_df.to_csv("data/cleaned/kaggle_ev_cleaned.csv", index=False)
    trends_df.to_csv("data/cleaned/trends_ev_cleaned.csv", index=False)

    # --- 4. Exploratory Analysis and Visualizations [cite: 115, 128] ---
    sns.set_theme(style="whitegrid")

    # Visualization 1: Temporal Analysis (Trends over time) [cite: 120]
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=trends_df, x='date', y='Tesla', label='Tesla Search Interest')
    sns.lineplot(data=trends_df, x='date', y='Electric Vehicles', label='EV Search Interest')
    plt.title("Google Search Interest Trends (2021-2024)")
    plt.ylabel("Interest Score")
    plt.savefig("data/cleaned/temporal_trends.png")
    plt.show()

    # Visualization 2: Categorical Analysis (Sales by Region) [cite: 122]
    # Filter for total EV Sales in 2023 for specific regions
    regions = ['USA', 'China', 'Europe', 'India']
    viz_df = kaggle_df[(kaggle_df['region'].isin(regions)) &
                       (kaggle_df['parameter'] == 'EV sales') &
                       (kaggle_df['year'].dt.year == 2023)]

    plt.figure(figsize=(10, 6))
    sns.barplot(data=viz_df, x='region', y='value', hue='powertrain')
    plt.title("EV Sales by Region and Powertrain (2023)")
    plt.ylabel("Number of Vehicles")
    plt.savefig("data/cleaned/categorical_sales.png")
    plt.show()

    # Visualization 3: Relationship Analysis (Heatmap) [cite: 125]
    plt.figure(figsize=(8, 6))
    correlation = trends_df[['Electric Vehicles', 'Tesla', 'Charging Station']].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title("Correlation: Search Terms Relationship")
    plt.savefig("data/cleaned/relationship_heatmap.png")
    plt.show()

    print("\n--- Transformation Complete. Cleaned data and plots saved in data/cleaned/ ---")
    return kaggle_df, trends_df


if __name__ == "__main__":
    clean_and_transform()