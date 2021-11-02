from abc import ABC, abstractmethod


class IDocumentsStorage(ABC):
    
    @abstractmethod
    def download_contract_template(self) -> str:
        """
        Скачивает шаблон договора из хранилища документов
        
        Возвращает путь до файла во временной директории
        """
