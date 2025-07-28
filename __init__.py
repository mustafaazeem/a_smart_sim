"""Intialize the platform, register entites in Async mode."""

from .const import DOMAIN


async def async_setup(hass, config):
    """Setup platform in async mode."""

    hass.data[DOMAIN] = {}

    hass.components.logger.info("A Smart SIM is loaded.")

    return True
