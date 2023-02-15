# API ISS Overhead Notifier
Using the API from:
- https://api.sunrise-sunset.org - for the sunset and sunrise times of my location
- http://api.open-notify.org/iss-now - for the current latitude and longitude of the ISS 
By knowing both we can figure out whether the ISS is currently flying over our heads!
If we are in a location close enough to the ISS, and our local time is between the sunset and sunrise time, we get alerted via email
