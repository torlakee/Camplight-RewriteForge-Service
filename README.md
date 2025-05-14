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

5. Start the app using uvicorn

   uvicorn src.entrypoint:app --reload



## Overview of the work (in details)

1. Created pyproject.toml
2. Created requirements.txt file
3. ...
4. Created file configurations.py, containing function to load the config and sensitive data
5. Created separated directory for version v1, in case of future versions
6. ..
7. Created local .env file, containing environment variables (exposed ports, used redis uri, etc. )
8. Created sample .secrets file, containing sample keys for the available LLM adapters (sensitive data)
9. ---
10. Created unit tests
11. Created integrated tests
12. ---
13. Set up lint tools
14. --
15. Added docstrings to each python script following Google Style
16. Created Dockerfile
17. Created docker-compose file
18. --
19. Created README.md (as requested in...), containing instructions how to set up dev environment, set up production environment
20. Created technical documentation
