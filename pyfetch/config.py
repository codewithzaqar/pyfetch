import os
import configparser
import pathlib

def load_config(config_path=None):
    """Load configuration from a file or return defaults."""
    config = {
        "no_art": False,
        "fields": None,
        "color_key": "CYAN",
        "color_value": "GREEN"
    }

    # Default config path: ~/.pyfetch.conf
    default_path = os.path.expanduser("~/.pyfetch.conf")
    config_file = config_path or default_path

    try:
        if os.path.exists(config_file):
            cfg = configparser.ConfigParser()
            cfg.read(config_file)
            if "pyfetch" in cfg:
                config["no_art"] = cfg["pyfetch"].getboolean("no_art", config["no_art"])
                config["fields"] = cfg["pyfetch"].get("fields", "").split(",") if cfg["pyfetch"].get("fields") else None
                config["color_key"] = cfg["pyfetch"].get("color_key", config["color_key"]).upper()
                config["color_value"] = cfg["pyfetch"].get("color_value", config["color_value"]).upper()
    except Exception as e:
        print(f"Warning: Failed to load config file {config_file}: {str(e)}")

    return config