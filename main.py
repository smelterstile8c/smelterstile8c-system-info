"""Print basic system information using only the standard library."""

import json
import os
import platform
import sys


def collect():
    info = {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python": platform.python_version(),
        "cwd": os.getcwd(),
        "argv": sys.argv[1:],
        "cpu_count": os.cpu_count(),
    }
    try:
        info["load_avg"] = [round(x, 2) for x in os.getloadavg()]
    except OSError:
        pass
    return info


def main():
    fmt = sys.argv[1] if len(sys.argv) > 1 else "text"
    info = collect()
    if fmt == "json":
        print(json.dumps(info, indent=2))
        return 0
    for key, value in info.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

