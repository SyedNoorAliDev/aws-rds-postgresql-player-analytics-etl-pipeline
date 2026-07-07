import logging

from extract import extract
from transform import transform
from load import load

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Starting ETL...")

    delivery, player, captain = extract()

    logging.info("Extraction complete.")

    final_df = transform(delivery, player, captain)

    logging.info("Transformation complete.")

    load(final_df)

    logging.info("Loaded %d rows.", len(final_df))

    logging.info("ETL completed successfully.")

if __name__ == "__main__":
    main()