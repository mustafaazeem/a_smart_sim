'''Simulating sensors used in A smart sim.'''

from datetime import timedelta 
import random

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_time_interval


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    '''Create simulated software sensors.'''

    SimSensors = [
        SimTempSensor(),
        SimLightSensor(),
        SimPresenceSensor(),
        SimMotionSensor()
    ]
    async_add_entities(SimSensors)

    async def update_sensors(now):
        for sensor in SimSensors:
            sensor.async_schedule_update_ha_state(True)

    async_track_time_interval(hass, update_sensors, timedelta(seconds=10))




class SimTempSensor(SensorEntity):
    '''Simulator for a temp sensor.'''

    def __init__(self):
        '''Construct a temprature sensor object.'''
        self._attr_name = "Simulated Temprature Sensor - MusT"
        self._attr_native_unit_of_measurement = "°C"
        self._attr_state = None

        @property
        def state(self):
            return self._attr_state

    async def async_update(self):
        '''Update the state of temp sensor whenever called in Async mode.'''

        self._attr_state = round(random.uniform(18.0, 26.0), 1)

class SimLightSensor(SensorEntity):
    '''Simulator for a smart light sensor.'''

    def __init__(self):
        '''Construct a Light sensor.'''

        self._attr_name = "Simulated Ambient Light Sensor - MusT"
        self._attr_native_unit_of_measurement = "lx"
        self._attr_state = None

    @property
    def state(self):
        '''Return the current state of the sensor.'''
        return self._attr_state

    async def async_update(self):
        '''Update the state of sensor whenever called in Async mode.'''
        self._attr_state = random.randint(100, 1000)

class SimPresenceSensor(BinarySensorEntity):
    '''Simulating a software based Presense Sensor.'''

    def __init__(self):
        '''Constructin a binary presence sensor.'''
        self._attr_name = "Simulated Presense Sensor - MusT"
        self._attr_state = False

    @property
    def state(self):
        '''Return the current state of the sensor.'''
        return self._attr_state

    async def async_update(self):
        '''Update the state of sensor whenever called in Async mode.'''
        self._attr_state = random.choice(True, False)

class SimMotionSensor(BinarySensorEntity):
    '''Simulating a motion sensor.'''

    def __init__(self):
        '''Constructing a binary motion detection sensor.'''
        self._attr_name = "Simulated Motion Detection Sensor - MusT"
        self._attr_state = False

    @property
    def state(self):
        '''Return the current state of the sensor.'''
        return self._attr_state

    async def async_update(self):
        '''Update the state of sensor whenever called in Async mode.'''
        self._attr_state = random.choice(True, False)
