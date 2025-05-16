```graphql
"""
Whether or not this `Service` is applied as a `Debit` or creates a `Discount`.
"""
enum ServiceApplication {
  """A credit/discount"""
  CREDIT
  """A debit/charge"""
  DEBIT
}

"""
Whether a `Tax` is applied as a percentage of the `Service` charge, or as a flat rate.
"""
enum TaxApplication {
  """A flat rate charge, regardless of the service charge"""
  FLAT
  """A percentage of the service charge"""
  PERCENTAGE
}
```
