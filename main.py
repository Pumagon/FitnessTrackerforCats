import time
import wifi_utils, accel_utils, display_utils, message_utils
import kintone, config

def main():
    # BMI160 Settings
    myActivity = accel_utils.Accelerometer(config.i2cChannel, config.sda, config.scl)
    
    # Display Settings
    if config.thisMachineHasDisplay == True:
        myDisplay = display_utils.Display(config.i2cChannel, config.sda, config.scl)
    else:
        myDisplay = None

    myMessage = message_utils.Message(myDisplay)
    
    # Kintone Settings
    sdomain = config.sdomain
    appId = config.appId
    token = config.token
     
    timezone_offset = config.timezone_offset_pdt

    myWifi = wifi_utils.Wifi(myDisplay)
    myWifi.wifiConnect()
    myWifi.ntpConnect()

    sumActivityValue = 0
    previousTime = time.time() + timezone_offset
    previousActivityValue = 0
    while True:
        activityValue = myActivity.calculateActivity()

        # Determin the threashold whether you are moving or not
        if activityValue >= config.activityThreshold:
            sumActivityValue += activityValue

        localTime = time.time() + timezone_offset

        lines = ["actValue:",
                 str(activityValue),
                 "sumActValue:",
                 str(sumActivityValue)]

        myMessage.showLines(lines)

        if localTime - previousTime >= 60:
            previousTime = localTime
            payload = {"app": appId,
                        "record": {"activity": {"value": sumActivityValue} }}

            recordId = kintone.uploadRecord(subDomain=sdomain,
                                            apiToken=token,
                                            record=payload)
            sumActivityValue = 0
            
        time.sleep(0.1)


if __name__ == "__main__":
    main()
