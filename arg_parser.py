import argparse


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Weather Data Analysis using Open-Meteo API"
        )
        self.parser.add_argument(
            '--latitude',
            type=float,
            required=True,
            help='Latitude of the location'
        )
        self.parser.add_argument(
            '--longitude',
            type=float,
            required=True,
            help='Longitude of the location'
            )
        self.parser.add_argument(
            '--start',
            type=str,
            required=True,
            help='Start date in YYYY-MM-DD format'
        )
        self.parser.add_argument(
            '--end',
            type=str,
            required=True,
            help='End date in YYYY-MM-DD format'
        )
        self.parser.add_argument(
            '--task',
            type=str,
            required=True,
            choices=[
                'max_temp', 'min_temp', 'avg_temp',
                'max_wind', 'min_wind', 'avg_wind',
                'max_soil', 'min_soil', 'avg_soil',
                'date_max_temp', 'date_min_temp',
                'date_max_wind', 'date_min_wind',
                'date_max_soil', 'date_min_soil',
                'plot_temp', 'plot_wind', 'plot_soil',
                'export_csv'
            ],
            help='Task to perform'
        )

    def parse(self):
        return self.parser.parse_args()
