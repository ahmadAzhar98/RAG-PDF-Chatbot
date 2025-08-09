# PDF Q&A with Context Highlighting

This project allows you to upload a PDF, ask questions about its content, and receive answers with context highlighting in the document.

The application has two parts:
- **Frontend** (Streamlit) – For uploading PDFs and interacting with the system
- **Backend** (FastAPI) – For processing PDFs and handling queries

---

## Features

- Upload any PDF (up to 200MB)
- Ask questions and get AI-generated answers
- Highlights relevant sections in the PDF
- Simple, clean UI
- Example **Testing Notebook** provided in the `test` directory

---

## Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Linux / MacOS:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Create a .env file (API Keys Required)

This project requires Anthropic (Claude) and Google Generative AI API keys.

You must create a `.env` file in the root of the project and add your keys.

**Steps:**

1. Sign up and get your Anthropic Claude API key from: https://console.anthropic.com/
2. Sign up and get your Google Generative AI API key from: https://makersuite.google.com/
3. Copy `.env-temp` from the repository and rename it to `.env`
4. Fill in your keys inside `.env`:
5. Place your .env exactly where .env-temp is.

```bash
# .env
ANTHROPIC_API_KEY=your_claude_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

 **Do not commit `.env` to Git** — it contains your private credentials.

---

## Running the Application

### Frontend (Streamlit)

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Backend (FastAPI)

1. Open a **new terminal** (keep frontend running separately).

2. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

3. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

---

## Testing Notebook

A testing notebook is available in the **`test`** directory for checking the processing pipeline and seeing example results without running the UI.

##  Sample UI

![Alt text](images/ui.png)

---

##  Notes
- Run **frontend** and **backend** independently in separate terminals.  
- Make sure your virtual environment is activated before running either.  
- You can customize ports in `uvicorn` and Streamlit settings if needed.
