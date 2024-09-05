import json


def process_gmt_offset_string(gmt_offset_name):
    return gmt_offset_name[:6]


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
            processed_gmt_offset = process_gmt_offset_string(gmt_offset_name)
            if processed_gmt_offset not in processed_data:
                processed_data[processed_gmt_offset] = []

            # check if there is duplicate
            if country not in processed_data[processed_gmt_offset]:
                processed_data[processed_gmt_offset].append(country)

    # Write the processed data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(processed_data, file, indent=4, ensure_ascii=False)


# Define the input and output file paths
input_file = 'countries.json'
output_file = 'post_process_countries.json'

# Call the function to process the countries
process_countries(input_file, output_file)
