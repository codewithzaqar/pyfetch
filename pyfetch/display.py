from .system_info import get_system_info
from .ascii_art import get_ascii_art

def display_info():
    """Display system information with ASCII art."""
    info = get_system_info()
    ascii_art = get_ascii_art().splitlines()

    # Prepare output
    max_key_len = max(len(key) for key in info.keys()) if info else 10
    output = []

    # Combine ASCII art with system info
    info_lines = [f"{key:<{max_key_len}}: {value}" for key, value in info.items()]
    max_lines = max(len(ascii_art), len(info_lines))

    # Pad lists to equal length
    ascii_art.extend([""] * (max_lines - len(ascii_art)))
    info_lines.extend([""] * (max_lines - len(info_lines)))

    # Combine lines
    for art, info_line in zip(ascii_art, info_lines):
        output.append(f"{art:<50} {info_line}")

    print("\n".join(output))