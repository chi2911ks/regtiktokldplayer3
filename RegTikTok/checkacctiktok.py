import os
from time import sleep
from CBAutoHelper import LDPlayer
string = '''{
    "propertySettings.phoneIMEI": "869394026105608",
    "propertySettings.phoneIMSI": "460004118137867",
    "propertySettings.phoneSimSerial": "89860081340017188418",
    "propertySettings.phoneAndroidId": "5f3b72699ab13c7c",
    "propertySettings.phoneModel": "Samsung_E200_ECO",
    "propertySettings.phoneManufacturer": "Samsung",
    "propertySettings.macAddress": "00DB324D4B76",
    "statusSettings.playerName": "otwrmhccsr",
    "basicSettings.verticalSync": false,
    "basicSettings.fsAutoSize": 1,
    "basicSettings.autoRun": false,
    "basicSettings.rootMode": true,
    "statusSettings.closeOption": 0,
    "hotkeySettings.backKey": {
        "modifiers": 0,
        "key": 27
    },
    "hotkeySettings.homeKey": {
        "modifiers": 0,
        "key": 112
    },
    "hotkeySettings.appSwitchKey": {
        "modifiers": 0,
        "key": 113
    },
    "hotkeySettings.menuKey": {
        "modifiers": 0,
        "key": 114
    },
    "hotkeySettings.zoomInKey": {
        "modifiers": 0,
        "key": 115
    },
    "hotkeySettings.zoomOutKey": {
        "modifiers": 0,
        "key": 116
    },
    "hotkeySettings.bossKey": {
        "modifiers": 2,
        "key": 81
    },
    "hotkeySettings.shakeKey": {
        "modifiers": 0,
        "key": 120
    },
    "hotkeySettings.operationRecordKey": {
        "modifiers": 0,
        "key": 121
    },
    "hotkeySettings.fullScreenKey": {
        "modifiers": 0,
        "key": 122
    },
    "hotkeySettings.showMappingKey": {
        "modifiers": 0,
        "key": 123
    },
    "hotkeySettings.videoRecordKey": {
        "modifiers": 0,
        "key": 119
    },
    "hotkeySettings.mappingRecordKey": {
        "modifiers": 0,
        "key": 117
    },
    "hotkeySettings.keyboardModelKey": {
        "modifiers": 2,
        "key": 70
    },
    "basicSettings.heightFrameRate": false,
    "basicSettings.adbDebug": 1,
    "advancedSettings.resolution": {
        "width": 360,
        "height": 600
    },
    "advancedSettings.resolutionDpi": 160,
    "advancedSettings.cpuCount": 2,
    "advancedSettings.memorySize": 4096,
    "propertySettings.phoneNumber": "+84399372757",
    "basicSettings.autoRotate": true,
    "basicSettings.isForceLandscape": false,
    "basicSettings.lockWindow": false,
    "advancedSettings.micphoneName": "Primary Sound Capture Driver",
    "advancedSettings.speakerName": "Primary Sound Driver",
    "networkSettings.networkEnable": true,
    "networkSettings.networkSwitching": false,
    "networkSettings.networkStatic": false,
    "networkSettings.networkAddress": "0.0.0.0",
    "networkSettings.networkGateway": "0.0.0.0",
    "networkSettings.networkSubnetMask": "255.255.255.0",
    "networkSettings.networkDNS1": "8.8.8.8",
    "networkSettings.networkDNS2": "8.8.4.4",
    "networkSettings.networkInterface": "",
    "basicSettings.disableMouseFastOpt": true,
    "basicSettings.cjztdisableMouseFastOpt_new": 0,
    "basicSettings.HDRQuality": 0,
    "basicSettings.qjcjdisableMouseFast": 1,
    "basicSettings.fps": 60,
    "basicSettings.astc": true,
    "statusSettings.sharedApplications": "",
    "statusSettings.sharedPictures": "",
    "statusSettings.sharedMisc": "",
    "basicSettings.left": 335,
    "basicSettings.top": 207,
    "basicSettings.width": 235,
    "basicSettings.height": 392,
    "basicSettings.realHeigh": 430,
    "basicSettings.realWidth": 309,
    "basicSettings.isForstStart": false,
    "basicSettings.mulFsAddSize": 0,
    "basicSettings.mulFsAutoSize": 2/8*9
}'''
ld = LDPlayer()
count = len(ld.GetDevices2())-1
# ld.Create('create')
with open(fr"D:\LDPlayer\LDPlayer3.0\vms\config\leidian{count}.config", 'w') as file:
    file.write(string)
ld.Info('index', str(count))
ld.Start()
