import json
import os
import shutil
import argparse

DEVICE_NAME = "midea_ac"
PACKAGE_FILE = os.path.join(".esphome", f"{DEVICE_NAME}.yaml.json")

with open(PACKAGE_FILE, "r") as package:
    data = json.load(package)
    esphome_version = data["esphome_version"]
    firmware_bin_path =  data["firmware_bin_path"]
    fname=f"{DEVICE_NAME}-{esphome_version}.bin" 
    shutil.copy(firmware_bin_path, fname)
    print(f"Copy firmware to {fname}")
    