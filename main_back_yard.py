from waterpuck import WaterPuck
# Back yard ---> Green = wemos D1 = GPIO 5, Blue = wemos D5 = GPIO 14
water_puck = WaterPuck(5, 14)
# Static ip
water_puck.listen('192.168.86.121', 8007)
