
## Development Steps - Roadmap
0. Decide on stack, libraries, tools and enviroment requirments
1. Scaffold FastAPI project
2. Design API schema
3. Implement HTTP endpoints/methods 
4. Create LLM adapter interface
5. Add Redis caching layer
6. Build local LLM stub
7. Implement input validation
8. Create a scheduler with worker modules or set up a ready product like Celery
9. Create Dockerfile
10. Create docker-compose.yml
11. Create Kubernetes manifests
12. Set up logging
13. Prepare unit and integration tests
14. Prepare README
15. Deploy to Kubernetes

## Architecture

![alt text](https://github.com/torlakee/Camplight-RewriteForge-Service/blob/main/diagram.png)

FastApi app exposing the following HTTP methods:

1. [POST] /v1/rewrite - a method which returns result immediately - synchronious
2. [POST] /v1/rewrite/submit - a method which will create a new job and return its id - asynchronous
3. [GET] /v1/rewrite/result/:id - a method which will return a result by job id - synchronious
4. [POST] /v1/rewrite/sse - SSE stream
5. [POST] /v1/rewrite/chunked - Chunked stream
6. [GET] /health - health check


Input validation:
* We have to check the length of the body.
* We have to check the format of the POST requests. It needs to include at least "text".
* We have to check if the style is part of the enumarated possible values <pirate | haiku | formal>
* We have to check if parameter id is an existing job id.
 

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
* LLM_API__OPENAI__KEY__0=somekey
* LLM_API__OPENAI__KEY__1=anotherkey
  
* LLM_API__GEMINI__KEY__0=somekey
* LLM_API__GEMINI__KEY__1=anotherkey
  
  Different enviroments will use different mechanism to load the config information:
  
| Environment | Config Vars                    | Sensitive data/Secrets                     |
|-------------|--------------------------------|--------------------------------------------|
| Cloud       | IaC variables                  | Secure stores (Vault, SecretManager, etc.) |
| Docker      | docker-compose ... environment | /run/secrets/                              |
| K8s         | ConfigMap                      | Mount a .secrets file                      |
| Dev         | .env file                      | .secrets file                              |


## Possible bottlenecks or issues

* Redis failure/cache storage failure

* LLM APIs limitations (rates quotas) or failure/not able to respond in time.

* We have to implement a retry mechanism.

