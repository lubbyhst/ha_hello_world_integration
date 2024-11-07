import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

DOMAIN = DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class HelloWorldConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Hello World integration."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Hello World", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_url"): str,
                vol.Optional("name", default="Hello World Sensor"): str,
            }),
        )
