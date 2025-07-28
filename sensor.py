"""Simulating sensors used in A smart sim."""

from datetime import timedelta
import logging
import random

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_time_interval

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Create simulated software sensors."""

    SimSensors = [
        SimTempSensor(),
        SimLightSensor(),
        SimPresenceSensor(),
        SimMotionSensor(),
    ]
    async_add_entities(SimSensors)

    async def update_sensors(now):
        for sensor in SimSensors:
            sensor.async_schedule_update_ha_state(True)

    async_track_time_interval(hass, update_sensors, timedelta(seconds=10))


class SimTempSensor(SensorEntity):
    """Simulator for a temp sensor."""

    def __init__(self):
        """Construct a temprature sensor object."""
        self._attr_name = "Simulated Temprature Sensor - MusT"
        self._attr_native_unit_of_measurement = "°C"
        self._attr_state = None
        self._attr_device_class = "temprature"
        self._attr_unique_id = "MustTemp001"

    @property
    def state(self):
        return self._attr_state

    async def async_update(self):
        """Update the state of temp sensor whenever called in Async mode."""

        self._attr_state = round(random.uniform(18.0, 26.0), 1)
        _LOGGER.debug("temprature sensor state updated to {self._attr_state}")


class SimLightSensor(SensorEntity):
    """Simulator for a smart light sensor."""

    def __init__(self):
        """Construct a Light sensor."""

        self._attr_name = "Simulated Ambient Light Sensor - MusT"
        self._attr_native_unit_of_measurement = "lx"
        self._attr_state = None
        self._attr_device_class = "light"
        self._attr_unique_id = "MustLight001"
        _LOGGER.info(
            "new {self._Attr_device_class} light sensor created {self._Attr_unique_id}"
        )

    @property
    def state(self):
        """Return the current state of the sensor."""
        return self._attr_state

    async def async_update(self):
        """Update the state of sensor whenever called in Async mode."""
        self._attr_state = random.randint(100, 1000)
        _LOGGER.debug("Light sensor state changed to {self._attr_state}")


class SimPresenceSensor(BinarySensorEntity):
    """Simulating a software based Presense Sensor."""

    def __init__(self):
        """Constructin a binary presence sensor."""
        self._attr_name = "Simulated Presense Sensor - MusT"
        self._attr_is_on = False
        self._attr_device_class = "presence"
        self._attr_unique_id = "MustPresence001"
        _LOGGER.info("new {self._attr_device_class} created {self._attr_unique_id}")

    @property
    def is_on(self):
        """Return the current state of the sensor."""
        return self._attr_is_on

    async def async_update(self):
        """Update the state of sensor whenever called in Async mode."""
        self._attr_is_on = random.choice([True, False])
        _LOGGER.debug("Presence sensor state changed to {self._attr_is_on}")


class SimMotionSensor(BinarySensorEntity):
    """Simulating a motion sensor."""

    def __init__(self):
        """Constructing a binary motion detection sensor."""
        self._attr_name = "Simulated Motion Detection Sensor - MusT"
        self._attr_is_on = False
        self._attr_device_class = "motion"
        self._attr_unique_id = "MustMotion001"
        _LOGGER.info("new {self._attr_device_class} created {self._Attr_unique_id}")

    @property
    def is_on(self):
        """Return the current state of the sensor."""
        return self._attr_is_on

    async def async_update(self):
        """Update the state of sensor whenever called in Async mode."""
        self._attr_is_on = random.choice([True, False])
        _LOGGER.debug("motion sensor state changed to {self_attr_is_on}")
