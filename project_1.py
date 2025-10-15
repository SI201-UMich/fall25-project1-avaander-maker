# Name: Ava Anderson
# Student ID: 4721 2454 
# Email: avaander@umich.ed
# Collaborators: Ava Anderson, Luther Hoy, and generative AI (ChatGPT, DeepAI)
#
# Function Authorship:
# Kamila: avg_yield_maize_north_temp_range, percentage_maize_east_high_rainfall
# Ava: avg_yield_temp_range_west, percentage_wheat_high_yield_south
# Luther: avg_rainfall_east_high_yield, most_frequent_crop_high_yield_rain
# All: def main():, read_csv, write_results_to_txt, mock and edge cases (collaborative)

import csv
import os

def read_csv(filename):
    """
    Reads a CSV file (located in the same folder as this script)
    and returns a list of dictionaries.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    if not os.path.exists(filepath):
        print(f" File not found: {filepath}")
        return []

    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


