import pytest
from points import Point
from rects import Rectangle

@pytest.fixture
def rect1():
    return Rectangle(1, 2, 3, 4)

@pytest.fixture
def rect2():
    return Rectangle(3, 1, 5, 5)

def test_init():
    with pytest.raises(ValueError):
        Rectangle(0, 0, -5, 5)
    with pytest.raises(ValueError):
        Rectangle(0, 0, 10, -10)

def test_from_points(rect1, rect2):
    assert Rectangle.from_points((Point(1, 2), Point(3, 4))) == rect1
    assert Rectangle.from_points([Point(3, 1), Point(5, 5)]) == rect2

def test_str(rect1, rect2):
    assert str(rect1) == "[(1, 2), (3, 4)]"
    assert str(rect2) == "[(3, 1), (5, 5)]"

def test_repr(rect1, rect2):
    assert repr(rect1) == "Rectangle(1, 2, 3, 4)"
    assert repr(rect2) == "Rectangle(3, 1, 5, 5)"

def test_eq(rect1, rect2):
    assert rect1 == Rectangle(1, 2, 3, 4)
    assert rect2 == rect2

def test_ne(rect1, rect2):
    assert rect1 != Rectangle(0, 1, 2, 3)
    assert rect2 != Rectangle(0, 0, 5, 5)

def test_getters(rect1, rect2):
    assert rect1.top == 4
    assert rect1.left == 1
    assert rect1.bottom == 2
    assert rect1.right == 3

    assert rect2.width == 2
    assert rect2.height == 4

    assert rect2.topleft == Point(3, 5)
    assert rect2.bottomleft == Point(3, 1)
    assert rect2.topright == Point(5, 5)
    assert rect2.bottomright == Point(5, 1)

    assert rect1.center == Point(2, 3)

def test_area(rect1, rect2):
    assert rect1.area() == 4
    assert rect2.area() == 8

def test_move(rect1, rect2):
    rect1.move(1, 1)
    rect2.move(-2, -3)

    assert rect1 == Rectangle(2, 3, 4, 5)
    assert rect2 == Rectangle(1, -2, 3, 2)

def test_intersection(rect1, rect2):
    intersected_rect1 = rect1.intersection(rect2)
    assert intersected_rect1 == None  # in this case intersection is a line segment

    intersected_rect2 = rect1.intersection(Rectangle(1.5, 1, 2.5, 2.5))
    assert intersected_rect2 == Rectangle(1.5, 2, 2.5, 2.5)

    intersected_rect3 = rect1.intersection(Rectangle(-100, -100, 0, 0))
    assert intersected_rect3 == None

def test_cover(rect1, rect2):
    covering_rect1 = rect1.cover(rect2)
    assert covering_rect1 == Rectangle(1, 1, 5, 5)

    covering_rect2 = rect1.cover(Rectangle(1.5, 1, 2.5, 2.5))
    assert covering_rect2 == Rectangle(1, 1, 3, 4)

    covering_rect3 = rect1.cover(Rectangle(-100, -100, 0, 0))
    assert covering_rect3 == Rectangle(-100, -100, 3, 4)

def test_make4(rect1, rect2):
    rect11, rect12, rect13, rect14 = rect1.make4()
    assert rect11 == Rectangle(1, 2, 2, 3)
    assert rect12 == Rectangle(2, 2, 3, 3)
    assert rect13 == Rectangle(1, 3, 2, 4)
    assert rect14 == Rectangle(2, 3, 3, 4)

    rect21, rect22, rect23, rect24 = rect2.make4()
    assert rect21 == Rectangle(3, 1, 4, 3)
    assert rect22 == Rectangle(4, 1, 5, 3)
    assert rect23 == Rectangle(3, 3, 4, 5)
    assert rect24 == Rectangle(4, 3, 5, 5)

if __name__ == "__main__":
    pytest.main()
