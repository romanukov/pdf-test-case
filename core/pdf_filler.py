from abc import ABC, abstractmethod


class IPdfFiller(ABC):
    
    @abstractmethod
    def fill_pdf(self, pdf_path: str, data: dict):
        """
        Заполняет данными из data pdf-файл, лежащий в pdf_path
        """
