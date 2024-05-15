from template.report_template import ReportTemplate


class ExcelReport(ReportTemplate):

    def get_data_from_db(self) -> None:
        print("Getting data from db Excel report")

    def perform_calculations(self) -> None:
        print("Perform calculations Excel report")

    def apply_format(self) -> None:
        print("Applying format for Excel report")

    def save_report(self) -> None:
        print("Saving Excel report")
