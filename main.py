# main.py
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.ai_service import generate_task_description
import markdown2

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    motivo: str = Form(...),
    bases: str = Form(...),
    prompt: str = Form(...),
    modelo: str = Form("gemini-2.0-flash"),
    temperatura: float = Form(0.7),
    k: int = Form(512)
):
    description = await generate_task_description(
        motivo, bases, prompt, modelo, temperatura, k
    )

    # Convertir texto a HTML con Markdown renderizado
    markdown_html = markdown2.markdown(description, extras=["fenced-code-blocks", "tables"])

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "motivo": motivo,
            "bases": bases,
            "prompt": prompt,
            "description": markdown_html
        }
    )
