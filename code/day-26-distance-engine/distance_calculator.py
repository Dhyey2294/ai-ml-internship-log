from math import radians, sin, cos, sqrt, atan2

# Haversine Distance Formula (Accurate Earth Distance)
def calculate_distance_km(lat1, lon1, lat2, lon2):
    try:
        R = 6371  # Earth radius in km

        lat1 = float(lat1)
        lon1 = float(lon1)
        lat2 = float(lat2)
        lon2 = float(lon2)

        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)

        a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return round(R * c, 2)

    except:
        return 0

# Estimate Travel Time
def estimate_travel_time_minutes(distance_km, avg_speed_kmph=30):
    try:
        return round((distance_km / avg_speed_kmph) * 60)
    except:
        return 0


# Estimate Taxi Fare Range
def estimate_taxi_fare_range(distance_km, min_rate=15, max_rate=20):
    try:
        min_fare = round(distance_km * min_rate)
        max_fare = round(distance_km * max_rate)
        return f"₹{min_fare} – ₹{max_fare}"
    except:
        return "₹0 – ₹0"


# Calculate Day-wise Distances
def calculate_daily_distances(itinerary):

    daily_distances = {}
    segment_distances = {}
    segment_times = {}

    for day in itinerary:

        day_number = day.get("day")
        activities = day.get("activities", [])

        total_distance = 0
        day_segments = []
        day_times = []

        for i in range(len(activities) - 1):

            a1 = activities[i]
            a2 = activities[i + 1]

            distance = calculate_distance_km(
                a1.get("latitude"),
                a1.get("longitude"),
                a2.get("latitude"),
                a2.get("longitude")
            )

            total_distance += distance
            day_segments.append(distance)

            travel_time = estimate_travel_time_minutes(distance)
            day_times.append(travel_time)

        daily_distances[day_number] = round(total_distance, 2)
        segment_distances[day_number] = day_segments
        segment_times[day_number] = day_times

    return daily_distances, None, segment_distances, segment_times
