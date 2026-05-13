import socket
import time

def get_current_ip(timeout=300):
    start = time.time()

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect(("8.8.8.8", 80))

            ip = s.getsockname()[0]

            s.close()

            if ip and not ip.startswith("127."):
                return ip

        except Exception:
            pass

        if time.time() - start > timeout:
            raise Exception("Timeout aguardando rede.")

        print("Aguardando rede/IP...")

        time.sleep(10)