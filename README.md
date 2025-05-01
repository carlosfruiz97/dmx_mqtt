# dmx_mqtt
Script que se instala como servicio. Se conecta a un USB-DMX y a un servidor MQTT. Se pueden mandar comandos mqtt.


ToDo:
- Auotdetectar usb
- Gestionar fallo de conexion usb
- Gestionar fallo de conexion mqtt
- Control versiones

# Install and setup
Clone repo and make install.sh runnable `chmod +x install.sh`

Run installer: 
```
cd ~
bash <(curl -s https://raw.githubusercontent.com/carlosfruiz97/dmx_mqtt/main/install.sh)
```

Editar configuracion
```
nano ~/dmx_mqtt/conf.yaml
```

Run
```
~/dmx_mqtt/dmx-env/bin/python ~/dmx_mqtt/dmx_mqtt.py ~/dmx_mqtt/conf.yaml
```

Run as a service
```bash
# Reload and enable
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable dmx-mqtt
sudo systemctl restart dmx-mqtt
```




# MQTT
Subscribed to `{topic_head}/{topic_cmd}`
payload
```javascript
{
    "ch":1,
    "val":100
}
```

```javascript
[
    { "ch":1, "val":100 },
    { "ch":2, "val":200 }
]
```


Subscribe to `{topic_head}/{topic_clear}` to clear

