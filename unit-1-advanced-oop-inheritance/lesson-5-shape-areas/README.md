# Shape Areas

Complete the given shape classes to compute the correct area for all of them:

**Circles**

Are created by passing `radius` in the constructor. The area of a circle is equals to `πr^2`. That's `3.14 * radius * radius` (we round `pi` to `3.14`).

**Rectangles**

They're created by passing `side1` and `side2` and area is equals to `side1 * side2`.

**Squares**

Squares are created by passing the `side` measure of the square and the area is `side * side` .

**IMPORTANT** Squares are subclasses of `Rectangle`s. The `Square` class should **NOT** implement the `area` method, only the `__init__` method.

**Examples:**

```python
c = Circle(radius=10)
c.area()  # 314.0 (3.14 * 10 * 10)

s = Square(side=4)
s.area()  # 16 (4 * 4)

r = Rectangle(side1=4, side2=3)
r.area()  # 12 (4 * 3)
```
