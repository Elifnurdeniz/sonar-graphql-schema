```graphql
"""
Includes accounts with an account status that matches this activation setting in this address list.
"""
enum AddressListAccountStatus {
  """All account statuses."""
  ALL
  """All account statuses that activate an account."""
  ACTIVE
  """All account statuses that do not activate an account."""
  INACTIVE
}

"""
Includes accounts with a delinquency state that matches this in this address list.
"""
enum AddressListDelinquency {
  """All accounts, regardless of delinquency."""
  ALL
  """Only include delinquent accounts."""
  DELINQUENT
  """Only include accounts which are not delinquent."""
  CURRENT
}
```
