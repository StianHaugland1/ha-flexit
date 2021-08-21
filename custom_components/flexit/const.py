"""Constants for the flexit integration."""

from logging import Logger, getLogger
from typing import List

LOGGER: Logger = getLogger(__package__)

DOMAIN = "flexit"

CONF_PLANT = "plant"
CONF_INTERVAL = "update_interval"

DEFAULT_INTERVAL = 30

# API
API_URL: str = f"https://api.climatixic.com"
TOKEN_PATH: str = f"{API_URL}/Token"
PLANTS_PATH: str = f"{API_URL}/Plants"
DATAPOINTS_PATH: str = f"{API_URL}/DataPoints"
FILTER_PATH: str = f"{DATAPOINTS_PATH}/Values?filterId="
API_HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-us",
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Flexit%20GO/2.0.6 CFNetwork/1128.0.1 Darwin/19.6.0",
    "Ocp-Apim-Subscription-Key": "c3fc1f14ce8747588212eda5ae3b439e",
}

BINARY_SENSOR = "binary_sensor"
CLIMATE = "climate"
SENSOR = "sensor"
PLATFORMS: List[str] = [BINARY_SENSOR, CLIMATE, SENSOR]


# Attributes
ATTR_OPERATING_TIME = "operating_time_hours"
ATTR_TIME_TO_CHANGE = "time_to_change_hours"

# Modes
MODE_HOME = "Home"
MODE_AWAY = "Away"
MODE_HIGH = "High"
MODE_COOKER_HOOD = "Cooker hood"

# Paths
HOME_AIR_TEMPERATURE_PATH = ";1!0020007CA000055"
AWAY_AIR_TEMPERATURE_PATH = ";1!0020007C1000055"
ROOM_TEMPERATURE_PATH = ";1!00000004B000055"
MODE_PATH = ";1!013000169000055"
MODE_PUT_PATH = ";1!01300002A000055"
OUTSIDE_AIR_TEMPERATURE_PATH = ";1!000000001000055"
SUPPLY_AIR_TEMPERATURE_PATH = ";1!000000004000055"
EXTRACT_AIR_TEMPERATURE_PATH = ";1!00000003B000055"
EXHAUST_AIR_TEMPERATURE_PATH = ";1!00000000B000055"
HEATER_PATH = ";1!0050001BD000055"
FILTER_OPERATING_TIME_PATH = ";1!00200011D000055"
FILTER_TIME_FOR_EXCHANGE_PATH = ";1!00200011E000055"
APPLICATION_SOFTWARE_VERSION_PATH = ";0!0083FFFFF00000C"
DEVICE_DESCRIPTION_PATH = ";0!0083FFFFF00001C"
MODEL_NAME_PATH = ";0!0083FFFFF000046"
MODEL_INFORMATION_PATH = ";0!0083FFFFF0012DB"
SERIAL_NUMBER_PATH = ";0!0083FFFFF0013EC"
FIRMWARE_REVISION_PATH = ";0!0083FFFFF00002C"
LAST_RESTART_REASON_PATH = ";0!0083FFFFF0000C4"
OFFLINE_ONLINE_PATH = ";0!Online"
SYSTEM_STATUS_PATH = ";0!0083FFFFF000070"
BACNET_MAC_PATH = ";0!108000000001313"
DEVICE_FEATURES_PATH = ";0!0083FFFFF0013F4"

SENSOR_DATA_PATH_LIST: List[str] = [
    MODE_PATH,
    OUTSIDE_AIR_TEMPERATURE_PATH,
    SUPPLY_AIR_TEMPERATURE_PATH,
    EXTRACT_AIR_TEMPERATURE_PATH,
    EXHAUST_AIR_TEMPERATURE_PATH,
    HOME_AIR_TEMPERATURE_PATH,
    AWAY_AIR_TEMPERATURE_PATH,
    ROOM_TEMPERATURE_PATH,
    FILTER_OPERATING_TIME_PATH,
    FILTER_TIME_FOR_EXCHANGE_PATH,
    HEATER_PATH,
]

DEVICE_INFO_PATH_LIST: List[str] = [
    APPLICATION_SOFTWARE_VERSION_PATH,
    DEVICE_DESCRIPTION_PATH,
    MODEL_NAME_PATH,
    MODEL_INFORMATION_PATH,
    SERIAL_NUMBER_PATH,
    FIRMWARE_REVISION_PATH,
    OFFLINE_ONLINE_PATH,
    SYSTEM_STATUS_PATH,
    LAST_RESTART_REASON_PATH,
]