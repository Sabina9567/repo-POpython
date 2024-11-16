import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    try:
        with open(INPUT_FILENAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    except FileNotFoundError:
        print(f"Error: File '{INPUT_FILENAME}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    task()
    try:
        with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
            for line in output_f:
                print(line, end="")
    except FileNotFoundError:
        print(f"Error: File '{OUTPUT_FILENAME}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the output file: {e}")
