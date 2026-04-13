# Pacific Internal Search Assistant

## Overview
This project is a lightweight internal knowledge search assistant that retrieves documents based on user queries while enforcing role-based access control.

## Features
- Keyword-based search with ranking
- Permission-aware filtering (intern, engineer, admin)
- Context aggregation into a response
- Basic agentic retry mechanism
- TTFT (Time to First Token) measurement
- Keyword highlighting and UI improvements

## Tech Stack
- FastAPI (Python backend)
- HTML, CSS, JavaScript frontend

---

## How to Run

### 1. Clone or unzip the project

### 2. Start the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
