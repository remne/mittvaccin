# mittvaccin Home Assistant Custom Component
Fulkodad custom component sensor till Home Assistant för att se lägsta ålder i Region Östergötland för vaccinationsbokning.

## configuration.yaml

```
sensor:
  - platform: mittvaccin_sensor
```

## lovelace badge example

```
badges:
  - entity: sensor.mitt_vaccin
```

## example automation

```
  - alias: 'Push notis vid vaccination'
    trigger:
      platform: numeric_state
      entity_id: sensor.mitt_vaccin
      below: 40
    action:
      - service: notify.mobile_app_<something>
        data:
          message: "BOKA VACCIN!"
          data:
            channel: Alarm             # creates a new channel called Alarm that you can manage from your device
            importance: high           # set the channel importance to high
            ledColor: red              # make the LED flash red for this notification
            vibrationPattern: "100,30,100,30,100,30,200,30,200,30,200,30,100,30,100,30,100"     # SOS vibration pattern
            persistent: true           # set to persistent
            sticky: true               # make sure it doesn't dismiss if selected
            #clickAction: /lovelace/alarm    # navigate user to the lovelace alarm view
            #icon: /local/alarm.jpg     # relative path to the icon
            color: red                 # set the color of the notification to red
            group: alarm               # the group name to group together notifications
            tag: alarm                 # tag is required in order to remove the persistent
      - service: light.turn_on
        entity_id:
          - light.<your_light_entity>
```
