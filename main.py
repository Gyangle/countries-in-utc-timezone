import json

# global veriable
input_file = 'countries.json'
output_file = 'post_process_countries.json'


def read_json_file(file_path):
    print(f"Reading file from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def process_gmt_offset_string(gmt_offset_name):
    return gmt_offset_name[:6]


def process_countries(countries):

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
    return processed_data


# Write the processed data to the output JSON file
def write_json_file(data, file_path):
    print(f"Writing file to {file_path}")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    countries = read_json_file(input_file)
    processed_data = process_countries(countries)
    write_json_file(processed_data, output_file)


if __name__ == "__main__":
    main()
