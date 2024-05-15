from template.report_template import ReportTemplate


class HTMLReport(ReportTemplate):

    def get_data_from_db(self) -> None:
        print("Getting data from db HTML report")

    def perform_calculations(self) -> None:
        print("Perform calculations HTML report")

    def filter_calculations(self) -> None:
        print("Filtering calculations HTML report")

    def apply_format(self) -> None:
        print("Applying format for HTML report")

    def save_report(self) -> None:
        print("Saving HTML report")
