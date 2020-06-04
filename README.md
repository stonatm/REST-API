
# REST API
Short &amp; simple micropython scripts

## blynk.py


Access to Blynk service via REST API


```
function init( token )
```
Store authorization token to use with others functions.

parameters:

**token** - authorization token.

```
function write_pin( pin, value )
```
Write a value to pin.

parameters:

**pin** - pin name (must be string like *"V0"*, *"V1"*).

**value** - a value to be writen to pin.

```
function read_pin( pin )

```
Read a pin value.

parameters:

**pin** - pin name to read

Function return pin value or string with error description if any occur.

```
function notify( message )
```

Sends a notification to android blynk app with given message.

```
function is_app_connected()
```
Function check if android app is connected with blynk service.

Function returns strings "true" or "false" (they are not boolean logical values)

Example:
```
from blynk import blynk
blynk.init("YOUR_AUTH_TOKEN")

blynk.write_pin("V0", 12.5)
blynk.notify("test message")

if blynk.is_app_connected() == "true":
  print("app online")

```

## adafruit.py

Access to adafruit.io service via REST API

```
