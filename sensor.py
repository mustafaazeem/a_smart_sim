"""Simulating sensors used in A smart sim."""

from datetime import timedelta
import logging
import random

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.helpers.event import async_track_time_interval

from .const import DEVICE_INFO

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Create simulated software sensors."""

    _LOGGER.info("Configuration parameters received: %s", config)
    _LOGGER.error("Testing logs for a smart sim loading!")

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
        """Construct a temperature sensor object."""
        self._attr_name = "Simulated Temperature Sensor - MusT"
        self._attr_native_unit_of_measurement = "°C"
        self._attr_state = None
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_unique_id = "MustTemp001"
        self._attr_device_info = DEVICE_INFO

        _LOGGER.info("new %s created %s", self._attr_device_class, self._attr_unique_id)

    @property
    def state(self):
        """Return state of Temperature Sensor."""
        return self._attr_state

    async def async_update(self):
        """Update the state of temp sensor whenever called in Async mode."""

        self._attr_state = round(random.uniform(18.0, 26.0), 1)
        _LOGGER.debug("temperature sensor state updated to %s", self._attr_state)


class SimLightSensor(SensorEntity):
    """Simulator for a smart light sensor."""

    def __init__(self):
        """Construct a Light sensor."""

        self._attr_name = "Simulated Illuminance Sensor - MusT"
        self._attr_native_unit_of_measurement = "lx"
        self._attr_state = None
        self._attr_device_class = SensorDeviceClass.ILLUMINANCE
        self._attr_unique_id = "MustLight001"
        self._attr_device_info = DEVICE_INFO
        _LOGGER.info("new %s created %s", self._attr_device_class, self._attr_unique_id)

    @property
    def state(self):
        """Return the current state of the sensor."""
        return self._attr_state

    async def async_update(self):
        """Update the state of sensor whenever called in Async mode."""
        self._attr_state = random.randint(100, 1000)
        _LOGGER.debug("Light sensor state changed to %s", self._attr_state)


class SimPresenceSensor(BinarySensorEntity):
    """Simulating a software based Presence Sensor."""

    def __init__(self):
        """Constructing a binary presence sensor."""
        self._attr_name = "Simulated Presence Sensor - MusT"
        self._attr_is_on = False
        self._attr_device_class = BinarySensorDeviceClass.PRESENCE
        self._attr_unique_id = "MustPresence001"
        self._attr_device_info = DEVICE_INFO
        _LOGGER.info("new %s created %s", self._attr_device_class, self._attr_unique_id)

    @property
    def is_on(self):
        """Return the current state of the sensor."""
        return self._attr_is_on

    async def async_update(self):
        """Update the state of sensor whenever called in Async mode."""
        self._attr_is_on = random.choice([True, False])
        _LOGGER.debug("Presence sensor state changed to %s", self._attr_is_on)


class SimMotionSensor(BinarySensorEntity):
    """Simulating a motion sensor."""

    def __init__(self):
        """Constructing a binary motion detection sensor."""
        self._attr_name = "Simulated Motion Detection Sensor - MusT"
        self._attr_is_on = False
        self._attr_device_class = BinarySensorDeviceClass.MOTION
        self._attr_unique_id = "MustMotion001"
        self._attr_device_info = DEVICE_INFO
        _LOGGER.info("new %s created %s", self._attr_device_class, self._attr_unique_id)

    @property
    def is_on(self):
        """Return the current state of the sensor."""
        return self._attr_is_on

    async def async_update(self):
        """Update the state of sensor whenever called in Async mode."""
        self._attr_is_on = random.choice([True, False])
        _LOGGER.debug("motion sensor state changed to %s", self._attr_is_on)
