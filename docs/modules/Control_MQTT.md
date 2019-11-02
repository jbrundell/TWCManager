# MQTT Control Module

## Introduction

The MQTT Control Module allows control over the TWCManager Tesla Wall Charger controller using MQTT topics. By publishing commands via MQTT, the behaviour of the charger (such as charger timing and mode) can be controlled.

### Status

| Detail          | Value          |
| --------------- | -------------- |
| **Module Name** | MQTTControl    |
| **Module Type** | Status         |
| **Status**      | In Development |

## Configuration

The following table shows the available configuration parameters for the MQTT Control module.

| Parameter   | Value         |
| ----------- | ------------- |
| enabled     | *required* Boolean value, ```true``` or ```false```. Determines whether we will enable MQTT control. |
| brokerIP    | *required* The IP address of the MQTT broker. We subscribe to control topics under this MQTT broker. |
| topicPrefix | *required* MQTT topic prefix for control topics. |
| username    | *optional* Username for connecting to MQTT server (if authentication is required). |
| password    | *optional* Password for connecting to MQTT broker (if authentication is required). |

### JSON Configuration Example

```
"control": {
  "MQTT": {
    "enabled": true,
    "brokerIP": "192.168.1.2",
    "topicPrefix": "TWC",
    "username": "mqttuser",
    "password": "mqttpass"
  }
}
```

## MQTT Topics

| MQTT Topic                       | Value |
| -------------------------------- | ----- |
| *prefix*/all/totalAmpsInUse      | TBA |
| *prefix*/*charger*/ampsInUse     | TBA |
| *prefix*/*charger*/ampsMax       | TBA |
| *prefix*/*charger*/carsCharging  | TBA |
| *prefix*/*charger*/power         | TBA |
| *prefix*/*charger*/state         | TBA |
| *prefix*/config/maxAmpsForSlaves | TBA |
| *prefix*/config/minAmpsPerTWC    | TBA |