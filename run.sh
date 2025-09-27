#!/bin/bash
set -e  # если какая-то команда завершится с ошибкой — скрипт остановится

PROJECT_DIR="/home/exoticsa/get_position_from_google"
VENV_DIR="$PROJECT_DIR/venv"

cd "$PROJECT_DIR" || exit 1

source "$VENV_DIR/bin/activate"

echo "Запуск xls_worker.py..."
python xls_worker.py

echo "Запуск send_mail.py..."
python send_mail.py

deactivate

echo "Готово!"
