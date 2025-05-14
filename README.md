# Camplight-RewriteForge-Service

services
 external
   adapters 
    openai.py   
 internal
   core_service.py
 entrypoint.py


## Project layout
| Path/File | Description |
|------|-------------|
| **`entrypoint.py`** | Main entry file to initialize the app. |


## Development Environment

Access the project directory with your terminal/console and follow the instructions:

1. Create a virtual environment
   
   python -m venv .venv
   Command Prompt: .venv\Scripts\activate
   PowerShell: .\venv\Scripts\Activate.ps1
   Linux/macos: source venv/bin/activate
   
3. Install python dependencies
   
   pip install --upgrade pip
   pip install -r requirements.txt

4. Start the app using uvicorn

   uvicorn src.entrypoint:app --reload
