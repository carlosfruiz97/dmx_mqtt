# dmx_mqtt
Script python para controlar un usb dmx a traves de una conexión mqtt


```bash
cd ~
git clone https://github.com/carlosfruiz97/dmx_mqtt.git 
```

Add nameserver 8.8.8.8 to /etc/resolv.conf
```bash
python -m venv ~/dmx-env
~/dmx-env/bin/pip install paho-mqtt
~/dmx-env/bin/pip install pyserial
~/dmx-env/bin/pip install pyyaml
cp ~/dmx_mqtt/conf_template.yaml ~/dmx_mqtt/conf.yaml
```

Editar configuracion de mqtt 
```bash
~/dmx_mqtt/conf.yaml
```

Run as a service

```bash
sudo nano /etc/systemd/system/dmx-mqtt.service
```



~/dmx-env/bin/python ~/dmx_mqtt/dmx_mqtt.py ~/dmx_mqtt/conf.yaml

# Install and setup
Clone repo and make install.sh runnable `chmod +x install.sh`

Run: 
```
cd ~
bash <(curl -s https://raw.githubusercontent.com/carlosfruiz97/dmx_mqtt/main/install.sh)
```