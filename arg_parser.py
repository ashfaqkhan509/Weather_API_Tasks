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
            help='Task to perform'
        )

    def parse(self):
        return self.parser.parse_args()
