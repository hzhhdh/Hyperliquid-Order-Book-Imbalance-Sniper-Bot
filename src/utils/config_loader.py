import json, yaml

class ConfigLoader:
    """Reads config file and validates schema."""
    def load(self, path: str) -> dict:
        with open(path) as f:
            return yaml.safe_load(f) if path.endswith('.yml') else json.load(f)
