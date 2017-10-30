# Small numbers decorator

Implement a `@small_numbers` decorator that enforces numeric arguments passed to a function to be less or equal than 100. If any numeric argument is greater than that specified limit, a `ValueError` should be raised. Example:

```python
@small_numbers
def my_func(number_param, string_param):
  pass

my_func(99, "Hello")  # Works OK!
my_func(101, "Oh no!")  # ValueErrro Raised!
```
