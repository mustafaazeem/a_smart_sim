"""Intialize the platform, register entites in Async mode."""
import logging 

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform 
from homeassistant.core import HomeAssistant

from .const import DOMAIN


_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]




# async def async_setup(hass, config):
#     """Setup platform in async mode."""

#     hass.data[DOMAIN] = {}

#     hass.components.logger.info("A Smart SIM is loaded.")

#     return True
