from template.report_template import ReportTemplate


class PDFReport(ReportTemplate):

    def get_data_from_db(self) -> None:
        print("Getting data from db PDF report")

    def apply_format(self) -> None:
        print("Applying format for PDF report")

    def save_report(self) -> None:
        print("Saving PDF report")
