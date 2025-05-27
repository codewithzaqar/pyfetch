import shutil
from colorama import init, Fore, Style
from .system_info import get_system_info
from .ascii_art import get_ascii_art

# Initialize colorama
init()

def display_info(no_art=False, fields=None, color_key="CYAN", color_value="GREEN", ascii_art=None):
    """Display system information with optional ASCII art, fields, and custom colors."""
    info = get_system_info()
    ascii_lines = ascii_art.splitlines() if ascii_art else get_ascii_art().splitlines() if not no_art else []

    # Filter fields if specified
    if fields:
        info = {k: v for k, v in info.items() if k in fields}

    # Get terminal width for dynamic alignment
    terminal_width = shutil.get_terminal_size().columns
    max_key_len = max(len(key) for key in info.keys()) if info else 10
    art_width = max(len(line) for line in ascii_lines) if ascii_lines else 0
    info_width = min(max_key_len + 2 + 30, terminal_width - art_width - 5)

    # Map color names to colorama attributes
    color_map = {
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    key_color = color_map.get(color_key.upper(), Fore.CYAN)
    value_color = color_map.get(color_value.upper(), Fore.GREEN)

    # Prepare output
    output = []
    info_lines = [f"{key_color}{key:<{max_key_len}}{Style.RESET_ALL}: {value_color}{value}{Style.RESET_ALL}" for key, value in info.items()]
    max_lines = max(len(ascii_lines), len(info_lines)) if ascii_lines else len(info_lines)

    # Pad lists to equal length
    ascii_lines.extend([""] * (max_lines - len(ascii_lines)))
    info_lines.extend([""] * (max_lines - len(ascii_lines)))

    # Combine lines with dynamic spacing
    for art, info_line in zip(ascii_lines, info_lines):
        output.append(f"{Fore.YELLOW}{art:<{art_width}}{Style.RESET_ALL} {info_line}" if not no_art else info_line)

    print("\n".join(output))