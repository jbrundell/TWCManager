# Tesla Powerwall 2

class TeslaPowerwall2:

  import requests
  import time

  cacheTime   = 60
  consumedW   = 0
  debugLevel  = 0
  fetchFailed = False
  generatedW  = 0
  importW     = 0
  exportW     = 0
  lastFetch   = 0
  serverIP    = None
  serverPort  = 80
  status      = False
  timeout     = 10
  voltage     = 0

  def __init__(self, debugLevel, config):
    self.debugLevel  = debugLevel
    self.status      = config.get('enabled', False)
    self.serverIP    = config.get('serverIP', None)
    self.serverPort  = config.get('serverPort','80')

  def debugLog(self, minlevel, message):
    if (self.debugLevel >= minlevel):
      print("Powerwall2: (" + str(minlevel) + ") " + message)

  def getConsumption(self):

    if (not self.status):
      self.debugLog(10, "Powerwall2 EMS Module Disabled. Skipping getConsumption")
      return 0

    # Perform updates if necessary
    self.update()

    # I don't believe this is implemented
    return float(0)

  def getGeneration(self):

    if (not self.status):
      self.debugLog(10, "Powerwall2 EMS Module Disabled. Skipping getGeneration")
      return 0

    # Perform updates if necessary
    self.update()

    # Return generation value
    return float(self.generatedW)

  def getTEDValue(self, url):

    # Fetch the specified URL from TED and return the data
    self.fetchFailed = False

    try:
        r = self.requests.get(url, timeout=self.timeout)
    except self.requests.exceptions.ConnectionError as e:
        self.debugLog(4, "Error connecting to Tesla Powerwall 2 to fetch solar data")
        self.debugLog(10, str(e))
        self.fetchFailed = True
        return False

    r.raise_for_status()
    return r

  def update(self):

    if ((int(self.time.time()) - self.lastFetch) > self.cacheTime):
      # Cache has expired. Fetch values from Powerwall.

      url = "http://" + self.serverIP + ":" + self.serverPort
      url = url + "/history/export.csv?T=1&D=0&M=1&C=1"

      value = self.getTEDValue(url)
      m = None
      if (value):
        m = self.re.search(b'^Solar,[^,]+,-?([^, ]+),', value, self.re.MULTILINE)
      else:
        self.debugLog(5, "Failed to find value in response from TED")
        self.fetchFailed = True

      if(m):
        self.generatedW = int(float(m.group(1)) * 1000)

      # Update last fetch time
      if (self.fetchFailed is not True):
        self.lastFetch = int(self.time.time())

      return True
    else:
      # Cache time has not elapsed since last fetch, serve from cache.
      return False
