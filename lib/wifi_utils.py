import time, network, ntptime
import config

class Wifi:
    def __init__(self, myDisplay):
        self.thisMachineHasDisplay = config.thisMachineHasDisplay
        self.thisMachineHasConsole = config.thisMachineHasConsole

        self.myDisplay = myDisplay

    def wifiConnect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        ssid = config.ssid
        password = config.password
        wlan.connect(ssid, password)

        line = "Config WiFi"
        if self.thisMachineHasDisplay == True:
            self.myDisplay.showLines([line])

        while not wlan.isconnected():
            line += '.'
            self.myDisplay.showLines([line])
            time.sleep(config.wifiRetrySec)
            pass

        line = "WiFi Connected"
        self.myDisplay.showLines([line])

    def ntpConnect(self):
        ntptime.host = config.ntpserver

        while True:
            try:
                ntptime.settime()
                line = "NTP time synced"
                self.myDisplay.showLines([line])
                time.sleep(config.ntpRetrySec)
                break
            except Exception as e:
                line = "Config NTP..."
                self.myDisplay.showLines([line])
                time.sleep(config.ntpRetrySec)
