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
- `--version`: Show program version and exit.

Example:
```bash
pyfetch --fields OS,CPU,Shell,Packages --color-key BLUE --color-value YELLOW
pyfetch --no-art --config ~/.my_pyfetch.conf
ptfetch --version
```

## Configuration
Create a `~/.pyfetch.conf` file to set defaults:
```ini
[pyfetch]
no_art = False,
fields = OS,CPU,Memory,Disk,Shell,Uptime,Packages
color_key = CYAN
color_value = GREEN
ascii_art = /path/to/custom_ascii.txt