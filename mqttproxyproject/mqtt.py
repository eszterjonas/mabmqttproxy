import paho.mqtt.client as mqtt

address = 'mab.inf.elte.hu'  # mab.inf.elte.hu
port = int(443)  # 443
username = 'tm_user2'
password = '123'
user = 'User1'

flag_connected = 0

def on_connect(c, userdata, flags, rc):
    if rc == 0:
        print('Connected.')
        client.subscribe(f'devices/{username}/inbox/#')
    else:
        print('Not connected.')
        exit(rc)

def publishMessage(message, topic):
    global client , username, user
    print(message)
    print(topic)
    client.publish(f'users/everyone/inbox/server/{topic}', message)
    
def on_message(c, userdata, msg):
    global client
    print(f'Topic: {msg.topic}')
    payload = msg.payload.decode('utf-8')
    if payload:
        print(f'Message: {payload}')
    if msg.topic == f'devices/{username}/inbox/{user}/100':
        print(f'Device reserved for {user}')
        client.publish(f'users/{user}/inbox/{username}/200')
    elif msg.topic == f'devices/{username}/inbox/{user}/function/{funct}':
        client.publish(f'users/{user}/inbox/{username}/functionResult/ok')


client = mqtt.Client(client_id=username, transport='websockets')
client.tls_set()
client.ws_set_options('/mqttservice')
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(address, port)
