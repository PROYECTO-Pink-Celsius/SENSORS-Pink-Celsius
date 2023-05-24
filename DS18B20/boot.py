import network
from .config import WIFI_SSID, WIFI_PASSWORD

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
while not sta_if.isconnected():
    pass

print('Connected to WiFi')