from template.report_template import ReportTemplate
from template.pdf_report import PDFReport
from template.excel_report import ExcelReport
from template.html_report import HTMLReport


def client_code(report_generator: ReportTemplate) -> None:
    print(f"Generating {report_generator.__class__.__name__} report:\n")
    report_generator.generate_report()
    print("")


if __name__ == "__main__":
    client_code(PDFReport())
    client_code(ExcelReport())
    client_code(HTMLReport())
