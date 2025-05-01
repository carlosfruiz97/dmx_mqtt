import paho.mqtt.client as mqtt
import serial
import json
import time
import threading
import yaml
import sys

class DmxMqtt:
    def __init__(self, yamlpath:str):
        with open(yamlpath, 'r') as file:
            conf:dict = yaml.safe_load(file)

        dmx_conf:dict = conf.get('dmx_conf')
        self.dmx_port:str = dmx_conf.get('dmx_port')
        self.baudrate:int = dmx_conf.get('baudrate')

        mqtt_conf:dict = conf.get('mqtt_conf')
        self.broker:str = mqtt_conf.get('broker')
        self.port:int = mqtt_conf.get('port')

        topic_head:str = mqtt_conf.get('topic_head')
        topic_head = topic_head.strip('/') + '/'

        self.topic_cmd:str = mqtt_conf.get('topic_cmd')
        self.topic_cmd = topic_head + self.topic_cmd.strip('/')
        print(f"Subscribing to {self.topic_cmd}")

        self.topic_clear:str = mqtt_conf.get('topic_clear')
        self.topic_clear = topic_head + self.topic_clear.strip('/')
        print(f"Subscribing to {self.topic_clear}")

        self.topic_state:str = mqtt_conf.get('topic_state')
        self.topic_state = topic_head + self.topic_state.strip('/')

        self.use_auth:bool = mqtt_conf.get('use_auth', False)
        self.mqtt_user:str = mqtt_conf.get('mqtt_user', False)
        self.mqtt_pass:str = mqtt_conf.get('mqtt_pass', False)

        self.dmx_data = bytearray(513)  # 0th is start code, then 512 channels
        
    def run(self):
        # === Start Everything ===
        client = mqtt.Client()
        if self.use_auth:
            client.username_pw_set(self.mqtt_user, self.mqtt_pass)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.broker, self.port, 60)

        threading.Thread(target=self._dmx_loop, daemon=True).start()
        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT broker with result code", rc)
        client.subscribe(self.topic_cmd)
        client.subscribe(self.topic_clear)

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode()

        if topic == self.topic_cmd:
            try:
                data = json.loads(payload)
                channel = int(data["channel"])
                value = int(data["value"])
                if 1 <= channel <= 512 and 0 <= value <= 255:
                    self.dmx_data[channel] = value
            except Exception as e:
                print("Error processing /dmx/cmd message:", e)

        elif topic == self.topic_clear:
            self.dmx_data = bytearray(513)

        # After any update, publish full state
        client.publish(self.topic_state, json.dumps(list(self.dmx_data[1:])))

    def _dmx_loop(self):
        with serial.Serial(self.dmx_port, baudrate=self.baudrate, bytesize=8, parity='N', stopbits=2) as ser:
            while True:
                ser.break_condition = True
                time.sleep(0.001)
                ser.break_condition = False
                time.sleep(0.001)
                ser.write(self.dmx_data)
                time.sleep(0.025)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dmx_mqtt_bridge.py <config.yaml>")
        sys.exit(1)

    config_path = sys.argv[1]
    dmx_mqtt = DmxMqtt(config_path)
    dmx_mqtt.run()