from document_reader import PDFReader, ExcelReader, WordReader, DocumentReader

class DocumentReaderFactory:
    @staticmethod
    def get_reader(file_type: str, file_path: str) -> DocumentReader:
        file_type = file_type.lower()

        if file_type == "pdf":
            return PDFReader(file_path)
        elif file_type == "word":
            return WordReader(file_path)
        elif file_type == "excel":
            return ExcelReader(file_path)
        elif file_type == "html":
            from document_reader import HTMLReader
            return HTMLReader()
        elif file_type == "json":
            from document_reader import JSONReader
            return JSONReader()
        else:
            raise ValueError(f"❌ Unsupported document type: {file_type}")
