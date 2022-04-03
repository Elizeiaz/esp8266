import psutil
import socket
import platform
import statistics

HOST = '192.168.0.138'
PORT = 9090

# psutil.sensors_battery().percent,
#             psutil.virtual_memory().percent,
#             psutil.cpu_percent(1)

s = socket.socket()

if __name__ == '__main__':
    s.connect((HOST, PORT))
    while True:
        data = [
            str(platform.uname().node),
            str(round(statistics.mean(psutil.cpu_percent(0.5, percpu=True)), 1)),
            str(psutil.virtual_memory().percent),
            str(psutil.sensors_battery().percent)]

        s.send(';'.join(data).encode())
