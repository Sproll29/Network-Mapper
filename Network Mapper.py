import subprocess
import threading

private_IP_connected = []

def ping(num1, num2):
    for ping in range(num1, num2):
        address = "192.168.1." + str(ping)
        res = subprocess.call(["ping", address])
        if res == 0:
            print("ping to", address, "OK")
            private_IP_connected.append(address)
        elif res == 2:
            print("no response from", address)
            private_IP_connected.append(address)
        else:
            print("ping to", address, "failed!")

t1 = threading.Thread(target=ping, args=((100, 112)))
t1.start()

t2 = threading.Thread(target=ping, args=((112, 124)))
t2.start()

t3 = threading.Thread(target=ping, args=((124, 136)))
t3.start()

t4 = threading.Thread(target=ping, args=((136, 148)))
t4.start()

t5 = threading.Thread(target=ping, args=((148, 160)))
t5.start()

t6 = threading.Thread(target=ping, args=((160, 172)))
t6.start()

t7 = threading.Thread(target=ping, args=((172, 184)))
t7.start()

t8 = threading.Thread(target=ping, args=((184, 201)))
t8.start()


t8.join()
t7.join()
t6.join()
t5.join()
t4.join()
t3.join()
t2.join()
t1.join()

print("\nAvaliable IP addresses:", private_IP_connected)

