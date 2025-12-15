import yaml
import os

def load_settings():
    with open("config/settings.yaml", "r") as f:
        settings = yaml.safe_load(f)

    return settings
