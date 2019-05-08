#Intro
Well, it's that time of year.  The time of year where I'm back to bumbling with my auto watering code.  This year I'm changing things up a bit.  I think this project is simpler than last year's water puck.  But hey, I'm wrong every day.  
# Experience
From any client that can send an URL:  
```
http://<TBD IP address>/water_on  
http://<TBD IP address>/water_off
http://<TBD IP address>/water_time 
http://<IP>/exit_listen 
``` 
will be sent to a wemos server running micropython. The wemos server has GPIO pin(s) set up to turn a watering valve on/off.
# Reaching From Long Distance
In order to send the URL from outside our home's wifi, I'll need an address that can go through our wifi router.  For this, I'll use [port forwarding](https://support.google.com/wifi/answer/6274503?hl=en).  
# Connect wemos to Mac over USB
To connect the wemos to the Mac using USB, the CH34X for High Sierra (OS on our macs) needs to be loaded.  _The tricky part_ is to allow the ```Jiangsu Qinheng Co.``` driver to be loaded - which is needed.  This is done in System Preferences/Security & Privacy.    
There appear to be many CH34X drivers "out there."  We ended up using the 1.4 driver found at [this GitHub](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver).
# Install micropython on the wemos
The [micropython docs have a tutorial](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) on getting micropython onto the esp8266.  We used what is currently the latest ```esp8266-20190125-v1.10.bin```.  

Following [the install instructions](http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware),   
* erase the flash:
```esptool.py --port /dev/tty.wchusbserial1410 erase_flash```  
* Copy micropython:  
```esptool.py --port /dev/tty.wchusbserial1410 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190125-v1.10.bin```    
_Note: The port path is unique to the USB port on your mac.
# Install webrepl (optional)
Since the wemos will be running headless, I like to do some debugging with [webrepl](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi).  _Note: import webrepl_setup will ask for a password.  This password is not used when connecting to the access point.  It is used when connecting to the webrepl session.__  See [wifi instructions](http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#wifi) for connecting to the AP.
# IDE
micropython doesn't have a popular, rich development environment.  Circuit Python has the mu editor.  Unfortunately, the mu editor doesn't work with CP.  We ended up using [uPyCraft](http://docs.dfrobot.com.cn/upycraft/) for code development.  It was the easiest way to write, copy files, and run micropython code on the wemos.
# Minimizing Code Size
There isn't much room for code on the esp8266.  Most micropython files have two versions:  
* *filename*_verbose.py - no bytes have been removed.  
* *filename*.py - file run through [pyminifier](https://liftoff.github.io/pyminifier/). This takes out comments and other bytes that aren't needed to run the code. E.g.:  
```
$ pyminifier -o wifimgr.py wifimgr_verbose.py
wifimgr_verbose.py (9271) reduced to 7617 bytes (82.16% of original size)
```
# wemos pinout 
![wemos pinout](https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/_images/board.png)
# Front yard
The front yard uses only one watering valve.  The GPIO pin used is D2 (wemos)= Pin 4 (micropython)
# The back yard
The back yard uses two valves.  The "blue" valve is uses GPIO pin D2 (wemos) = Pin 4 (micropython).  The "green" valve uses GPIO pin D1 = Pin 5 (micropython).