# CSV to iCalendar Converter

This script converts a CSV file containing date and person information into an iCalendar (`.ics`) file. It is useful for automating the creation of calendar events from a simple CSV file.

## Features

- Reads a CSV file with `date` and `person` columns.
- Converts each row into an iCalendar event.
- Allows the user to specify the input CSV file and the output iCalendar file.
- Handles invalid or malformed rows gracefully with logging.

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `ics`
  - `argparse`

Install the required packages using `pip`:

```bash
pip install ics
```

## Usage

### Command-line Arguments

- `-c`, `--csv`: Path to the input CSV file (required).
- `-o`, `--output`: Name of the output iCalendar file (optional, defaults to `paydays.ics`).

### Example

Given a CSV file named `events.csv` with the following content:

```
1/15/2025,Timmy
1/31/2025,Malcolm
2/14/2025,Winnie
2/28/2025,Malcolm
```

Run the script as follows:

```bash
./csv2ics.py -c events.csv -o my_calendar.ics
```

This will generate an iCalendar file named `my_calendar.ics` with events for each row in the CSV file.

### Help Menu

To view the help menu, run:

```bash
./csv2ics.py -h
```

Output:

```
usage: csv2ics.py [-h] -c CSV [-o OUTPUT]

Convert a CSV file to an iCalendar file.

optional arguments:
  -h, --help            show this help message and exit
  -c CSV, --csv CSV     Path to CSV file
  -o OUTPUT, --output   Output iCalendar file name (default: paydays.ics)
```

## CSV Format

The input CSV file must have two columns:

1. **Date**: In `MM/DD/YYYY` format (e.g., `1/15/2025`).
2. **Person**: A string representing the person associated with the event.

Example:

```
1/15/2025,Franklin
1/31/2025,Melissa
```

## Logging

The script logs its operations and outputs messages to the console, including:

- Events being added to the calendar.
- Skipping malformed rows or invalid date formats.
- Errors encountered during execution.

## Output

The script generates an `.ics` file containing calendar events. Each event is named using the format:

```
Payday - {Person} ({Date})
```

For example:

- Event Name: `Payday - Franklin (2025-01-15)`
- Date: `2025-01-15`

## Error Handling

- **Malformed Rows**: Rows with missing or extra columns are skipped with a warning.
- **Invalid Date Format**: Rows with improperly formatted dates are skipped with a warning.
- **File Errors**: Any issues reading the CSV or writing the `.ics` file are logged as errors.

## Development

### Code Structure

- `get_logger`: Configures and returns a logger.
- `get_parameters`: Parses command-line arguments.
- `read_csv`: Reads the CSV file and validates its format.
- `format_date`: Converts date strings into a standard format.
- `convert_to_ics`: Converts the CSV data into an iCalendar file.

### Contributing

Feel free to submit pull requests or suggest features. Contributions are welcome!

## License

This script is licensed under the MIT License. See the LICENSE file for details.

---
