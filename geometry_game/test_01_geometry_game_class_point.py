from geometry_game_class_point import Point


def test_point_in_rectangle_passed():
    point = Point(3, 4)
    point_in_rectangle = point.falls_in_rectangle((1, 2), (7, 9))
    assert point_in_rectangle is True


def test_point_in_rectangle_failed():
    point = Point(3, 4)
    point_in_rectangle = point.falls_in_rectangle((5, 6), (7, 9))
    assert point_in_rectangle is False
