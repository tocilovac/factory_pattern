from abc import ABC, abstractmethod

class DocumentReader(ABC):
    """
    Abstract product for reading documents.
    Each concrete reader must implement extract_content()
    and return content in structured form (list preserving order).
    """

    @abstractmethod
    def extract_content(self) -> list:
        pass


class PDFReader(DocumentReader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_content(self) -> list:
        # placeholder logic — real extraction in later steps
        return [
            {"type": "text", "content": "PDF text example"},
            {"type": "table", "content": [["A", "B"], [1, 2]]},
            {"type": "text", "content": "More text inside PDF"}
        ]


class WordReader(DocumentReader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_content(self) -> list:
        return [
            {"type": "text", "content": "Word document intro"},
            {"type": "text", "content": "Paragraph content"}
        ]


class ExcelReader(DocumentReader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_content(self) -> list:
        return [
            {"type": "table", "content": [["Name", "Age"], ["Arian", 23]]}
        ]
class HTMLReader:
    def read(self, file_path: str) -> str:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return f"[HTML Content Extracted]\n{content}"
        except Exception as e:
            return f"Error reading HTML: {e}"


class JSONReader:
    def read(self, file_path: str) -> str:
        import json
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return f"[JSON Content Extracted]\n{data}"
        except Exception as e:
            return f"Error reading JSON: {e}"

