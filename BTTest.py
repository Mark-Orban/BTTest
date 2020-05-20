import bluetooth

print("Searching for nearby devices...\n")
try:

    devices = bluetooth.discover_devices(lookup_names=True)
except:
    print("Error")

print(devices)

while devices == []:
    print("No bluetooth devices found")
    retry = input("Try again? Y/N: ")
    if retry.lower() == "n":
        exit()

    print("Searching for nearby devices...\n")

    devices = bluetooth.discover_devices(lookup_names=True)
    

num = 0

for addr, name in devices:
    num+=1
    print(num, ".", name, "-", addr)

device_selected = int(input("Select your device: "))-1

print("You have selected:", devices[device_selected][1])

addr = str(devices[device_selected][0])

port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((addr[2:19], port))
    
def test():
        sock.send(str.encode("Hello"))

test()
