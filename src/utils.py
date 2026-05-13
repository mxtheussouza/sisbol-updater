from pathlib import Path

LAST_IP_FILE = "last_ip.txt"

def load_last_ip():
    path = Path(LAST_IP_FILE)

    if not path.exists():
        return None

    return path.read_text().strip()

def save_last_ip(ip):
    Path(LAST_IP_FILE).write_text(ip)