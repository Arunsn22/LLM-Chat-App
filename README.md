# LLM-Chat-App-
#Run the commands:

Install Python.<br>
Install Ollama.<br>
Run the following commands to get everything set up and test the scripts:-<br>
&nbsp;&nbsp;ollama run mistral.<br><br>

python -m venv venv<br>
venv\Scripts\activate &nbsp;&nbsp;# On Windows<br>
pip install fastapi uvicorn streamlit requests<br><br>

Get the following scripts ready:<br>
├── app.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# FastAPI backend<br>
├── streamlit_app.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Streamlit frontend<br><br>

Run Ollama in a terminal: ollama serve<br><br>

Run FastAPI backend:<br>
cd path\to\LLM_Project<br>
python -m uvicorn app:app --reload<br><br>

Run Streamlit frontend:<br>
cd path\to\LLM_Project<br>
streamlit run streamlit_app.py<br><br>

App opens at: [http://localhost:8501](http://localhost:8501)
