from abc import ABC, abstractmethod


class ReportTemplate(ABC):

    def generate_report(self) -> None:

        self.get_data_from_db()
        self.perform_calculations()
        self.filter_calculations()
        self.apply_format()
        self.save_report()

    @abstractmethod
    def get_data_from_db(self) -> None:
        pass

    @abstractmethod
    def apply_format(self) -> None:
        pass

    @abstractmethod
    def save_report(self) -> None:
        pass

    def perform_calculations(self) -> None:
        pass

    def filter_calculations(self) -> None:
        pass
