import platform
import psutil
import os

def get_system_info():
    """Collect system information."""
    try:
        # OS Information
        os_name = platform.system()
        os_release = platform.release()
        os_version = platform.version()

        # Kernel
        kernel = platform.uname().release if os_name != "Windows" else platform.release()

        # CPU
        cpu = platform.processor()
        cpu_cores = psutil.cpu_count(logical=True)

        # Memory
        memory = psutil.virtual_memory()
        total_memory = memory.total / (1024 ** 3)  # Convert to GB
        used_memory = memory.used / (1024 ** 3)    # Convert to GB

        # Uptime
        uptime_seconds = psutil.boot_time()
        uptime = f"{int(uptime_seconds // 3600)} hours, {int((uptime_seconds % 3600) // 60)} mins"

        return {
            "OS": f"{os_name} {os_release}",
            "Version": os_version,
            "Kernel": kernel,
            "CPU": f"{cpu} ({cpu_cores} cores)",
            "Memory": f"{used_memory:.1f} GiB / {total_memory:.1f} GiB",
            "Uptime": uptime
        }
    except Exception as e:
        return {"Error": f"Failed to gather system info: {str(e)}"}