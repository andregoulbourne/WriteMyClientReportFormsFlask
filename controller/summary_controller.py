from service.summary_service import SummaryService, WriterCommentService

class SummaryController:
    def __init__(self):
        self.summary_service = SummaryService()
        self.write_comment_service = WriterCommentService()

    def get_all_summarys(self):
        summaries = self.summary_service.get_all_summarys()
        return [s.to_dict() for s in summaries]

    def get_summary_by_student_name(self, student_name):
        summary = self.summary_service.get_summary_by_student_name(student_name)
        return summary.to_dict() if summary else None

    def save_summary(self, summary_data):
        result = self.summary_service.save_summary(summary_data)
        return result

    def delete_summary(self, summary_id):
        result = self.summary_service.delete_summary(summary_id)
        return result

    def writer_comment(self, summarys):
        result = self.write_comment_service.write_comment(summarys)
        return result