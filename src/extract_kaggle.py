import kagglehub
from kagglehub import KaggleDatasetAdapter
import os


def extract_kaggle_ev_data():
    # 1. Define the file to load from the dataset
    # The file name within this specific dataset is "IEA Global EV Data 2024.csv"
    file_name = "IEA Global EV Data 2024.csv"

    print(f"Downloading {file_name} from Kaggle...")

    # 2. Load the dataset directly into a Pandas DataFrame
    # Note: Ensure you have your kaggle.json token configured in ~/.kaggle/
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "patricklford/global-ev-sales-2010-2024",
        file_name,
    )

    # 3. Create the raw data directory if it doesn't exist
    raw_path = "data/raw"
    os.makedirs(raw_path, exist_ok=True)

    # 4. Save the raw file for the assignment's EL requirements
    save_path = os.path.join(raw_path, "kaggle_ev_sales_raw.csv")
    df.to_csv(save_path, index=False)

    print(f"Successfully saved raw data to {save_path}")
    print("First 5 records:\n", df.head())

    return df


if __name__ == "__main__":
    extract_kaggle_ev_data()
