import unittest
from weather_task import (
    get_avg,
    get_max,
    get_min,
    write_csv,
    plot_graph,
    fetch_weather_data
)
import tempfile
import os
import csv


class TestWeatherTasks(unittest.TestCase):
    data = {
        'time': [
            '2025-07-08T01:00',
            '2025-07-08T02:00',
            '2025-07-09T01:00',
            '2025-07-09T02:00',
            '2025-07-10T01:00',
            '2025-07-10T02:00',
            '2025-07-11T01:00',
            '2025-07-11T02:00'
        ],
        'temprature': [7.3, 16.6, 16.3, 15.5, 15.4, 15.1, 14.6, 14.2],
        'wind_speed': [12.1, 12.5, 13.6, 15.9, 15.5, 12.4, 14.7, 13.4],
        'soil_tempraure': [17.9, 17.8, 17.5, 16.9, 16.6, 16.3, 16.1, 16.5]
    }

    def test_fetch_data_success(self):
        """
        Test that fetch_weather_data returns valid JSON with expected keys
        """
        data = fetch_weather_data(52.52, 13.41, "2025-07-08", "2025-07-10")
        self.assertIsInstance(data, dict)
        self.assertIn("hourly", data)
        self.assertIn("time", data["hourly"])
        self.assertIn("temperature_2m", data["hourly"])

    def test_fetch_data_failure(self):
        """
        Test to ensure API fails gracefully with invalid parameters.
        Since fetch_weather_data returns JSON, check for expected error structure.
        """
        data = fetch_weather_data(999, 999, "2025-99-99", "2025-99-99")
        self.assertIsInstance(data, dict)

    def test_get_avg_temp(self):
        """
        Test to get average of temprature
        """
        self.assertEqual(
            get_avg(self.data['temprature']),
            14.375
        )
        self.assertNotEqual(
            get_avg(self.data['temprature']),
            12
        )

    def test_get_avg_wind_speed(self):
        """
        Test to get average of wind speed
        """
        self.assertEqual(
            get_avg(self.data['wind_speed']),
            13.762500000000001
        )
        self.assertNotEqual(
            get_avg(self.data['wind_speed']),
            12.76
        )

    def test_get_avg_soil_temp(self):
        """
        Test to get average of soil temprature
        """
        self.assertEqual(
            get_avg(self.data['soil_tempraure']),
            16.95
        )
        self.assertNotEqual(
            get_avg(self.data['soil_tempraure']),
            14.76
        )

    def test_date_with_max_temp(self):
        """
        Test the get_max function that it correctly
        return the date on which the teprature is high
        """
        self.assertEqual(
            get_max(self.data['temprature'], self.data['time']),
            (16.6, '2025-07-08T02:00')
        )
        self.assertNotEqual(
            get_max(self.data['temprature'], self.data['time']),
            (15.6, '2025-07-07T02:00')
        )

    def test_date_with_max_wind_speed(self):
        """
        Test the get_max function that it correctly
        return the date on which the wind speed is high
        """
        self.assertEqual(
            get_max(self.data['wind_speed'], self.data['time']),
            (15.9, '2025-07-09T02:00')
        )
        self.assertNotEqual(
            get_max(self.data['wind_speed'], self.data['time']),
            (12.6, '2025-07-08T02:00')
        )

    def test_date_with_max_soil_temprature(self):
        """
        Test the get_max function that it correctly
        return the date on which the soil teprature is high
        """
        self.assertEqual(
            get_max(self.data['soil_tempraure'], self.data['time']),
            (17.9, '2025-07-08T01:00')
        )
        self.assertNotEqual(
            get_max(self.data['soil_tempraure'], self.data['time']),
            (14.9, '2025-07-09T01:00')
        )

    def test_date_with_min_temp(self):
        """
        Test the get_min function that it correctly
        return the date on which the teprature is low
        """
        self.assertEqual(
            get_min(self.data['temprature'], self.data['time']),
            (7.3, '2025-07-08T01:00')
        )
        self.assertNotEqual(
            get_min(self.data['temprature'], self.data['time']),
            (8.3, '2025-07-03T01:00')
        )

    def test_date_with_min_wind_speed(self):
        """Test the get_min function that it correctly
        return the date on which the wind speed is low
        """
        self.assertEqual(
            get_min(self.data['wind_speed'], self.data['time']),
            (12.1, '2025-07-08T01:00')
        )
        self.assertNotEqual(
            get_min(self.data['wind_speed'], self.data['time']),
            (10.1, '2025-07-10T01:00')
        )

    def test_date_with_min_soil_temprature(self):
        """
        Test the get_min function that it correctly return
        the date on which the soil teprature is low
        """
        self.assertEqual(
            get_min(self.data['soil_tempraure'], self.data['time']),
            (16.1, '2025-07-11T01:00')
        )
        self.assertNotEqual(
            get_min(self.data['soil_tempraure'], self.data['time']),
            (13.1, '2025-07-10T01:00')
        )

    def test_get_avg_empty(self):
        """Test get_avg with empty list"""
        self.assertIsNone(get_avg([]))

    def test_get_avg_none_values(self):
        """Test get_avg with None values in list"""
        self.assertEqual(
            get_avg([None, 10, None, 20]),
            15
        )

    def test_get_max_single_value(self):
        """Test get_max with a single element list"""
        self.assertEqual(
            get_max([42], ['2025-07-08T01:00']),
            (42, '2025-07-08T01:00')
        )

    def test_get_min_single_value(self):
        """Test get_min with a single element list"""
        self.assertEqual(
            get_min([42], ['2025-07-08T01:00']),
            (42, '2025-07-08T01:00')
        )

    def test_get_max_with_duplicates(self):
        """Test get_max when multiple values are the same maximum"""
        values = [10, 20, 20, 5]
        dates = ['t1', 't2', 't3', 't4']
        self.assertEqual(
            get_max(values, dates),
            (20, 't2')
        )

    def test_get_min_with_duplicates(self):
        """Test get_min when multiple values are the same minimum"""
        values = [10, 5, 20, 5]
        dates = ['t1', 't2', 't3', 't4']
        self.assertEqual(
            get_min(values, dates),
            (5, 't2')
        )

    def test_csv_file_content(self):
        """Test if the content of the CSV file is correct."""

        test_data = {
            "time": ["2025-07-08T01:00", "2025-07-08T02:00"],
            "temperature_2m": [22.5, 23.1],
            "wind_speed_10m": [5.5, 6.0],
            "soil_temperature_0cm": [18.2, 18.4]
        }

        with tempfile.NamedTemporaryFile(mode='r+', delete=False, newline='') as tmpfile:
            test_filename = tmpfile.name
            write_csv(test_data, test_filename)

        try:
            with open(test_filename, mode='r', newline='') as f:
                reader = csv.reader(f)
                rows = list(reader)

                expected_rows = [
                    ["Time", "Temperature (°C)", "Wind Speed (km/h)", "Soil Temperature (°C)"],
                    ["2025-07-08T01:00", "22.5", "5.5", "18.2"],
                    ["2025-07-08T02:00", "23.1", "6.0", "18.4"]
                ]

                self.assertEqual(rows, expected_rows)

        finally:
            os.remove(test_filename)

    def test_plot_graph_runs(self):
        """
        Test that plot_graph runs without throwing an exception.
        This doesn't check the actual plot visually.
        """
        dates = ["2025-07-08", "2025-07-09", "2025-07-10"]
        values = [22.5, 23.1, 21.9]
        title = "Test Temperature Plot"
        ylabel = "Temperature (°C)"

        try:
            plot_graph(dates, values, title, ylabel, show=False)
        except Exception as e:
            self.fail(f"plot_graph() raised an exception: {e}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
