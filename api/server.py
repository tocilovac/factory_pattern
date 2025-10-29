from fastapi import FastAPI, UploadFile, File, HTTPException
from factory import DocumentReaderFactory
import tempfile
import os

app = FastAPI(title="Document Reader API")

@app.post("/read-file")
async def read_file(file_type: str, file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        # ✅ Create the reader with both file_type and file_path
        reader = DocumentReaderFactory.get_reader(file_type.lower(), tmp_path)
        result = reader.extract_content()
    finally:
        os.remove(tmp_path)

    return {"file_type": file_type, "content": result}
