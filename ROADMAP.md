
## Project layout

## Lint / format
 I will use the following packages/tools:
   Container scanning: trivy
   Secrets analysis: trufflehog 
   Dependency vulnerability scanner: safety
   Linting and docutype: Ruff, bandit

   
   Automated security testing: ZAP

## Config & secrets
  We will have 2 files:
  
* .env - specifies configuration variables
* .secrets - contains the sensitive information
   
  I assume that we expect to scale the application and we will need instead of a single Key for each adapter. If a key is in use it will go to the next one.
  
  .secrets will have the following structure:
  LLM_API__OPENAI__KEY__0=somekey
  LLM_API__OPENAI__KEY__1=anotherkey
  
  LLM_API__GEMINI__KEY__0=somekey
  LLM_API__GEMINI__KEY__1=anotherkey
  
  Different enviroments will use different mechanism to load the config information:
