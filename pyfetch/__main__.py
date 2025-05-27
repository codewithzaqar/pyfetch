import sys
import argparse
from .display import display_info

def main():
    parser = argparse.ArgumentParser(description="Pyfetch: A Python-based system information tool")
    parser.add_argument("--no-art", action="store_true", help="Disable ASCII art")
    parser.add_argument(
        "--fields",
        type=str,
        help="Comma-separated list of fields to display (e.g., OS,CPU,Memory)",
        default="OS,Version,Kernel,CPU,Memory,Uptime,Shell"
    )
    args = parser.parse_args()
    display_info(no_art=args.no_art, fields=args.fields.split(",") if args.fields else None)

if __name__ == "__main__":
    main()