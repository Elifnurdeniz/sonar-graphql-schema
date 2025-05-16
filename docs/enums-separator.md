```graphql
"""The character that marks a decimal place in a number."""
enum DecimalSeparator {
  """A comma"""
  COMMA
  """A dot/period"""
  DOT
}

"""The character that separates digits (e.g. 10,000,000 vs 10.000.000)."""
enum DigitSeparator {
  """A comma"""
  COMMA
  """A dot/period"""
  DOT
  """A space"""
  SPACE
}
```
