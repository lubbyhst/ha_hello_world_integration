import requests
from homeassistant.components.sensor import SensorEntity
from const import CONF_API_URL, CONF_NAME
from . import DOMAIN

DOMAIN = DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Hello World sensor based on a config entry."""
    name = config_entry.data.get(CONF_NAME)
    api_url = config_entry.data.get(CONF_API_URL)

    async_add_entities([HelloWorldSensor(name, api_url)], True)

class HelloWorldSensor(SensorEntity):
    """Representation of a Hello World Sensor."""

    def __init__(self, name, api_url):
        """Initialize the sensor."""
        self._name = name
        self._api_url = api_url
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get(self._api_url)
            response.raise_for_status()
            data = response.json()
            self._state = data.get("message", "No message")
        except requests.RequestException:
            self._state = "Error"
