import os
import json

with open("config.json") as f:
    env_vars = json.load(f)

HUGGINGFACEHUB_API_TOKEN = env_vars["HF_API_KEY"]