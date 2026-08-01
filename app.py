from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse

app = FastAPI(title="Kunwa Business Consulting Services Ltd")

@app.get("/")
def read_index():
    return FileResponse("index.html")

@app.post("/submit")
def handle_submit(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    return RedirectResponse(url="/?success=true", status_code=303)

@app.post("/submit-review")
def handle_review(name: str = Form(...), comment: str = Form(...)):
    return RedirectResponse(url="/?review_success=true", status_code=303)

app.mount("/static", StaticFiles(directory="."), name="static")
app.mount("/", StaticFiles(directory="."), name="root")
