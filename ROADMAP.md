
## Architecture



FastApi app exposing the following HTTP methods:
1 [POST] /v1/rewrite - a method which returns result immediately - synchronious
2 [POST] /v1/rewrite/submit - a method which will create a new job and return its id - asynchronous
3 [GET] /v1/rewrite/result/:id - a method which will return a result by job id - synchronious
4 [POST] /v1/rewrite/sse - SSE stream
5 [POST] /v1/rewrite/chunked - Chunked stream
6 [GET] /health - health check

Input validation:
 We have to check the format of the POST requests.
 We have to check if the style is part of the enumarated possible values <pirate | haiku | formal>
 We have to check if parameter id is an existing job id.

## Project layout
 Create project codebase structure
* src/
  * deployment/
    * configuration.py - Class used for loading the enviroment variables and secrets
  * adapters/
    * openai.py
    * stub.py
  * routes/
  * models/
  * caching/
  * entrypoint.py
* docs/
* tests/
  * unit/
  * integration/

This is an initial codebase structure. It will be changed during the development. 

Create a pyproject.toml file for specifying dependecies and lint tools

## Lint / format
 I will use the following packages/tools:
* Container scanning: **trivy**
* Secrets analysis: **trufflehog**
* Dependency vulnerability scanner: **safety**
* Linting and docutype: **Ruff, bandit**

   
* Automated security testing: **ZAP**

## Config & secrets
  We will have 2 files:
  
* **.env** - specifies configuration variables
* **.secrets** - contains the sensitive information
   
  I assume that we expect to scale the application and we will need more than 1 key per LLM adapter. In case a certain key is already in use, it will pick the next key.
  
  .secrets will have the following structure:
  LLM_API__OPENAI__KEY__0=somekey
  LLM_API__OPENAI__KEY__1=anotherkey
  
  LLM_API__GEMINI__KEY__0=somekey
  LLM_API__GEMINI__KEY__1=anotherkey
  
  Different enviroments will use different mechanism to load the config information:
