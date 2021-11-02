

class Container:
    def resolve_dependencies(self):
        """
        Реализует подстановку зависимостей в приложении.
        
        IDocumentsStorage -> GoogleDocumentsStorage
        IPdfFiller -> PdftkFiller
        """
