from pytrends.request import TrendReq
import os


def extract_google_trends():
    # 1. Initialize TrendReq (hl=language, tz=timezone offset)
    # No API keys required for pytrends
    pytrends = TrendReq(hl='en-US', tz=360)

    # 2. Define keywords related to Smart Mobility
    kw_list = ["Electric Vehicles", "Tesla", "Charging Station"]

    print(f"Extracting Google Trends data for: {kw_list}...")

    try:
        # 3. Build payload for the last 5 years
        pytrends.build_payload(kw_list, timeframe='today 5-y', geo='')

        # 4. Extract interest over time (Time-Series data)
        df = pytrends.interest_over_time()

        if not df.empty:
            # Drop the 'isPartial' column often returned by Google Trends
            if 'isPartial' in df.columns:
                df = df.drop(columns=['isPartial'])

            # 5. Ensure storage directories exist
            os.makedirs("data/raw", exist_ok=True)
            os.makedirs("data/processed", exist_ok=True)

            # 6. Save Raw and Processed (CSV/JSON) formats
            df.to_csv("data/raw/trends_ev_raw.csv")
            df.to_csv("data/processed/trends_ev_processed.csv")
            df.to_json("data/processed/trends_ev_processed.json")

            print("Successfully saved Trends data to data/raw/ and data/processed/")
            return df
        else:
            print("No data found for these keywords.")

    except Exception as e:
        print(f"Error during extraction: {e}")
        # Note: Google Trends often rate-limits (Error 429)


if __name__ == "__main__":
    extract_google_trends()
