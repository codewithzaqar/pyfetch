# Pyfetch

A Python-based command-line system information tool inspired by Neofetch.

## Installation 

```bash
pip install pyfetch
```

## Usage
Run the tool with
```bash
pyfetch
```
### Option
- `--no-art`: Disable ASCII art.
- `--fields`: Specify fields to display (e.g, `OS`,`CPU`,`Memory`,`Disk`).
- `--color-key`: Set color for keys (e.g, RED, BLUE, CYAN).
- `--config`: Spacify a custom config file path

Example:
```bash
pyfetch --fields OS,CPU,Shell --no-art
```

## Configuration
Create a `~/.pyfetch.conf` file to set defaults:
```ini
[pyfetch]
no_art = False,
fields = OS,CPU,Memory,Disk,Shell,Uptime
color_key = CYAN
color_value = GREEN