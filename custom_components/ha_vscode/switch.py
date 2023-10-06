from .vscode_device import VSCodeDeviceAPI
from homeassistant.const import UnitOfInformation
from homeassistant.components.switch import (
    SwitchEntity,
    SwitchDeviceClass,
)
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


async def async_setup_entry(hass, config, async_add_devices):
    # Run setup via Storage
    dev_url = config.data["dev_url"]
    path = config.data["path"]
    async_add_devices([VSCodeEntity(path, dev_url)])


class VSCodeEntity(SwitchEntity):
    _attr_name = "Development URL"
    _attr_native_unit_of_measurement = UnitOfInformation
    _attr_device_class = SwitchDeviceClass.SWITCH

    def __init__(self, bin_dir, dev_url):
        self.device = VSCodeDeviceAPI(bin_dir)
        self._attr_name = "VSCode Tunnel: " + dev_url

    def turn_on(self, **kwargs) -> None:
        """Turn the entity on."""
        self.device.startTunnel()

    def turn_off(self, **kwargs):
        """Turn the entity off."""
        self.device.stopTunnel()

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self.device.isRunning()
