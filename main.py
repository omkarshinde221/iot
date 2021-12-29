# python 3.6
from flask import Flask, render_template
import random

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
broker = 'broker.emqx.io'
port = 1883
topic = "topicName/led"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client


def led_on(client):
    msg = f"1"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")


def led_off(client):
    msg = f"2"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")

def led_off3(client):
    msg = f"3"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")

def led_off4(client):
    msg = f"4"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/1', methods=['POST'])
def turn_on():
    ran_on()
    return render_template('index.html')

def ran_on():
    client = connect_mqtt()
    client.loop_start()
    led_on(client)

@app.route('/2', methods=['POST'])
def turn_off():
    ran_off()
    return render_template('index.html')

def ran_off():
    client = connect_mqtt()
    client.loop_start()
    led_off(client)

@app.route('/3', methods=['POST'])
def turn_off3():
    ran_off3()
    return render_template('index.html')

def ran_off3():
    client = connect_mqtt()
    client.loop_start()
    led_off3(client)

@app.route('/4', methods=['POST'])
def turn_off4():
    ran_off4()
    return render_template('index.html')

def ran_off4():
    client = connect_mqtt()
    client.loop_start()
    led_off4(client)



if __name__ == "__main__":
    app.run(port=5001)
