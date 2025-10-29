from factory import DocumentReaderFactory

def main():
    # test different file types
    file_types = ["pdf", "word", "excel", "txt", "html", "json"]  # txt should throw error

    for f in file_types:
        print(f"\n--- Creating reader for: {f.upper()} ---")
        try:
            reader = DocumentReaderFactory.get_reader(f)
            content = reader.read(f"sample_document.{f}")
            print(content)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
