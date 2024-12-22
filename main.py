import praytimes
from datetime import datetime

# Set your location (latitude, longitude) and timezone
latitude =int( input("Enter value  of latitude:"))  # Example: Dhaka, Bangladesh
longitude =int(input("Enter value of longitude:"))
timezone = int(input("Enter value of timezone:")) # GMT+6 for Bangladesh Standard Time

# Create a PrayTimes object
pt = praytimes.PrayTimes()

# Get today's date
today = datetime.now().date()

# Calculate prayer times for today
prayer_times = pt.get_times(today, (latitude, longitude), timezone)

# Display the prayer times
print("Salah Times for Today:")
print(f"Fajr: {prayer_times['fajr']}")
print(f"Dhuhr: {prayer_times['dhuhr']}")
print(f"Asr: {prayer_times['asr']}")
print(f"Maghrib: {prayer_times['maghrib']}")
print(f"Isha: {prayer_times['isha']}")
