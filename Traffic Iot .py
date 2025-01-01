import time
import random
import requests
from datetime import datetime
import math

# Constants
EXPECTED_TIME = 30  # in minutes
SERVER_URL = "http://trafficpolice-server.com/report"

# Simulated GPS Data (Lat, Long) for testing
def get_simulated_gps_data():
    # Simulate GPS coordinates (latitude: 23.7 to 23.8, longitude: 90.3 to 90.4)
    lat = random.uniform(23.7, 23.8)  # Simulated latitude
    lon = random.uniform(90.3, 90.4)  # Simulated longitude
    return lat, lon

# Camera Placeholder for Testing (You can simulate detection here)
def detect_bus(frame):
    # Simulate bus detection by randomly deciding if a bus is detected
    return random.choice([True, False])

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance

def main():
    start_time = None
    end_time = None

    while True:
        # Simulate frame capture (you can replace this with real camera capture in production)
        frame = None  # Here you would normally call cv2.VideoCapture(0).read()

        # Simulate bus detection
        if detect_bus(frame):
            if start_time is None:
                start_time = time.time()  # Record the real start time
                start_lat, start_lon = get_simulated_gps_data()
                start_timestamp = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Bus started at: {start_lat}, {start_lon} at {start_timestamp}")
            else:
                end_time = time.time()  # Record the real stop time
                end_lat, end_lon = get_simulated_gps_data()
                end_timestamp = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Bus stopped at: {end_lat}, {end_lon} at {end_timestamp}")

                # Calculate the journey time in minutes
                journey_time = (end_time - start_time) / 60  # in minutes

                # Calculate the distance traveled
                distance = haversine(start_lat, start_lon, end_lat, end_lon)
                print(f"Distance traveled: {distance:.2f} km")

                # Prepare data for the server
                data = {
                    "bus_id": "123",
                    "start_time": start_timestamp,
                    "end_time": end_timestamp,
                    "journey_time": journey_time,
                    "status": "Delayed" if journey_time > EXPECTED_TIME else "On Time",
                    "distance": distance,
                    "start_location": {"lat": start_lat, "lon": start_lon},
                    "end_location": {"lat": end_lat, "lon": end_lon}
                }

                # Simulate sending data to the server
                try:
                    response = requests.post(SERVER_URL, json=data)
                    print("Data sent:", response.status_code)
                except requests.exceptions.RequestException as e:
                    print(f"Error sending data: {e}")

                # Reset for next detection
                start_time = None
                end_time = None
        
        time.sleep(1)  # Simulate waiting for the next detection cycle

if __name__ == "__main__":
    main()
