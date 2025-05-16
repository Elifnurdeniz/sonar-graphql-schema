```graphql
"""An aggregation function, used by the `Aggregator`."""
enum AggregationFunction {
  """Returns the maximum value across all matching entities"""
  MAX
  """Returns the minimum value across all matching entities"""
  MIN
  """Returns the total value across all matching entities"""
  SUM
  """Returns the average value across all matching entities"""
  AVG
  """
  Returns a count of all elements where a field matches a particular value. Only works on string fields.
  """
  COUNT
}
```
