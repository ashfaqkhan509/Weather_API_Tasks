import unittest
from weather_task import get_avg, get_max, get_min


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


if __name__ == "__main__":
    unittest.main(verbosity=2)