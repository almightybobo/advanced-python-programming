# Negative Numbers Iterators

The `NegativeNumbersIterator` is really similar to `NumbersIterator`, with the difference that it should count backwards starting from 0.

```python
iterator = iter(NegativeNumbersIterator())

print(next(iterator))  # 0
print(next(iterator))  # -1
print(next(iterator))  # -2
print(next(iterator))  # -3
```

**Warning!** This is also an infinite iterator.
