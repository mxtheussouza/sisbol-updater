# SISBOL IP Updater

Automação para atualização automática de IP no phpMyAdmin do SISBOL.

Compatível com:

* Windows
* Linux

Tecnologias:

* Python
* Selenium
* Chromium

---

# Objetivo

O sistema:

1. Detecta o IP atual da máquina;
2. Aguarda a rede ficar disponível;
3. Abre o phpMyAdmin;
4. Faz login automaticamente;
5. Atualiza o IP da máquina usando o hostname;
6. Finaliza.

---

# Estrutura do Projeto

```txt id="gq3m4o"
sisbol-updater/
│
├── main.py
├── config.json
├── requirements.txt
├── last_ip.txt
│
├── browser/
│   ├── chrome-linux64/
│   └── chrome-win64/
│
├── drivers/
│   ├── chromedriver
│   └── chromedriver.exe
│
├── logs/
│   └── updater.log
│
└── src/
```

---

# Requisitos

## Windows

* Python 3.11+
* Chromium portátil
* ChromeDriver

---

## Linux

* Python 3.11+
* Chromium portátil
* ChromeDriver
* systemd

---

# Instalação — Windows

## 1. Instalar Python

Baixar:

[Python Downloads](https://www.python.org/downloads)

Durante instalação marcar:

```txt id="uyqwtj"
Add Python to PATH
```

---

# 2. Extrair projeto

Exemplo:

```txt id="jlwm0a"
C:\sisbol-updater
```

---

# 3. Criar ambiente virtual

Abrir CMD/Powershell na pasta do projeto:

```powershell id="jlwm1a"
python -m venv venv
```

---

# 4. Ativar ambiente virtual

```powershell id="jlwm2a"
venv\Scripts\activate
```

---

# 5. Instalar dependências

```powershell id="jlwm3a"
pip install -r requirements.txt
```

---

# 6. Configurar config.json

Exemplo:

```json id="jlwm8a"
{
  "phpmyadmin_url": "https://intranets.51ct.eb.mil.br/phpmyadmin",
  "username": "USUARIO",
  "password": "SENHA",

  "database": "blocksisbol",

  "table": "19bc",
  "ip_column": "ip",
  "where_column": "hostname",
  "where_value": "__HOSTNAME__",

  "headless": true
}
```

---

# 7. Testar execução

```powershell id="jlwm9a"
python main.py
```

---

# 8. Automatizar no Windows

Abrir:

```txt id="jlvmaa"
Agendador de Tarefas
```

---

## Criar tarefa

### Geral

Nome:

```txt id="jlvmba"
SISBOL IP Updater
```

Marcar:

```txt id="jlvnca"
Executar com privilégios mais altos
```

---

## Disparadores

Adicionar:

```txt id="jlvnda"
Ao fazer logon
```

---

## Ações

Programa:

```txt id="jlvnea"
C:\sisbol-updater\venv\Scripts\python.exe
```

Argumentos:

```txt id="jlvnfa"
C:\sisbol-updater\main.py
```

---

# Instalação — Linux

---

# 1. Instalar Python

Ubuntu/Debian:

```bash id="jlvnga"
sudo apt update
sudo apt install python3 python3-venv -y
```

---

# 2. Copiar projeto

```bash id="jlvnha"
sudo mkdir -p /opt/sisbol-updater
sudo cp -r . /opt/sisbol-updater
```

---

# 3. Entrar na pasta

```bash id="jlvnia"
cd /opt/sisbol-updater
```

---

# 4. Criar ambiente virtual

```bash id="jlvnja"
python3 -m venv venv
```

---

# 5. Ativar ambiente virtual

```bash id="jlvnka"
source venv/bin/activate
```

---

# 6. Instalar dependências

```bash id="jlvnla"
pip install -r requirements.txt
```

---

# 7. Dar permissões

```bash id="jlvnqa"
chmod +x drivers/chromedriver
chmod +x browser/chrome-linux64/chrome
```

---

# 8. Configurar config.json

Mesmo exemplo do Windows.

---

# 9. Testar execução

```bash id="jlvnra"
python3 main.py
```

---

# 10. Criar service

Arquivo:

```txt id="jlvnsa"
/etc/systemd/system/sisbol-updater.service
```

Conteúdo:

```ini id="jlvnta"
[Unit]
Description=SISBOL IP Updater
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=/opt/sisbol-updater
ExecStart=/opt/sisbol-updater/venv/bin/python /opt/sisbol-updater/main.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

---

# 11. Recarregar systemd

```bash id="jlvnua"
sudo systemctl daemon-reload
```

---

# 12. Ativar inicialização automática

```bash id="jlvnva"
sudo systemctl enable sisbol-updater
```

---

# 13. Iniciar serviço

```bash id="jlvnwa"
sudo systemctl start sisbol-updater
```

---

# 14. Verificar status

```bash id="jlvnxa"
sudo systemctl status sisbol-updater
```

---

# Logs

Arquivo:

```txt id="jlvnya"
logs/updater.log
```

---

# Ver logs Linux

```bash id="jlvnza"
journalctl -u sisbol-updater -f
```

---

# Fluxo da Automação

```txt id="jlvo0a"
Liga computador
↓
Rede sobe
↓
IP é detectado
↓
phpMyAdmin abre
↓
Login automático
↓
UPDATE executado
↓
Finaliza
```

---

# Observações

* O hostname da máquina é usado automaticamente no WHERE;
* O sistema evita atualização desnecessária;
* O projeto utiliza Chromium portátil;
* Não depende do navegador instalado;
* Compatível com Windows e Linux.
