import yaml

def load_config(config_path: str = "/Users/mukulagarwal/Desktop/Projects/agentic-trading-bot/config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config