"""My first integration."""

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)
DOMAIN = "my_first_integration"

# This is the new line that fixes the hassfest config_schema error
CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


# The function signature is updated to add type hints, fixing the pylint errors
def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration."""
    # The period at the end of the message is removed
    _LOGGER.info("Hello from My First Integration! It has been set up")
    # Return True to indicate setup was successful
    return True
