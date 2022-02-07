vim /boot/wpa_supplicant.conf

country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="snet"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}

touch /boot/ssh


