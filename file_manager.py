import csv
import os


class FileManager:
    @staticmethod
    def read_csv(file_path):
        """Read data from a CSV file and return a list of dictionaries."""
        if not os.path.exists(file_path):
            return []

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    @staticmethod
    def write_csv(file_path, fieldnames, data):
        """Overwrite a CSV file with new data."""
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def append_csv(file_path, fieldnames, row):
        """Append a single row to a CSV file."""
        file_exists = os.path.exists(file_path)

        with open(file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists or os.path.getsize(file_path) == 0:
                writer.writeheader()

            writer.writerow(row)