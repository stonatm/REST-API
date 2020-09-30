# (c) stonatm@gmail.com
# library to read synoptic data for
# polish cities from imgw.pl

class imgw:
  import urequests
  import json

  data = {"message":"Acquire data first"}
  
  def acquireData(station_id):
    url = 'https://danepubliczne.imgw.pl/api/data/synop/id/' + str(station_id)
    headers={'Content-Type':'text/html'}
    response = imgw.urequests.get(url, headers=headers)
    imgw.data = imgw.json.loads(response.text)
      
  def getStationID():
    if 'id_stacji' in imgw.data:
      return (imgw.data['id_stacji'])
    else:
      return(imgw.data['message'])

  def getStationName():
    if 'stacja' in imgw.data:
      return (imgw.data['stacja'])
    else:
      return(imgw.data['message'])

  def getMeasurementDate():
    if 'data_pomiaru' in imgw.data:
      return (imgw.data['data_pomiaru'])
    else:
      return(imgw.data['message'])

  def getMeasurementTime():
    if 'godzina_pomiaru' in imgw.data:
      return (imgw.data['godzina_pomiaru'])
    else:
      return(imgw.data['message'])

  def getTemperature():
    if 'temperatura' in imgw.data:
      return (imgw.data['temperatura'])
    else:
      return(imgw.data['message'])

  def getWindSpeed():
    if 'predkosc_wiatru' in imgw.data:
      return (imgw.data['predkosc_wiatru'])
    else:
      return(imgw.data['message'])

  def getWindDirection():
    if 'kierunek_wiatru' in imgw.data:
      return (imgw.data['kierunek_wiatru'])
    else:
      return(imgw.data['message'])

  def getRelativeHumidity():
    if 'wilgotnosc_wzgledna' in imgw.data:
      return (imgw.data['wilgotnosc_wzgledna'])
    else:
      return(imgw.data['message'])

  def getTotalRainfall():
    if 'suma_opadu' in imgw.data:
      return (imgw.data['suma_opadu'])
    else:
      return(imgw.data['message'])

  def getPressure():
    if 'cisnienie' in imgw.data:
      return (imgw.data['cisnienie'])
    else:
      return(imgw.data['message'])
