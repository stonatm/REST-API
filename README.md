
# REST API
Short &amp; simple micropython scripts

## blynk.py ![blynk.png](blynk.png)


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

parameters:

**message** - message text to send

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

## adafruit.py ![adafruit.png](adafruit.png)

Access to adafruit.io service via REST API

```
function init( username, aio )
```

Initialize library with username and adafruit AIO key.

parameters:

**username** - your adafruit.io username.

**aio** - your adafruit.io AIO access key.


```
function write_feed( feed_name, value )
```
Write a value to feed

parameters:

**feed_name** - your adafruit feed name.

**value** - value to sent to given feed

```
function read_feed(feed_name)
```

Read last stored value from given feed.

parameters:

**feed_name** - your adafruit feed name.

Example:

```
from adafruit import adafruit
adafruit.init('ADAFRUIT_USERNAME', 'YOUR_AIO_KEY')

adafruit.write_feed('FEED_NAME', 23.5)
print( adafruit.read_feed('FEED_NAME') )
```

## tspeak.py ![tspeak.png](tspeak.png)

Access to thingspeak service via REST API

```
function init( channel_id, read_key, write_key )
```

Initialize library with your channel id number and access keys.

parameters:

**channel_id** - your thingspeak channel id number

**read_key** - your thingspeak read access key

**write_key** - your thingspeak write access key

```
function write_channel( channel_number, value )
```

Write a value to thingspeak given channel number.

parameters:

**channel_number** - channel number (1-8)

**value** - a value to write to given channel number

Function returns a three type of value:

- **-1** when errors occur.

- **0** when data was rejected due to sending more than once every 15 seconds.

- **integer number** when data was stored. This is the next *entry id* of the message sent to channel.


```
function read_channel( channel_number )
```

Read last stored value from given channel number.

parameters:

**channel_number** - channel number (1-8)

If any error occurs function return a **-1** value.

Example:

```
from tspeak import tspeak
tspeak.init( 'CHANNEL_ID_NUMBER', 'READ_KEY', 'WRITE_KEY' )

tspeak.write_channel( 1, 123.5)
# wait 15 seconds before sending next data to the next channels
print( tspeak.read_channel(1) )
```
