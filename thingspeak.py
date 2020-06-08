# (c) stonatm@gmail.com
# Thingspeak access via REST API

# GET https://api.thingspeak.com/update?api_key=C9Y5UYPY6IRW7W4I&field1=0

# GET https://api.thingspeak.com/channels/566284/feeds.json?results=2

#read channel
#GET
query = api_key 4D36BGV6L5JHA7VG
header = content-type application/json
https://api.thingspeak.com/channels/566284/fields/1.json?results=1
                                    \channel_id   \              \
                                                   \channel no    \
                                                                   \no of last entries
response:
{
  "channel": {
    "id": 566284,
    "name": "test-chan",
    "description": "test",
    "latitude": "0.0",
    "longitude": "0.0",
    "field1": "node0.temp",
    "field2": "node1.temp",
    "field3": "Field Label 3",
    "created_at": "2018-08-30T14:04:35Z",
    "updated_at": "2018-11-05T10:08:58Z",
    "last_entry_id": 1293218
  },
  "feeds": [
    {
      "created_at": "2020-06-01T11:11:45Z",
      "entry_id": 1293218,
      "field1": "255"
    }
  ]
}


#write channel
#GET
https://api.thingspeak.com/update?api_key=C9Y5UYPY6IRW7W4I&field1=255