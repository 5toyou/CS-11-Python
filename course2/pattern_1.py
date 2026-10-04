from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Report(Document):
    def render(self) -> str:
        return "Рендер звіту (Report)"

class Invoice(Document):
    def render(self) -> str:
        return "Рендер рахунку (Invoice)"

class Contract(Document):
    def render(self) -> str:
        return "Рендер контракту (Contract)"

class NullDocument(Document):
    def render(self) -> str:
        return "Помилка: Невідомий тип документа"

class DocumentFactory:
    @staticmethod
    def create(doc_type: str) -> Document:
        # instead of if/elif
        doc_classes = {
            'report': Report,
            'invoice': Invoice,
            'contract': Contract
        }
        
        document_class = doc_classes.get(doc_type, NullDocument)
        return document_class()


input_type = 'invoice'
my_document = DocumentFactory.create(input_type)

print(my_document.render())