# dmx_mqtt
Script python para controlar un usb dmx a traves de una conexión mqtt


```bash
cd ~
git clone https://github.com/carlosfruiz97/dmx_mqtt.git 
```

```bash
# Add nameserver 8.8.8.8 to /etc/resolv.conf
python -m venv ~/dmx-env
~/dmx-env/bin/pip install paho-mqtt
~/dmx-env/bin/pip install pyserial
~/dmx-env/bin/pip install pyyaml
cp ~/dmx_mqtt/conf_template.yaml ~/dmx_mqtt/conf.yaml
```

```bash
~/dmx-env/bin/python ~/dmx_mqtt/dmx_mqtt.py ~/dmx_mqtt/conf.yaml
```
