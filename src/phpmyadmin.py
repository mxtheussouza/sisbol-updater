import socket
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.browser import create_driver
from src.logger import logger

def update_ip_in_phpmyadmin(config, new_ip):
    driver = create_driver(config["headless"])

    wait = WebDriverWait(driver, 20)

    try:
        logger.info("Abrindo phpMyAdmin...")

        driver.get(config["phpmyadmin_url"])

        logger.info("Realizando login...")

        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "input_username"))
        )

        password_input = driver.find_element(By.ID, "input_password")

        username_input.send_keys(config["username"])
        password_input.send_keys(config["password"])
        password_input.send_keys(Keys.ENTER)

        logger.info("Aguardando login finalizar...")

        wait.until(
            EC.presence_of_element_located((By.ID, "pma_navigation_tree"))
        )

        logger.info("Abrindo página SQL diretamente...")

        sql_url = (
            f"{config['phpmyadmin_url']}"
            f"/index.php?route=/database/sql&db={config['database']}"
        )

        driver.get(sql_url)

        logger.info("Aguardando editor SQL...")

        sql_editor = wait.until(
            EC.presence_of_element_located((By.ID, "sqlquery"))
        )

        hostname = socket.gethostname()

        where_value = (
            hostname
            if config["where_value"] == "__HOSTNAME__"
            else config["where_value"]
        )

        print(where_value)

        query = f"""
        UPDATE `{config['table']}`
        SET `{config['ip_column']}` = '{new_ip}'
        WHERE `{config['where_column']}` = '{where_value}';
        """

        logger.info(f"Executando query: {query}")

        driver.execute_script(
            """
            if (window.CodeMirror) {
                const cm = document.querySelector('.CodeMirror').CodeMirror;
                cm.setValue(arguments[0]);
            } else {
                arguments[1].value = arguments[0];
            }
            """,
            query,
            sql_editor
        )

        execute_button = wait.until(
            EC.element_to_be_clickable((By.ID, "button_submit_query"))
        )

        execute_button.click()

        time.sleep(3)

        logger.info("Query executada com sucesso.")

        return True

    except Exception as e:
        logger.exception(f"Erro durante automação: {e}")
        return False

    finally:
        driver.quit()