class Server:
    pass

# from machine import I2C, Pin
# from time import sleep_ms
# import ssd1306
# import network
# import socket
# import display

# i2c = I2C(scl=Pin(5), sda=Pin(4))
# display = display.Display(i2c)
#
# display.show_info('Start')
#
# sta = network.WLAN(network.STA_IF)
# sta.connect('Elizeiazzzar', 'smaillwar')
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 9090))
# s.listen(1)
#
#
# def start_server(s: socket):
#     display.show_info('Wait connection')
#     conn, addr = s.accept()
#     display.show_info('Connected!')
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             display.show_info('Error')
#         else:
#             display.show_data(data.decode())
#
#
# while True:
#     try:
#         start_server(s)
#     except:
#         pass
