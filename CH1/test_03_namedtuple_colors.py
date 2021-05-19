from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
Color.__new__.__defaults__ = (255, 255, 255)


def test_default_values():
    color_1 = Color()
    color_2 = Color(255, 255, 255)
    assert color_1 == color_2


def test_color_value_access():
    color = Color(5, 52)
    assert color.red == 5
    assert color.green == 52
    assert color.blue == 255
