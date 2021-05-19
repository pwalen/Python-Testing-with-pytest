"""Test the Car data type."""

from collections import namedtuple

Car = namedtuple('Car', 'brand model version availability year brandNew id'.split())
Car.__new__.__defaults__ = (None, None, None, True, None, True, None)


def test_asdict():
    """_asdict() should return a dictionary."""
    car = Car('Peugeot', '406', '2.0 HDI Saint Tropez Sedan', False, 2001, False, 11)
    car_dict = car._asdict()
    car_expected = {
        'brand': 'Peugeot',
        'model': '406',
        'version': '2.0 HDI Saint Tropez Sedan',
        'availability': False,
        'year': 2001,
        'brandNew': False,
        'id': 11
    }
    assert car_dict == car_expected


def test_replace():
    """replace() should change passed in fields."""
    car_before = Car('Opel', 'Astra', '1.4 L Family 1 I4', False, 2005, False, 12)
    car_after = car_before._replace(version='1.6 L Family 1 I4', availability=True)
    car_expected = Car('Opel', 'Astra', '1.6 L Family 1 I4', True, 2005, False, 12)
    assert car_after == car_expected
