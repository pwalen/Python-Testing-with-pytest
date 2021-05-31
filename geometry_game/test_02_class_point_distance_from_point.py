from geometry_game import Point


def test_distance_from_point_passed():
    point1 = Point(1, 1)
    point2 = Point(2, 2)
    result = point1.distance_from_point(point2)
    result = str(round(result, 2))
    assert result == '1.41'


def test_distance_from_point_failed():
    point1 = Point(1, 1)
    point2 = Point(2, 2)
    result = point1.distance_from_point(point2)
    result = str(round(result, 2))
    assert result != '1.56'
