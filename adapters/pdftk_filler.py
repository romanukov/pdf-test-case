from core.pdf_filler import IPdfFiller


class PdftkFiller(IPdfFiller):
    """
    Реализация заполнителя PDF на библиотеке PDFTK.
    """
    
    def fill_pdf(self, pdf_path: str, data: dict): ...