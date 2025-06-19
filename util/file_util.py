import os
import csv

class FileUtil:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def read_file(filename):
        result = None

        with open(filename, 'r') as file:
            result = file.read()

        return result

    @staticmethod
    def read_csv(file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            result = [row for row in reader]
        return result

    @staticmethod
    def read_csv_line(file_path, attribute_name, attribute):
        result = None
        all_lines = FileUtil.read_csv(file_path)
        if all_lines:
            for line in all_lines:
                if line.get(attribute_name) == attribute:
                    result = line
                    break
        return result

    @staticmethod
    def write_csv(file_path, data):
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            return 1
        except Exception as e:
            print(f"An error occurred while writing to the CSV file: {e}")
            raise e
