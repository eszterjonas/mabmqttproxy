from . import mqtt

print("Start")
mqtt.client.loop_start()
print("Start after mqtt")
#mqtt.client.disconnect()