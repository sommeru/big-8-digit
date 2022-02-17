# Instructions for setting up
## Prepare your Raspberry Pi
touch /boot/ssh
vim /boot/wpa_supplicant.conf

country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="SSID"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}

## SSH to your pi and run the following commands...
sudo raspi-config
- enable SPI
sudo apt-get install git python3-dev
git config --global credential.helper store
git clone https://github.com/sommeru/big-8-digit.git
vim /home/pi/big-8-digit/config.json
- # Enter your control file url here
sudo cp /home/pi/big-8-digit/big-8-digit.service /lib/systemd/system
sudo chmod 644 /lib/systemd/system/big-8-digit.service
sudo systemctl daemon-reload
sudo systemctl enable big-8-digit.service

