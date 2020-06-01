# (c) stonatm@gmail.com
# adafruit.io access via REST API
class adafruit:

  import urequests
  import json

  USERNAME = ''
  AIO = ''
  initialise = False

  #set username and aio key to use below function
  def init(username, aio):
    adafruit.USERNAME = username
    adafruit.AIO = aio
    adafruit.initialise = True

  #read feed last value
  def read_feed(feedname):
    if not adafruit.initialise:
      return
    headers = {'Content-Type':'application/json', 'X-AIO-Key': adafruit.AIO}
    url = 'http://io.adafruit.com/api/v2/' + adafruit.USERNAME + '/feeds/' + feedname
    response = adafruit.urequests.get(url, headers = headers)
    table = adafruit.json.loads(response.text)
    if "last_value" in table:
      return (table['last_value'])
    else:
      return(response.text)

  #write value to feed
  def write_feed(feedname, value):
    if not adafruit.initialise:
      return
    headers = {'Content-Type':'application/json', 'X-AIO-Key': adafruit.AIO}
    table = {"datum":{"value":value}}
    values = adafruit.json.dumps(table)
    url = 'http://io.adafruit.com/api/v2/' + adafruit.USERNAME + '/feeds/' + feedname + '/data'
    response = adafruit.urequests.post( url, data = values ,headers = headers)
    return (response.text)
