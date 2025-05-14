import os
from dotenv import load_dotenv
from pathlib import Path

def load_config():
    base_dir = Path(__file__).resolve().parent.parent.parent
    load_dotenv(base_dir / ".env")
    load_dotenv(base_dir / ".secrets", override=True)