import os

from model.summary import Summary
from util.file_util import FileUtil


class SummaryDao:
    def __init__(self):
        self.file_path = os.path.join(FileUtil.PROJECT_ROOT, 'resources', 'Summarys.csv')

    def get_all_summarys(self):
        result = []

        """
        Reads the summary data from the CSV file and returns it as a list of dictionaries.
        Each dictionary represents a row in the CSV file.
        """
        rows = FileUtil.read_csv(self.file_path)
        if rows:
            for row in rows:
                summary = self._dict_to_summary(row)
                result.append(summary)

        return result


    def get_summary_by_student_name(self, student_name):
        """
        Reads the summary data from the CSV file and returns a summary for a specific student.
        """
        row = FileUtil.read_csv_line(self.file_path, 'STUDENT_NAME', student_name)
        if row:
            return self._dict_to_summary(row)
        return None

    def save_summary(self, summary):
        """
        Saves a summary object to the CSV file.
        If the summary already exists, it updates the existing entry.
        """
        rows = FileUtil.read_csv(self.file_path)
        updated = False

        for i, row in enumerate(rows):
            if row['ID'] == summary['id']:
                rows[i] = summary
                updated = True
                break

        if not updated:
            rows.append(summary)

        return FileUtil.write_csv(self.file_path, rows)


    def delete_summary(self, summary_id):
        """
        Deletes a summary from the CSV file by its ID.
        """
        rows = FileUtil.read_csv(self.file_path)
        updated_rows = [row for row in rows if row['ID'] != summary_id]

        if len(updated_rows) < len(rows):
            return FileUtil.write_csv(self.file_path, updated_rows)
        return 0



    def _dict_to_summary(self, row):
        """
        Converts a dictionary row from the CSV file into a summary object.
        """
        return Summary (
            id = row['ID'],
            student = row['STUDENT_NAME'],
            status = row['STATUS'],
            made_a_difference = row['MADE_A_DIFFERENCE'],
            covered_value = row['COVERED_VALUE'],
            recommendation = row['RECOMMENDATION'],
            gender = row['GENDER']
        )

    def _summary_to_dict(self, summary):
        """
        Converts a summary object into a dictionary.
        """
        return {
            'ID': summary.id,
            'STUDENT_NAME': summary.student,
            'STATUS': summary.status,
            'MADE_A_DIFFERENCE': summary.made_a_difference,
            'COVERED_VALUE': summary.covered_value,
            'RECOMMENDATION': summary.recommendation,
            'GENDER': summary.gender
        }
