from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

# Allow CORS so Streamlit can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class ChatRequest(BaseModel):
    user_message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.user_message

    # Build the command
    augmented_prompt = user_message  # Or modify if needed
    try:
        command = f'ollama run mistral "{augmented_prompt}"'
        print(f">> Running command: {command}", flush=True)
        print(">> About to call subprocess...", flush=True)

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8',
            shell=True,
            timeout=120,  # 4-minute timeout
            check=True
        )
        print(">> Subprocess completed", flush=True)

        cleaned_stdout = result.stdout.strip()
        cleaned_stderr = result.stderr.strip()
        print(">> Cleaned STDOUT:", cleaned_stdout, flush=True)
        print(">> Cleaned STDERR:", cleaned_stderr, flush=True)

        response = cleaned_stdout

    except subprocess.TimeoutExpired:
        response = "⚠️ The LLM took too long to respond (timeout)."
        print(">> Subprocess timed out.", flush=True)

    except subprocess.CalledProcessError as e:
        response = f"⚠️ Ollama CLI failed with error:\n{e.stderr.strip()}"
        print(">> Ollama CLI failed with error:", e.stderr.strip(), flush=True)

    except Exception as e:
        response = f"⚠️ An error occurred: {str(e)}"
        print(">> Exception:", e, flush=True)

    print(">> Returning response to Streamlit.", flush=True)
    return {"response": response}
