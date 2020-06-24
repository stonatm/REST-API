
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

## accuweat.py ![accuweather.png](accuweather.png)

Access to accuweather.com synoptic data via REST API

### How to get your Api Key:
 - create account on https://developer.accuweather.com/user/login
 - after create account and login click "add new app" and get API Key

### How to find city ID for your city:
 - open https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/search
 - fill field **apikey** with your api key and **q** with your city name to search in *Query Parameters* section
 - click **Send this request**

```
function init(apikey, cityid)
```

Initialize the library with Api key and city id number. You must run this function before use other functions from this library.

parameters:

**apikey** - your accuweather.com account apikey

**cityid** - your city id number

```
function refreshData()
```
Get actual synoptic data from accuweather.com and store them to later use by read... functions. In free trial account there is a 50 requests per day limit.

```
readTemperature()
```

Return temperature for your city

```
function readWeatherText()
```

Return text description of weather for your city like **"Sunny"**, **"Cloudy"** etc.

```
function readWeatherIcon()
```

Return only icon number (not icon) according to actual weather in your city.
Icon list: https://developer.accuweather.com/weather-icons

```
function readIsDayTime()
```

Return **True** if in your city is a day time otherwise return **False**

```
function readLocalObserwationDate()
```

Return a local date of obserwation in your city. Return string in format **YYYY-MM-DD**

```
function readLocalObserwationTime()
```

Return a local time of obserwation in your city. Return string in format **HH:MM:SS**

All of read functions return proper data or text description of error if any occur.

### example

```
from accuweat import accuweat
accuweat.init( 'ACCUWEATHER_API_KEY', 265168)

accuweat.refreshData()

print( accuweat.readTemperature() )
print( accuweat.readWeatherText() )
print( accuweat.readWeatherIcon() )
print( accuweat.readIsDayTime() )
print( accuweat.readLocalObserwationTime() )
print( accuweat.readLocalObserwationDate() )
```
