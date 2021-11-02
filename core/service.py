import os
from typing import BinaryIO

from core.documents_storage import IDocumentsStorage
from core.models import CustomerData
from core.pdf_filler import IPdfFiller


class Service:
    document_storage: IDocumentsStorage
    pdf_filler: IPdfFiller
    
    def create_contract(self, customer_data: CustomerData) -> BinaryIO:
        """
        Создает документ с договором для клиента. Возвращает объект pdf-файла.
        """
        pdf_path = self.document_storage.download_contract_template()
        self.pdf_filler.fill_pdf(pdf_path, customer_data.dict())
        with open(pdf_path, 'rb') as pdf_file:
            os.remove(pdf_path)
        return pdf_file
