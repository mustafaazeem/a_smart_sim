"""Config Flow for a_smat_sim."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.schema (
    {
        vol.Required("name", default = "Mustafa"): str,
        vol.Required("update_interval", default = 10): int
    }
)


class ASmartSimConfigFlow(ConfigFlow, domain=DOMAIN):
    """Create a configuration flow for a_smart_sim."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial setup via user-step."""

        if user_input is None:
            '''Show form with name and update_interval fields on first visit.'''
            return self.async_show_form(step_id="user", data_schema=STEP_USER_DATA_SCHEMA)

        # User submitted a form, Create config entry with user submitted data. 
        return self.async_create_entry(title="a_smart_sim", data=user_input)