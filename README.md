# 🎫 TiketJira — AI-Powered Task Description Generator

**TiketJira** is a **FastAPI** application powered by **Google Gemini (Generative AI)** that automatically generates structured technical task descriptions based on a ticket’s reason and related data sources or components.

It helps development and support teams **reduce documentation time** and **maintain consistency** when creating Jira tickets or user stories (*Definition of Ready — DOR*).

---

## 🚀 Key Features

- 🧠 **Gemini Flash (2.0 / 2.5) Integration**  
  Generates concise, well-structured technical text including *Objective*, *Description*, *Deliverable*, and *DOR* sections.

- ⚙️ **Parametric Prompt Configuration**  
  Customize the base prompt, model temperature, and maximum output tokens (`k`) to control creativity and response length.

- 🌐 **Simple Web Interface**  
  Built with FastAPI and Jinja2, featuring a clean, minimal UI with Markdown rendering.

- 🔒 **Local or Cloudflared Deployment**  
  Securely expose the service through Cloudflare Tunnel or run it locally.

---

## 🧩 Project Structure
```bash
tiketjira/
├── main.py                     # FastAPI entry point
├── services/
│   └── ai_service.py           # Gemini API integration logic
├── templates/
│   └── index.html              # Web interface
├── static/
│   └── styles.css              # Basic styling
├── requirements.txt            # Project dependencies
└── tiketjira.log               # Optional log file



## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sightes/tiketjira.git
cd tiketjira
