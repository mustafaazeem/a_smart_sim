"""Config Flow for a_smat_sim."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.const import Platform
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

class ASmartSimConfigFlow(ConfigFlow, domain=DOMAIN):
    """Create a configuration flow for a_smart_sim."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial setup via user-step."""

        if user_input is None:
            """If user just visited first time, there is no input, send default form then."""
            return self.async_show_form(step_id="user")

        return self.async_create_entry(title="a_smart_sim", data=user_input)
