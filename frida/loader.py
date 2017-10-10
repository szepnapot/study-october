#python code
import frida
import time
device = frida.get_usb_device()
print("DEVICE: {}".format(device))
pid = device.spawn(["com.example.a11x256.frida_test"])
print("PID: {}".format(pid))
device.resume(pid)
time.sleep(1) #Without it Java.perform silently fails
session = device.attach(pid)
with open("s2.js") as f:
    script = session.create_script(f.read())
script.load()
script.post(pid)

def my_message_handler(message , payload): #define our handler
    print message
    print payload

script.on("message", my_message_handler) #register our handler to be called
script.load()

#prevent the python script from terminating
raw_input()

