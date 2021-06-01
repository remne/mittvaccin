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
