import os
import re
from typing import Dict
from pathlib import Path

def read_llm_keys_from_secrets(secrets_path: str = ".secrets") -> Dict[str, Dict[int, str]]:
    if not Path(secrets_path).exists():
        raise FileNotFoundError(f"{secrets_path} not found.")

    secrets = {}
    key_pattern = re.compile(r"LLM_API__([A-Z]+)__KEY__(\d+)")
    
    with open(secrets_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            match = key_pattern.match(key.strip())
            if match:
                provider = match.group(1).lower()
                index = int(match.group(2))
                secrets.setdefault(provider, {})[index] = value.strip()

    return secrets