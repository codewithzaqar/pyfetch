import sys
import argparse
from .display import display_info
from .config import load_config
from . import __version__

def main():
    parser = argparse.ArgumentParser(description="Pyfetch: A Python-based system information tool")
    parser.add_argument("--no-art", action="store_true", help="Disable ASCII art")
    parser.add_argument(
        "--fields",
        type=str,
        help="Comma-separated list of fields to display (e.g., OS,CPU,Memory)",
        default="OS,Version,Kernel,CPU,Memory,Uptime,Shell"
    )
    parser.add_argument(
        "--color-key",
        type=str,
        help="Color for keys (e.g., RED, BLUE, CYAN)",
        default=None
    )
    parser.add_argument(
        "--color-value",
        type=str,
        help="Color for values (e.g., GREEN, YELLOW, MAGENTA)",
        default=None
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to custom config file",
        default=None
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"pyfetch {__version__}",
        help="Show program's version number and exit"
    )
    args = parser.parse_args()

    #Load config from (if exists) and merge with CLI args
    config = load_config(args.config)
    config["no_art"] = args.no_art or config.get("no_art", False)
    config["fields"] = args.fields.split(",") if args.fields else config.get("fields", None)
    config["color_key"] = args.color_key or config.get("color_key", "CYAN")
    config["color_value"] = args.color_value or config.get("color_value", "GREEN")
    config["ascii_art"] = config.get("ascii_art", None)  # Custom ASCII art from config

    display_info(**config)

if __name__ == "__main__":
    main()