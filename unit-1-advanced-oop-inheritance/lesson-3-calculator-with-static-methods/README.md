# Calculator with static methods

Build a calculator using only static and class methods.

This is the way it should work:

```python
Calculator.add(2, 4)  # 6
Calculator.subtract(8, 1)  # 7
Calculator.multiply(3, 5)  # 15
Calculator.divide(5, 2)  # 2.5
```

Note that I've never created an instance of the calculator. I'm using the regular class.

One final addition. The `subtract` method **must** be implemented using the `add` method. Something like this:

```python
subtract = add(x, y * -1)
```

# python @classmethod and @staticmethod
- classmethod:  the class of the object instance is implicitly passed as the first argument instead of self 
	( need **class** to be the first parameter )
- staticmethod: neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class
	( real static, don't need self )
