'''All constants that are used in this smart sim.'''

from homeassistant.helpers.device_registry import DeviceInfo

DOMAIN = "a_smart_sim"

DEVICE_INFO = DeviceInfo(
    identifiers={("a_smart_Sim", "simulation device")},
    name="A Smart Simulation by MusT",
    manufacturer="Mustafa",
    model="simulation device",
    serial_number="0.1"
    )
