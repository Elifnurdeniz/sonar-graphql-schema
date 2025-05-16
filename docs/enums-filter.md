```graphql
"""The operator applied to a `StoredFilter`."""
enum StoredFilterOperator {
  """Matches"""
  MATCH
  """Does Not Match"""
  NO_MATCH
  """Is set"""
  ISSET
  """Unset"""
  UNSET
  """Equals True"""
  EQ_TRUE
  """Equals False"""
  EQ_FALSE
  """Equals Me"""
  EQ_ME
  """Greater Than"""
  GT
  """Greater Than or Equal To"""
  GTE
  """Less Than"""
  LT
  """Less Than or Equal To"""
  LTE
  """Is Within Range"""
  RANGE
  """Is One Of"""
  ONE_OF
  """Is Not One Of"""
  NOT_OF
}
```
