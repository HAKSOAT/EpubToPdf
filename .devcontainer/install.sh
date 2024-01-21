#! /bin/bash
sudo apt-get -q update
sudo apt-get -qy install --no-install-recommends wget
# https://github.com/wkhtmltopdf/packaging/releases
wget -nv -O /tmp/wkhtmltox.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_arm64.deb
sudo apt-get -qy install /tmp/wkhtmltox.deb
sudo apt --fix-broken install -y
