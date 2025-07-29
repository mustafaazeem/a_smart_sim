'''Config Flow for a_smat_sim.'''
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class ASmartSimConfigFlow(ConfigFlow, domain=DOMAIN):
    '''Create a configuration flow for a_smart_sim.'''

    VERSION = 1

    async def async_step_user(self, user_input=None):
        '''Handle the initial setup via user-step.'''
        
        if user_input is None:
            '''If user just visited first time, there is no input, send default form then.'''
            return self.async_show_form(step_id='user')
        
        return self.async_create_entry(title= 'a_smart_sim', data=user_input)
        

