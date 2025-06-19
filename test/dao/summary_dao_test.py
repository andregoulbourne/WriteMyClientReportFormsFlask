import unittest

from dao.summary_dao import SummaryDao
from model.summary import Summary


class TestSummaryDao(unittest.TestCase):
    def setUp(self):
        self.summary_dao = SummaryDao()

    def test_get_all_summarys(self):
        summaries = self.summary_dao.get_all_summarys()
        self.assertIsNotNone(summaries)
        self.assertGreater(len(summaries), 0)
        self.assertEqual('Sally', summaries[0].student)

    def test_get_summary_by_student_name(self):
        summary = self.summary_dao.get_summary_by_student_name('Sally')
        self.assertIsNotNone(summary)
        self.assertEqual('Sally', summary.student)

    def test_save_summary(self):
        new_summary = Summary(
            id = '999',
            student = 'Test Student',
            status = '2',
            made_a_difference = '1',
            covered_value= '',
            recommendation= '',
            gender= 'F'
        )
        result = self.summary_dao.save_summary(new_summary)
        self.assertGreater(result, 0)

        # Verify the summary was saved
        saved_summary = self.summary_dao.get_summary_by_student_name('Test Student')
        self.assertIsNotNone(saved_summary)
        self.assertEqual('Test Student', saved_summary.student)
        # Clean up
        self.summary_dao.delete_summary(new_summary.id)

    def test_delete_summary(self):
        new_summary = Summary(
            id='999',
            student='Test Student',
            status='2',
            made_a_difference='1',
            covered_value='',
            recommendation='',
            gender='F'
        )
        self.summary_dao.save_summary(new_summary)
        result = self.summary_dao.delete_summary(new_summary.id)
        self.assertGreater(result, 0)

if __name__ == "__main__":
    unittest.main()