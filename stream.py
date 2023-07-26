from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import sys
import time

app = FastAPI()

def generate_text():
    for i in range(10):
        sys.stdout.write(f"Text {i} ") 
        sys.stdout.flush()
        yield f"Text {i} "
        time.sleep(1)


@app.get("/")
async def streamapp():
    generated_text = generate_text()
    return StreamingResponse(content=generated_text, media_type="text/plain")

# uvicorn stream:app --reload