#!/bin/python3

import argparse
import logging
import sys
import csv
from ics import Calendar, Event
from datetime import datetime


def get_logger() -> logging.Logger:
    """Configures and returns a logger object."""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO,
    )
    return logging.getLogger("CSV2ICS")


def get_parameters():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Convert a CSV file to an iCalendar file.")
    parser.add_argument("-c", "--csv", help="Path to CSV file", required=True)
    parser.add_argument("-o", "--output", help="Output iCalendar file name", default="paydays.ics")

    # Print help menu if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def read_csv(file_path: str) -> list:
    """Reads a CSV file and returns a list of dictionaries."""
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:  # Ensure there are exactly two columns
                    data.append({"date": row[0], "person": row[1]})
                else:
                    logger.warning(f"Skipping malformed row: {row}")
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        raise
    return data


def format_date(data: list) -> list:
    """Converts the date strings in the list of dictionaries to datetime objects."""
    formatted_data = []
    for row in data:
        try:
            row["date"] = datetime.strptime(row["date"], "%m/%d/%Y").strftime("%Y-%m-%d")
            formatted_data.append(row)
        except ValueError as e:
            logger.warning(f"Skipping invalid date format in row: {row} - {e}")
    return formatted_data


def convert_to_ics(data: list, output_file: str):
    """Converts the list of dictionaries to an iCalendar file."""
    calendar = Calendar()
    for row in data:
        event = Event()
        event.name = f"Payday - {row['person']} ({row['date']})"
        event.begin = row["date"]
        event.make_all_day()
        calendar.events.add(event)
        logger.info(f"Added event: \"{event.name}\"")

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(calendar.serialize_iter())
        logger.info(f"iCalendar file written to {output_file}")
    except Exception as e:
        logger.error(f"Error writing iCalendar file: {e}")
        raise


def main():
    args = get_parameters()

    csv_path = args.csv
    output_file = args.output

    logger.info(f"Reading CSV file: {csv_path}")
    csv_data = read_csv(csv_path)

    logger.info("Formatting dates")
    formatted_data = format_date(csv_data)

    logger.info("Converting to iCalendar")
    convert_to_ics(formatted_data, output_file)


if __name__ == "__main__":
    logger = get_logger()
    main()
