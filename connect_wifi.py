import network, utime

import esp
esp.osdebug(None)

import gc
gc.collect()

# def do_connect():
#     try:
#         sta_if = network.WLAN(network.STA_IF)
#         if not sta_if.isconnected():
#             sta_if.active(True)
#             sta_if.connect('donsky-4thFloor', 'donsky982')
#             while not sta_if.isconnected():
#                 pass
#         print('network config:', sta_if.ifconfig())
#     except Exception as e:
#         print("Error encountered", e)
# 
#     
# 
# do_connect()
print("Starting station connection...")
station = network.WLAN(network.STA_IF)
print("After define...")
station.active(True)
print("Start connecting...")
try:
    station.connect("donsky-4thFloor", "donsky982")
    print("Establishing connection...")
    for i in range(10):
        print("Connecting to station in {}".format(i))
        utime.sleep(1)
        if station.isconnected():
            break
        
    if station.isconnected():
        print("station Connection OK!")
        print("Network Config ", station.ifconfig())
    else:
        print("station internal error")
except Exception as e:
    print(e)