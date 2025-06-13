Install Python.
Install Ollama.
Run the follwoing commands to get everything set up and test the scripts:-
  ollama run mistral.
  python -m venv venv
  venv\Scripts\activate     # On Windows
  pip install fastapi uvicorn streamlit requests
Get the following scripts ready: 
  ├── app.py             # FastAPI backend
  ├── streamlit_app.py   # Streamlit frontend
Run Ollama in a terminal: ollama serve
Run FastAPI backend: 
  cd path\to\LLM_Project
  python -m uvicorn app:app --reload
Run Streamlit frontend: 
  cd path\to\LLM_Project
  streamlit run streamlit_app.py
App opens at: http://localhost:8501



