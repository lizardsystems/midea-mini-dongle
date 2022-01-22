call env.cmd
call %ESPHOME_VENV%\Scripts\activate
esphome compile %NODE_ID%.yaml 
xcopy /f /y ".esphome/build/%NODE_NAME%/.pioenvs/%NODE_NAME%/firmware.bin"  "%NODE_ID%.bin"