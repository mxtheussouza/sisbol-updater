from src.config import load_config
from src.ip import get_current_ip
from src.utils import load_last_ip, save_last_ip
from src.logger import logger
from src.phpmyadmin import update_ip_in_phpmyadmin

def main():
    config = load_config()

    current_ip = get_current_ip()

    logger.info(f"IP atual detectado: {current_ip}")

    last_ip = load_last_ip()

    if current_ip == last_ip:
        logger.info("IP não mudou. Nada a fazer.")
        return

    logger.info(f"IP alterado: {last_ip} -> {current_ip}")

    success = update_ip_in_phpmyadmin(config, current_ip)

    if success:
        save_last_ip(current_ip)
        logger.info("IP atualizado com sucesso.")
    else:
        logger.error("Falha ao atualizar IP.")


if __name__ == "__main__":
    main()