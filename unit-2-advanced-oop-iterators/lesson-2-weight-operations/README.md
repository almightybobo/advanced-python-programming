# Weight operations

Use Magic Methods to support the `+` operator in the custom built class `Weight`. Example:

```python
w1 = Weight(kilograms=80)
w2 = Weight(pounds=46)
w3 = w1 + w2

print(w3.kilograms)  # 100.90
print(w3.pounds)  # 222.0
```

You can also combine it with properties to have a more powerful solution.
