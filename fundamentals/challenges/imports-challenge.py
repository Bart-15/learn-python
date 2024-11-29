from astral import LocationInfo
from astral.sun import sun
from datetime import date

def dateFormarHHMM(timestamp):
  return timestamp.strftime("%H:%M")

def calculateSunriseSunset(lat, long):
  city = LocationInfo("Pampanga", "Philippines", "Asia/Manila", lat, long)

  # Print location details
  print(f"Location: {city.name}, {city.region}")
  print(f"Timezone: {city.timezone}")
  print(f"Latitude: {city.latitude}, Longitude: {city.longitude}")

  # Calculate sunrise and sunset for today
  s = sun(city.observer, date=date.today())
  print(f"Sunrise: {dateFormarHHMM(s['sunrise'])}")
  print(f"Sunset: {dateFormarHHMM(s['sunset'])}")


calculateSunriseSunset(15.094310, 120.766960)
