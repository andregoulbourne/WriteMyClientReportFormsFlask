from dao.summary_dao import SummaryDao

class SummaryService:
    def __init__(self):
        self.summary_dao = SummaryDao()  # Initialize with actual DAO implementation

    def get_all_summarys(self):
        return self.summary_dao.get_all_summarys()

    def get_summary_by_student_name(self, student_name):
        return self.summary_dao.get_summary_by_student_name(student_name)

    def save_summary(self, summary):
        return self.summary_dao.save_summary(summary)

    def delete_summary(self, summary_id):
        return self.summary_dao.delete_summary(summary_id)


class WriterCommentService:

    def write_comment(self, summarys):
        result = ''

        for summary in summarys:

            if summary:
                result += f"""
                        On a scale from 1-3, {summary.student} confidence level with the material was at a {summary.status} at the beginning of the session.

                        In the session we worked on finding {summary.covered_value}.

                        After the session {summary.student} said {summary.gender} was feeling more confident with the material then prior.

                        Recommendations: {summary.recommendation}.

                        """
        return result