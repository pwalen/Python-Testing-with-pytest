from geometry_game import Point


def test_point_in_rectangle_passed():
    point = Point(3, 4)
    rectangle_coordinates = ((1, 2), (7, 9))
    point_in_rectangle = point.falls_in_rectangle(rectangle_coordinates[0], rectangle_coordinates[1])
    assert point_in_rectangle is True


def test_point_in_rectangle_failed():
    point = Point(3, 4)
    rectangle_coordinates = ((5, 6), (7, 9))
    point_in_rectangle = point.falls_in_rectangle(rectangle_coordinates[0], rectangle_coordinates[1])
    assert point_in_rectangle is False
