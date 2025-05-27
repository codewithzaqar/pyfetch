from colorama import init, Fore, Style
from .system_info import get_system_info
from .ascii_art import get_ascii_art

# Initialize colorama
init()

def display_info(no_art=False, fields=None):
    """Display system information with ASCII art."""
    info = get_system_info()
    ascii_art = get_ascii_art().splitlines() if not no_art else []

    # Filter fields if specified
    if fields:
        info = {k: v for k, v in info.items() if k in fields}

    # Prepare output
    max_key_len = max(len(key) for key in info.keys()) if info else 10
    output = []

    # Combine ASCII art with system info
    info_lines = [f"{Fore.CYAN}{key:<{max_key_len}}{Style.RESET_ALL}: {Fore.GREEN}{value}{Style.RESET_ALL}" for key, value in info.items()]
    max_lines = max(len(ascii_art), len(info_lines)) if ascii_art else len(info_lines)

    # Pad lists to equal length
    ascii_art.extend([""] * (max_lines - len(ascii_art)))
    info_lines.extend([""] * (max_lines - len(info_lines)))

    # Combine lines
    for art, info_line in zip(ascii_art, info_lines):
        output.append(f"{Fore.YELLOW}{art:<50}{Style.RESET_ALL} {info_line}" if not no_art else info_line)

    print("\n".join(output))