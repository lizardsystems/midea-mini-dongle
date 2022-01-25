call env.cmd
call %ESPHOME_VENV%\Scripts\activate
esphome compile %NODE_ID%.yaml 
python copy_firmware.py