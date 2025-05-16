```graphql
"""Late fee application mode."""
enum LateFeeMode {
  """
  Late fee is applied as a fixed charge, based on the amount associated with the late fee service.
  """
  FLAT
  """
  Late fee is applied as a percentage of the delinquent balance, or as the
  amount of the late fee service, whichever is higher.
  """
  PERCENTAGE
}
```
