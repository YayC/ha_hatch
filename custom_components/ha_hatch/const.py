from enum import Enum

# Configuration Constants
DOMAIN: str = "ha_hatch"

# Integration Setting Constants
CONFIG_FLOW_VERSION: int = 2
PLATFORMS = ["media_player", "light", "binary_sensor", "sensor"]

# Home Assistant Data Storage Constants
DATA_MQTT_CONNECTION: str = "mqtt_connection"
DATA_REST_DEVICES: str = "rest_devices"
DATA_MEDIA_PlAYERS: str = "media_players"
DATA_LIGHTS: str = "lights"
DATA_BINARY_SENSORS: str = "binary_sensors"
DATA_SENSORS: str = "sensors"
DATA_EXPIRATION_LISTENER: str = "expiration_listener"
