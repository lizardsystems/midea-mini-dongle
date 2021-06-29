# Midea mini dongle

![Midea mini dongle](images/dongle_with_case_preview.jpg)

This is the Midea mini dongle - USB stick for air conditioners controlled by the Midea UART protocol.

This repository contains a schematic and PCB layout for a Midea mini dongle.

### Some credits before start

Thanks to [Sergey V. Dudanov](https://github.com/dudanov) who created an excelent [midea_ac](https://esphome.io/components/climate/midea_ac.html) component for ESPHome that integrates midea-like aircondititioners with Home Assistant.

Schematics are based on manufacturers datasheets but some component values come from [Adafruit Learning System](https://learn.adafruit.com/) so thanks to Adafruit for keeping their products open source.

## Idea

Small dongle with minimum components and fully assembled by PCB manufacturing service in standard case.

## Schematic

This is the schematic of Midea mini dongle

![Schematic](images/Schematic_midea-mini-dongle.png)

Download pdf file [Schematic_midea-mini-dongle.pdf](Schematic_midea-mini-dongle.pdf)
## PCB 

Dimensions: 
 - Width x Height: 44x20mm
 - USB connector: +15mm 
 - Overall: 59x20mm
 - Thickness: 0.8mm

### 2D View
![2D View](images/pcb-midea-mini-dongle-2d.png)

### 3D View
![3D View](images/pcb-midea-mini-dongle-3d.png)

### Case

PCB is designed for [Gainta G1901 case](datasheets/case.pdf)

## Ordering and manufacturing

 - Gerber files: [Gerber_pcb-midea-mini-dongle-v1.3_2021-05-14.zip](jlcpcb/Gerber_pcb-midea-mini-dongle-v1.3_2021-05-14.zip)
 - BOM file: [BOM_pcb-midea-mini-dongle-v1.3_2021-05-14.csv](jlcpcb/BOM_pcb-midea-mini-dongle-v1.3_2021-05-14.csv)
 - CPL file: [PickAndPlace_pcb-midea-mini-dongle-v1.3_2021-05-14.csv](jlcpcb/PickAndPlace_pcb-midea-mini-dongle-v1.3_2021-05-14.csv)

When ordering fully assembled (with ESP-12F and USB port) 10 pieces on [JLCPCB site](https://jlcpcb.com/), the price per piece was  $5 USD (2021-05-15) 

![JLCPCB Order](images/jlcpcb_order.png)

## Hardware

## Firmware

You may use [simple config](esphome/simple.yaml) or write your own following by instructions on the ESPHome website.

### Flashing
Please read flashing manual

## Resources
 - [midea_ac component for ESPHome](https://esphome.io/components/climate/midea_ac.html) 
 - [midea-open-dongle](https://github.com/dudanov/midea-open-dongle)
 - [Midea HVAC WiFi Dongle](https://github.com/reneklootwijk/mideahvac-dongle)
