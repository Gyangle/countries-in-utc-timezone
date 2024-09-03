import json
import re

def normalize_gmt_offset(gmt_offset_name):
    """Normalize GMT offset names by converting to UTC+X or UTC-X format."""
    match = re.match(r'UTC([+-])(\d{2}):\d{2}', gmt_offset_name)
    if match:
        sign = match.group(1)
        hours = int(match.group(2))
        return f"UTC{sign}{hours}"
    return gmt_offset_name

def process_countries(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        countries = json.load(file)

    # Dictionary to hold the processed data
    processed_data = {}

    # Process each country and group by normalized gmtOffsetName
    for country in countries:
        for timezone in country.get('timezones', []):
            gmt_offset_name = timezone.get('gmtOffsetName')
            normalized_gmt_offset = normalize_gmt_offset(gmt_offset_name)
            if normalized_gmt_offset not in processed_data:
                processed_data[normalized_gmt_offset] = []
            processed_data[normalized_gmt_offset].append(country)

    # Write the processed data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(processed_data, file, indent=4, ensure_ascii=False)

# Define the input and output file paths
input_file = 'countries.json'
output_file = 'post_process_countries.json'

# Call the function to process the countries
process_countries(input_file, output_file)
