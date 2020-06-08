# (c) stonatm@gmail.com
# thingspeak access via REST API
class tspeak:
  import json
  import urequests

  CHANNEL_ID = 0
  READ_KEY = ''
  WRITE_KEY = ''
  initialise = False

  #init with access keys and channel id
  def init(channel_id, read_key, write_key):
    tspeak.CHANNEL_ID = channel_id
    tspeak.READ_KEY = read_key
    tspeak.WRITE_KEY = write_key
    tspeak.initialise = True

  #read channel last stored data
  def read_channel(channel_number):
    if not tspeak.initialise:
      return
    headers = {'Content-Type':'application/json'}
    query = {"api_key":tspeak.READ_KEY}
    values = tspeak.json.dumps(query)
    url = 'http://api.thingspeak.com/channels/' + str(tspeak.CHANNEL_ID) + '/fields/' + str(channel_number) + '/last.json'
    response = tspeak.urequests.get(url, data = values, headers = headers)
    table = tspeak.json.loads(response.text)
    if not (table == -1):
      return(table["field"+str(channel_number)])
    else:
      return(response.text)

  #write data to channel
  def write_channel(channel_number, value):
    if not tspeak.initialise:
      return
    headers = {'Content-Type':'application/json','Connection':'close'}
    url = 'http://api.thingspeak.com/update?api_key=' + tspeak.WRITE_KEY + '&field' + str(channel_number) + '=' + str(value)
    response = tspeak.urequests.post( url, headers = headers)
    return (response.text)

