from core.documents_storage import IDocumentsStorage


class GoogleDocumentsStorage(IDocumentsStorage):
    """
    Реализация хранилища документов на Google Docs
    """
    
    def download_contract_template(self) -> str: ...
