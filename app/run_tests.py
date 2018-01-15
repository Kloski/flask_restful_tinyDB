# -*- coding: utf-8 -*-
"""
Tests module.

Tests execution.
"""
import serial
from struct import unpack
from app.server.api import db_client

# Buffer size for send/read data
buff_Size = 8
# Open serial port
ser = serial.Serial(port="/dev/arduino", baudrate=115200, timeout=0.1)

# Var just for debugging...
i = 0
max_Itter = 100

# Clear DB
db_client._clear_db()

# Create DB instance of DAC value
db_client.insert_json({'DAC_Power': '0', 'Value': 2048})

while 1:
    # Read Serial line until two delimiters apear
    data = ser.read_until(b'\x7e\x7e', 9)
    # if data length isnt exact size of 8 its garbage
    if(len(data) == buff_Size):
        # Some data mining...
        data = data[:6]
        bus = data[0]
        unit = data[1]
        temp_data = data[2:]
        # Convert hex data into float
        temp = unpack('f', temp_data)[0]
        # If data already exist update else create new
        if len(db_client.find_by_property_contains_value("DAC_Unit", '{0}{1}'.format(
                bus, unit))) > 0:
            db_client.update("DAC_Unit", '{0}{1}'.format(
                bus, unit), {'Temp': '{0:.2f}'.format(temp)})
        else:
            db_client.insert_json({'DAC_Unit': '{0}{1}'.format(
                bus, unit), 'Temp': '{0:.2f}'.format(temp)})
        # Print for debuging...
        print("Bus: {0}; Unit: {1}; Temp: {2:.2f}".format(bus, unit, temp))

    # Write DAC value to Serial Port
    print(db_client.get_all())
    print(db_client.find_by_property_contains_value('DAC_Power', '0'))
    dac_value = db_client.find_by_property_contains_value('DAC_Power', '0')[
        0]['Value']
    buff = bytearray([0x7e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7e])

    if dac_value < 0 or dac_value > 4095:
        # If Dac value is out of range just send zero
        ser.write(buff)
    else:
        # Else send right value
        hex_int = dac_value.to_bytes(4, 'little')
        for i in range(3, 7):
            buff[i] = hex_int[i - 3]
        ser.write(buff)

    # Break after max_Itter... Just for Debugging
    """
    i = i + 1
    if i > max_Itter:
        break
    """
