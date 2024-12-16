import machine
import onewire
import ds18x20
import time

sensor_pin = machine.Pin(4)
ow = onewire.OneWire(sensor_pin)
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

if not roms:
    raise Exception("No DS18B20 sensors found!")

def get_temperature():
    ds.convert_temp()
    time.sleep(1)
    return ds.read_temp(roms[0])
