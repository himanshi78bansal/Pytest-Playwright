#!/bin/bash
set -e

ALLURE_VERSION="2.27.0"
ALLURE_ZIP="allure-${ALLURE_VERSION}.zip"
ALLURE_DIR="allure-${ALLURE_VERSION}"
INSTALL_PATH="/opt/allure"

echo "🔹 Installing prerequisites (safe mode)..."
sudo apt update || echo "⚠️ apt update failed, continuing..."
sudo apt install -y curl unzip || {
  echo "❌ Failed to install curl/unzip"
  exit 1
}

echo "🔹 Cleaning old downloads..."
rm -f ${ALLURE_ZIP}

echo "🔹 Downloading Allure ${ALLURE_VERSION} (SSL bypass due to corporate proxy)..."
wget --no-check-certificate \
  https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/${ALLURE_ZIP}

echo "🔹 Verifying zip file..."
file ${ALLURE_ZIP} | grep -q "Zip archive data" || {
  echo "❌ Invalid zip file downloaded. Aborting."
  exit 1
}

echo "🔹 Extracting Allure..."
unzip -q ${ALLURE_ZIP}

echo "🔹 Installing to ${INSTALL_PATH}..."
sudo rm -rf ${INSTALL_PATH}
sudo mv ${ALLURE_DIR} ${INSTALL_PATH}

echo "🔹 Creating symlink..."
sudo ln -sf ${INSTALL_PATH}/bin/allure /usr/bin/allure

echo "🔹 Cleaning up..."
rm -f ${ALLURE_ZIP}

echo "✅ Allure installation completed successfully!"
allure --version
