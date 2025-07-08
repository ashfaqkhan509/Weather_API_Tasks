from arg_parser import ArgParser
from weather_task import fetch_weather_data, get_avg, get_max, get_min, write_csv, plot_graph


def main():
    args = ArgParser().parse()

    data = fetch_weather_data(args.latitude, args.longitude, args.start, args.end)
    daily = data["hourly"]
    time = daily["time"]

    if args.task == 'max_temp':
        print("Max Temperature:", max(daily["temperature_2m"]))
   
    elif args.task == 'min_temp':
        print("Min Temperature:", min(daily["temperature_2m"]))
    
    elif args.task == 'avg_temp':
        print("Average Temperature:", get_avg(daily["temperature_2m"]))
    
    elif args.task == 'max_wind':
        print("Max Wind Speed:", max(daily["wind_speed_10m"]))
    
    elif args.task == 'min_wind':
        print("Min Wind Speed:", min(daily["wind_speed_10m"]))
    
    elif args.task == 'avg_wind':
        print("Average Wind Speed:", get_avg(daily["wind_speed_10m"]))
    
    elif args.task == 'max_soil':
        print("Max Soil Temp:", max(daily["soil_temperature_0cm"]))
    
    elif args.task == 'min_soil':
        print("Min Soil Temp:", min(daily["soil_temperature_0cm"]))
    
    elif args.task == 'avg_soil':
        print("Average Soil Temp:", get_avg(daily["soil_temperature_0cm"]))
    
    elif args.task == 'date_max_temp':
        val, date = get_max(daily["temperature_2m"], time)
        print(f"Date with Max Temp: {date} ({val}°C)")
    
    elif args.task == 'date_min_temp':
        val, date = get_min(daily["temperature_2m"], time)
        print(f"Date with Min Temp: {date} ({val}°C)")
    
    elif args.task == 'date_max_wind':
        val, date = get_max(daily["wind_speed_10m"], time)
        print(f"Date with Max Wind: {date} ({val} km/h)")
    
    elif args.task == 'date_min_wind':
        val, date = get_min(daily["wind_speed_10m"], time)
        print(f"Date with Min Wind: {date} ({val} km/h)")
    
    elif args.task == 'date_max_soil':
        val, date = get_max(daily["soil_temperature_0cm"], time)
        print(f"Date with Max Soil Temp: {date} ({val}°C)")
    
    elif args.task == 'date_min_soil':
        val, date = get_min(daily["soil_temperature_0cm"], time)
        print(f"Date with Min Soil Temp: {date} ({val}°C)")
    
    elif args.task == 'plot_temp':
        plot_graph(time, daily["temperature_2m"], "Average Temperature Over Time", "Temperature (°C)")
    
    elif args.task == 'plot_wind':
        plot_graph(time, daily["wind_speed_10m"], "Average Wind Speed Over Time", "Wind Speed (km/h)")
    
    elif args.task == 'plot_soil':
        plot_graph(time, daily["soil_temperature_0cm"], "Average Soil Temperature Over Time", "Soil Temp (°C)")
    
    elif args.task == 'export_csv':
        write_csv(daily)
        print("CSV exported as 'weather_output.csv'")


if __name__ == "__main__":
    main()

