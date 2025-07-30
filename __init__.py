"""Intialize the platform, register entites in Async mode."""
import logging 

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform 
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
PLATFORMS: list[Platform] = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    '''Sets up a_smart_sim from a config entry.'''
    _LOGGER.info("Setting up a_smart_Sim integration with entry %s", entry.title)

    # Store config entry data. 
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data 

    # Forward the stored data to be setup by the sensor platform.
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    '''Unload a config entry specified in entry variable.'''
    _LOGGER.info("Unload a_smart_sim config entry with id %s", entry.title)

    # Unload platform.
    if unload.ok := await hass.config_entries.async_unload_platform(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok







# async def async_setup(hass, config):
#     """Setup platform in async mode."""

#     hass.data[DOMAIN] = {}

#     hass.components.logger.info("A Smart SIM is loaded.")

#     return True
