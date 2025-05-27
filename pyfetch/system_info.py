import platform
import psutil
import os
import getpass
import subprocess
import functools

@functools.lru_cache(maxsize=1)
def get_system_info():
    """Collect system information."""
    info = {}
    try:
        # OS Information
        os_name = platform.system()
        info["OS"] = f"{os_name} {platform.release()}"
        info["Version"] = platform.version()

        # Kernel
        kernel = platform.uname().release if os_name != "Windows" else platform.release()

        # CPU
        try:
            info["CPU"] = f"{platform.processor()} ({psutil.cpu_count(logical=True)} cores)"
        except Exception:
            info["CPU"] = "Unknown"

        # Memory
        try:
            memory = psutil.virtual_memory()
            info["Memory"] = f"{memory.used / (1024 ** 3):.1f} GiB / {memory.total / (1024 ** 3):.1f} GiB"
        except Exception:
            info["Memory"] = "Unknown"

        # Disk Usage
        try:
            disk = psutil.disk_usage("/")
            info["Disk"] = f"{disk.used / {1024 ** 3}:.1f} GiB / {disk.total / {1024 ** 3}:.1f} GiB"
        except Exception:
            info["Disk"] = "Unknown"

        # Uptime
        try:
            uptime_seconds = psutil.boot_time()
            info["Uptime"] = f"{int(uptime_seconds // 3600)} hours, {int((uptime_seconds % 3600) // 60)} mins"
        except Exception:
            info["Uptime"] = "Unknown"

        # Shell
        try:
            shell = os.environ.get("SHELL", getpass.getuser() + "@" + os_name)
            info["Shell"] = shell.split("/")[-1]
        except Exception:
            info["Shell"] = "Unknown"

        # Package Manager
        try:
            package = "Unknown"
            if os_name == "Linux":
                if os.path.exists("/usr/bin/dpkg"):
                    result = subprocess.run(["dpkg", "--list"], capture_output=True, text=True)
                    packages = str(len(result.stdout.splitlines()) - 5) + " (apt)"
                elif os.path.exists("/usr/bin/rpm"):
                    result = subprocess.run(["rpm", "-qa"], capture_output=True, text=True)
                    packages = str(len(result.stdout.splitlines())) + " (yum/rpm)"
                elif os.path.exists("/usr/bin/pacman"):
                    result = subprocess.run(["pacman", "-Q"], capture_output=True, text=True)
                    packages = str(len(result.stdout.splitlines()))
            info["Packages"] = packages
        except Exception:
            info["Packages"] = "Unknown"

        return info
    except Exception as e:
        return {"Error": f"Failed to gather system info: {str(e)}"}