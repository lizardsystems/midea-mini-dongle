
# Flash dongle with ESPHome firmware

## Firmware

You may create your own firmaware or download ready to use firmware.

### Create your own firmware

Please read [Getting Started with ESPHome](https://esphome.io/guides/getting_started_command_line.html) and [Getting Started with ESPHome and Home Assistant](https://esphome.io/guides/getting_started_hassio.html)

Compile the firmware.

### Download ready to use firmware

Download firmware [midea_ac.bin](midea_ac.bin) from this repository.

## Connect dongle to computer


## Flash dongle with compiled firmware

### First time flashing 

Download flasher https://github.com/esphome/esphome-flasher/releases

Open the flasher tool
 - Serial port: select COM port where the dongle is connected (there is probably only one option).
 - Firmware: Browse to the location where you downloaded your compiled firmware and select your firmware.
 
![image](https://user-images.githubusercontent.com/4923679/124561924-16b5f580-de47-11eb-88de-41583f74d1a0.png)

Click Flash ESP and wait

The dongle will be flashed now, you can follow the progress in the console window. 

When finished writing the firmware the ESP switch off dongle

### Flashing Over-The-Air (OTA)

You may upload a new firmare over the air using commnad line [command line](https://esphome.io/guides/cli.html?highlight=command%20line#upload-command) or upload via web interface.

For uploading firmware via web interface, open the dongle address (IP ro DNS) in web browser.  Select a new firmware file and click the Update button

![image](https://user-images.githubusercontent.com/4923679/124578267-b929a500-de56-11eb-9241-e5beb5762944.png)


## Connecting dongle to Wi-Fi network

![image](https://user-images.githubusercontent.com/4923679/124567170-6fd45800-de4c-11eb-99d1-a14ab3e08ae6.png)

![image](https://user-images.githubusercontent.com/4923679/124567285-87abdc00-de4c-11eb-9a4b-9f6d1bf76c4f.png)

Type password for Fallback Hotspot. Default: midea_ac_1234!@#$

When you connect to the fallback network, the web interface should open automatically (see also login to network notifications). If that does not work, you can also navigate to http://192.168.4.1/ manually in your browser.

![image](https://user-images.githubusercontent.com/4923679/124567130-61863c00-de4c-11eb-86be-49ea9a270f94.png)

In this web interface, you can manually override the WiFi settings.

Additionally, you can upload a new firmware file.

## See also
 - https://esphome.io/guides/getting_started_hassio.html
