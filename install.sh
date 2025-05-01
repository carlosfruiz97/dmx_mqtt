#!/bin/bash
set -e

# === Detect and set up ===
REPO_DIR="$HOME/dmx-mqtt"
ENV_DIR="$REPO_DIR/dmx-env"
SERVICE_NAME="dmx-mqtt"
USER_NAME=$(whoami)

echo "Setting up in $REPO_DIR as user $USER_NAME"


# === Clone repo ===
if [ ! -d "$REPO_DIR" ]; then
  git clone https://github.com/carlosfruiz97/dmx_mqtt.git "$REPO_DIR"
else
  echo "Repo already exists at $REPO_DIR"
fi

cd "$REPO_DIR"

# === Copy conf template ===
cp "conf.yaml.template" "conf.yaml"

# === Create virtual environment ===
if [ ! -d "$ENV_DIR" ]; then
  echo "Creating Python virtual environment..."
  python3 -m venv "$ENV_DIR"
  "$ENV_DIR/bin/pip" install --upgrade pip
  "$ENV_DIR/bin/pip" install -r requirements.txt
fi

# === Install systemd service ===
# SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"
# TEMPLATE="dmx-mqtt.service.template"

# echo "Creating systemd service at $SERVICE_FILE"

# Replace placeholders
# sudo bash -c "sed -e 's#__USER__#$USER_NAME#g' -e 's#__WORKDIR__#$REPO_DIR#g' $TEMPLATE > $SERVICE_FILE"


echo "✅ Installed $SERVICE_NAME."
echo "Edit conf.yaml and run the following to enable service"
echo "sudo systemctl enable "$SERVICE_NAME""
echo "sudo systemctl restart "$SERVICE_NAME""