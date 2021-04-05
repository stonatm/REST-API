# (c) stonatm@gmail.com
# micropython pushsafer notification sender

import urequests
import json

DEBUG = False

def send_notification(private_key, device, title, message, sound, vibration, icon ):
  # create rest api request 
  url = 'https://www.pushsafer.com/api'
  url = url + '?k=' + str(private_key) + '&d=' + str(device) + '&t=' + str(title.replace(' ','%20')) + '&m=' + str(message.replace(' ','%20')) +'&s=' +str(sound) + "&v=" + str(vibration) + "&i=" + str(icon)

  # rest api call
  response = urequests.post(url = url)

  # debug
  if DEBUG:
    print('response text:')
    print(response.text)

  # convert response to json
  if 'status' in response.content.decode():
    json_encoded =  json.loads(response.content)
    return json_encoded['status']
  else:
    return 0
