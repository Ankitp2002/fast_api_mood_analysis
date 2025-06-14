# Mood Analysis API Project

This is a **free and open-source mood analysis** API built using **FastAPI**. The goal is to analyze text (or speech in future versions) and predict the **mood or emotion** behind it using open, free-to-use models — no paid APIs or commercial tools.

---

## 🚀 Features (Planned & Ongoing)

- ✅ FastAPI backend setup
- ✅ Virtual environment setup
- ✅ Free/open-source models (HuggingFace, spaCy, etc.)
- 🧠 Mood detection from user text (anger, happiness, sadness, etc.)
- 🗃️ REST API endpoint for mood classification
- 📊 (Future) Mood stats dashboard
- 🗣️ (Future) Speech-to-text support
- 🧩 (Future) Multilingual input

---

find . -type d -name "**pycache**" -exec rm -r {} +

## 📁 Project Structure

```bash

/
├── apis/
│   ├── __init__.py
│   ├── auth/
│   │   ├── models.py
│   │   ├── schema/
│   │   │   └── __init__.py
│   │   └── views/
│   │       └── __init__.py
│   ├── base_model.py
│   ├── health/
│   │   ├── models.py
│   │   ├── schema/
│   │   │   ├── __init__.py
│   │   │   └── health_check.py
│   │   └── views/
│   │       ├── __init__.py
│   │       └── health_check.py
│   ├── reg_model.py
│   └── reg_router.py
├── configuration/
│   ├── db.py
│   ├── logger.py
│   ├── server.py
│   └── settings.py
├── main.py
├── pyvenv.cfg
├── README.md
└── requirements.txt


```
