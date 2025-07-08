from arg_parser import ArgParser
from weather_task import (
    fetch_weather_data,
    get_avg, get_max,
    get_min,
    write_csv,
    plot_graph
)


def main():
    args = ArgParser().parse()

    data = fetch_weather_data(
        args.latitude,
        args.longitude,
        args.start,
        args.end
    )
    daily = data["hourly"]
    time = daily["time"]

    task_map = {
        'max_temp': lambda: print("Max Temperature:",max(daily["temperature_2m"])),
        'min_temp': lambda: print("Min Temperature:", min(daily["temperature_2m"])),
        'avg_temp': lambda: print("Average Temperature:", get_avg(daily["temperature_2m"])),

        'max_wind': lambda: print("Max Wind Speed:", max(daily["wind_speed_10m"])),
        'min_wind': lambda: print("Min Wind Speed:", min(daily["wind_speed_10m"])),
        'avg_wind': lambda: print("Average Wind Speed:", get_avg(daily["wind_speed_10m"])),

        'max_soil': lambda: print("Max Soil Temp:", max(daily["soil_temperature_0cm"])),
        'min_soil': lambda: print("Min Soil Temp:", min(daily["soil_temperature_0cm"])),
        'avg_soil': lambda: print("Average Soil Temp:", get_avg(daily["soil_temperature_0cm"])),

        'date_max_temp': lambda: print_date("Max Temp", *get_max(daily["temperature_2m"], time), "°C"),
        'date_min_temp': lambda: print_date("Min Temp", *get_min(daily["temperature_2m"], time), "°C"),

        'date_max_wind': lambda: print_date("Max Wind", *get_max(daily["wind_speed_10m"], time), "km/h"),
        'date_min_wind': lambda: print_date("Min Wind", *get_min(daily["wind_speed_10m"], time), "km/h"),

        'date_max_soil': lambda: print_date("Max Soil Temp", *get_max(daily["soil_temperature_0cm"], time), "°C"),
        'date_min_soil': lambda: print_date("Min Soil Temp", *get_min(daily["soil_temperature_0cm"], time), "°C"),

        'plot_temp': lambda: plot_graph(
            time, daily["temperature_2m"],
            "Average Temperature Over Time", "Temperature (°C)"
        ),
        'plot_wind': lambda: plot_graph(
            time, daily["wind_speed_10m"],
            "Average Wind Speed Over Time", "Wind Speed (km/h)"
        ),
        'plot_soil': lambda: plot_graph(
            time, daily["soil_temperature_0cm"],
            "Average Soil Temperature Over Time", "Soil Temp (°C)"
        ),

        'export_csv': lambda: (write_csv(daily), print("CSV exported as 'weather_output.csv'"))
    }

    def print_date(label, val, date, unit):
        print(f"Date with {label}: {date} ({val} {unit})")

    task = task_map.get(args.task)
    if task:
        task()
    else:
        print(f"Invalid task: {args.task}")


if __name__ == "__main__":
    main()
