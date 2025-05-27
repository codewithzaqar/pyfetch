import os
import configparser
import pathlib
from colorama import Fore

def load_config(config_path=None):
    """Load configuration from a file or return defaults."""
    valid_colors = {"RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"}
    config = {
        "no_art": False,
        "fields": None,
        "color_key": "CYAN",
        "color_value": "GREEN",
        "ascii_art": None,
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
                color_key = cfg["pyfetch"].get("color_key", config["color_key"]).upper()
                color_value = cfg["pyfetch"].get("color_value", config["color_value"]).upper()
                config["color_key"] = color_key if color_key in valid_colors else config["color_key"]
                config["color_value"] = color_value if color_value in valid_colors else config["color_value"]
                config["ascii_art"] = cfg["pyfetch"].get("ascii_art", None)
                if config["ascii_art"]:
                    # Read custom ASCII art from file
                    if os.path.exists(config["ascii_art"]):
                        with open(config["ascii_art"], "r") as f:
                            config["ascii_art"] = f.read()
                    else:
                        print(f"Warning: ASCII art file {config['ascii_art']} not found")
                        config["ascii_art"] = None
        else:
            print(f"Warning: Config file {config_file} not found, using defaults")
    except Exception as e:
        print(f"Warning: Failed to load config file {config_file}: {str(e)}")

    return config