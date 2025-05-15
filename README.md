# Camplight-RewriteForge-Service

## Project layout
| Path/File | Description |
|------|-------------|
| **`entrypoint.py`** | Main entry file to initialize the app. |


## Development Environment
### Run manually
Access the project directory with your terminal/console and follow the instructions:

1. Create a virtual environment
```console
    python -m venv .venv

    Command Prompt: .venv\Scripts\activate

    PowerShell: .\venv\Scripts\Activate.ps1

    Linux/macos: source venv/bin/activate
```
3. Install python dependencies
```console
    pip install --upgrade pip

    pip install -r requirements.txt
```
5. Start the app using uvicorn
```console
    uvicorn src.entrypoint:app --reload
```
### Run using Docker
```console
    docker-compose up --build
```
### Run linting tools manually
```console
    pip install bandit ruff
   
    ruff check . --fix
   
    bandit -r src -c .bandit.yaml
```
### Run linting tools using Docker
```console
    docker-compose run --rm lint
```

### Additional: Generate documentation using docstrings and Sphinx
```console
    cd docs
  
    Linux/macos: make html
    Windows: make.bat html
```
Open the generated documentation file inside docs/build/index.html

## Overview of the work (in details)
0. Created ROADMAP.md file ✔️
1. Created pyproject.toml ✔️
2. Created requirements.txt file ✔️
3. ...
4. Created file configurations.py, containing function to load the config and sensitive data
5. Created separated directory for version v1, in case of future versions ✔️
6. Created base class LLMAdapter ✔️
7. Created class OpenAIAdapter extending base class LLMAdapter ✔️
8. Created class GeminiAdapter extending base class LLMAdapter ✔️
9. Created local .env file, containing environment variables (exposed ports, used redis uri, etc. ) ✔️
10. Created sample .secrets file, containing sample keys for the available LLM adapters (sensitive data) ✔️
11. Created function which provides LLM adapter inside the routers - provide_llm ✔️
12. Created unit tests
13. Created integrated tests // sample request, expected results
14. ---
15. Set up lint tools ✔️
16. --
17. Added docstrings to each python script following Google Style
18. Created Dockerfile ✔️
19. Created docker-compose file ✔️
20. --
21. Created README.md (as requested in...), containing instructions how to set up dev environment, set up production environment ✔️
22. Created technical documentation
23. Add possible future improvements
24. Add possible security measures besides checking with zap, bandit, truffledog, trivy

### Possible improvements
* We can create additiona input validation for scripts, sql injections or suspicious wording in the text passed from the client
* We can use third-party tool for queueing the job
* Regarding health check we can add:
    * Ping to redis
    * Retry on time out or connection retrier
    * Set up a redist cluster
    * Add Liveness, Readiness and Startup probes to k8s (deployment.yaml)
    * We can expose Swagger UI and OpenAPI json
* We can put all error message strings into a separate file (for future l10n and i18n)
* We can add option for adding custom styles to the already set ones - pirate, haiku, formal, ...
* We can set up a logger instead of using print or better set up the ELK stack

### Possible security measures
* Add CORS guard/rule
* The standard http security headers
* 

## In production we can use:
* Gunicorn and Uvicorn
* nginx for reverse proxy
  
It will be better to isolate the LLM adapter calls in a separate layer. It will avoid rate limit abuse or any other malicious intents.

It will be better to have a separate requiremenets-dev.txt containing only the dev-related packages - liniting, testing, etc.
