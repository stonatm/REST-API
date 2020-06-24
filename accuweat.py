# (c) stonatm@gmail.com
# Accuweather access via Rest API
class accuweat:
  import urequests
  import json

  data = {"Message":"Set cityID and apiKey"}

  CITYID = 0
  APIKEY = ''

  def init(apikey, cityid):
    accuweat.APIKEY = str(apikey)
    accuweat.CITYID= cityid

  def refreshData():
    response = accuweat.urequests.get('http://dataservice.accuweather.com/currentconditions/v1/' + str(accuweat.CITYID) + '?apikey=' +str(accuweat.APIKEY))
    accuweat.data = accuweat.json.loads(response.text.replace('[','').replace(']',''))

  def readTemperature():
    if 'Temperature' in accuweat.data:
      return (accuweat.data["Temperature"]["Metric"]["Value"])
    else:
      return (accuweat.data["Message"])

  def readWeatherText():
    if 'WeatherText' in accuweat.data:
      return (accuweat.data["WeatherText"])
    else:
      return (accuweat.data["Message"])

  def readWeatherIcon():
    if 'WeatherIcon' in accuweat.data:
      return (accuweat.data["WeatherIcon"])
    else:
      return (accuweat.data["Message"])

  def readIsDayTime():
    if 'IsDayTime' in accuweat.data:
      return (accuweat.data["IsDayTime"])
    else:
      return (accuweat.data["Message"]) 

  def readLocalObserwationDate():
    if 'LocalObservationDateTime' in accuweat.data:
      return (accuweat.data["LocalObservationDateTime"][0:10])
    else:
      return (accuweat.data["Message"])

  def readLocalObserwationTime():
    if 'LocalObservationDateTime' in accuweat.data:
      return (accuweat.data["LocalObservationDateTime"][11:19])
    else:
      return (accuweat.data["Message"])
