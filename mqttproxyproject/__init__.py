from . import mqtt

mqtt.client.loop_start()

if mqtt.flag_connected == 1:
    print("Succesfully connected")
else: 
    print("Something happened")


#mqtt.client.disconnect()