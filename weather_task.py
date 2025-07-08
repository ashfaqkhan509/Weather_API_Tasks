import requests
import csv
from datetime import datetime
import matplotlib.pyplot as plt



def fetch_weather_data(lat, lon, start, end):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,wind_speed_10m,soil_temperature_0cm"
        f"&start_date={start}&end_date={end}"
        
    )
    response = requests.get(url)
    return response.json()



def write_csv(data, filename="weather_output.csv"):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Time",
            "Temperature (°C)",
            "Wind Speed (km/h)",
            "Soil Temperature (°C)"
        ])
        for i in range(len(data["time"])):
            writer.writerow([
                data["time"][i],
                data["temperature_2m"][i],
                data["wind_speed_10m"][i],
                data["soil_temperature_0cm"][i]
            ])



def get_avg(values):
    total = sum(v for v in values if v is not None)
    count = sum(1 for v in values if v is not None)
    return total / count if count else None


def get_max(values, dates):
    max_val = max(values)
    index = values.index(max_val)
    return max_val, dates[index]


def get_min(values, dates):
    min_val = min(values)
    index = values.index(min_val)
    return min_val, dates[index]


def plot_graph(dates, values, title, ylabel):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

