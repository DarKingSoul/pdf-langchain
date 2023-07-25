from typing import Union

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/process")
async def read_root(file: UploadFile = File(...)):
    with open('base.pdf', 'wb') as f:
        f.write(file.file.read())
    await file.close()
    response = process_doc(question='Quienes son los autores del pdf?')
    return {'response': file.filename, 'inference': response}
