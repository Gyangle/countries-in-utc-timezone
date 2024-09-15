import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

# Global variable
input_file = 'countries.json'
output_file = 'post_process_countries.json'


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Read JSON file and return its content."""
    logging.info(f"Reading file from {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return []


def process_gmt_offset_string(gmt_offset_name: str) -> str:
    """Process GMT offset string to a normalized format."""
    return gmt_offset_name[:6]


def process_countries(countries: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Process countries and group by normalized GMT offset name."""
    processed_data = {}

    for country in countries:
        for timezone in country.get('timezones', []):
            gmt_offset_name = timezone.get('gmtOffsetName')
            processed_gmt_offset = process_gmt_offset_string(gmt_offset_name)
            if processed_gmt_offset not in processed_data:
                processed_data[processed_gmt_offset] = []

            # Use a set to avoid duplicates
            if country not in processed_data[processed_gmt_offset]:
                processed_data[processed_gmt_offset].append(country)
    return processed_data


def write_json_file(data: Dict[str, Any], file_path: str) -> None:
    """Write data to a JSON file."""
    logging.info(f"Writing file to {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except IOError as e:
        logging.error(f"Error writing file {file_path}: {e}")


def main() -> None:
    """Main function to read, process, and write JSON data."""
    countries = read_json_file(input_file)
    if countries:
        processed_data = process_countries(countries)
        write_json_file(processed_data, output_file)


if __name__ == "__main__":
    main()