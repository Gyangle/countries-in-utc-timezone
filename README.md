# Country Timezone Processor

This Python script processes a JSON file containing country data and groups countries by their GMT offset names in a normalized format. It reads from an input file, normalizes the GMT offset names, and writes the processed data to an output file.

## Features

- **Normalization of GMT Offsets**: Converts GMT offset names from formats like `UTC+05:30` to `UTC+5`. Could modify base on usage. 
- **Grouping by GMT Offset**: Organizes countries by their normalized GMT offsets.

## Usage

### Prerequisites

- Python 3.x
- JSON input file with country data (`countries.json`)

### Script Functions

1. **`normalize_gmt_offset(gmt_offset_name)`**: Normalizes GMT offset names to `UTC+X` or `UTC-X` format.

2. **`process_countries(input_file, output_file)`**: Reads the input JSON file, processes the country data, and writes the grouped results to the output JSON file.

### Input File

- **`countries.json`**: This file should contain an array of country objects with the following structure:

  ```json
  [
    {
      "name": "Country Name",
      "timezones": [
        {
          "gmtOffsetName": "UTC+05:30"
        }
      ]
    }
  ]
  ```

### Output File

- **`post_process_countries.json`**: The script will write the processed data to this file, grouping countries by their normalized GMT offset.

### Example

To use the script, simply place your `countries.json` file in the same directory as the script and run it. The script will process the data and output the result to `post_process_countries.json`.

```bash
python main.py
```

## In the end

Feel free to adjust any details to better fit your project or preferences!