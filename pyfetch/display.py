import shutil
from colorama import init, Fore, Style
from .system_info import get_system_info
from .ascii_art import get_ascii_art

# Initialize colorama
init()

def display_info(no_art=False, fields=None, color_key="CYAN", color_value="GREEN"):
    """Display system information with ASCII art."""
    info = get_system_info()
    ascii_art = get_ascii_art().splitlines() if not no_art else []

    # Filter fields if specified
    if fields:
        info = {k: v for k, v in info.items() if k in fields}

    # Get terminal width for dynamic alignment
    terminal_width = shutil.get_terminal_size().columns
    max_key_len = max(len(key) for key in info.keys()) if info else 10
    art_width = 50 if ascii_art else 0
    info_width = min(max_key_len + 2 + 30, terminal_width - art_width - 5)  # Reserve space for values

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
    max_lines = max(len(ascii_art), len(info_lines)) if ascii_art else len(info_lines)

    # Pad lists to equal length
    ascii_art.extend([""] * (max_lines - len(ascii_art)))
    info_lines.extend([""] * (max_lines - len(info_lines)))

    # Combine lines
    for art, info_line in zip(ascii_art, info_lines):
        output.append(f"{Fore.YELLOW}{art:<{art_width}}{Style.RESET_ALL} {info_line}" if not no_art else info_line)

    print("\n".join(output))