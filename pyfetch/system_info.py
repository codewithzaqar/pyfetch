import platform
import psutil
import os
import getpass

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

        return info
    except Exception as e:
        return {"Error": f"Failed to gather system info: {str(e)}"}