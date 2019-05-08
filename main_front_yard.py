# The front yard has one valve.
# it is on the wemos GPIO 4, which is I believe D2.
from waterpuck import WaterPuck
# The IP address is the one I want to be it's static ip.
water_puck = WaterPuck(4)
water_puck.listen('192.168.86.120',8006)
