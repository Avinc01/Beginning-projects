from zoneinfo import ZoneInfo
from datetime import datetime


while True:

    print("\n==============Time Zone Converter==============")
    print("Common zones are: America/New_York, America/Chicago, America/Los_Angeles, Europe/London, Asia/Tokyo")

    from_zone_name = input("\nInput source time zone: ")
    to_zone_name = input("Input the zone to convert to: ")
    current_time = input("Enter the 24h time (HH:MM): ")

    hours, minutes = map(int, current_time.split(':'))
    from_zone = ZoneInfo(from_zone_name)
    to_zone = ZoneInfo(to_zone_name)

    now = datetime.now()
    naive = datetime(now.year, now.month, now.day, hours, minutes)

    from_time = naive.replace(tzinfo = from_zone)
    to_time = from_time.astimezone(to_zone)

    print(f"\nOriginal: {from_time.strftime('%I:%M %p %Z')}")
    print(f"Converted: {to_time.strftime('%I:%M %p %Z')}")