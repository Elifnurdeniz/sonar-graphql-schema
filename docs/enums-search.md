```graphql
"""The general search mode to use."""
enum GeneralSearchMode {
  """
  Search in only the root of the query. Root elements will be limited to those that have a match in a string field.
  """
  ROOT
  """
  Search through the root of query, and all query relations. Root elements will
  be limited to those that have a match in themselves or any relation.
  """
  ROOT_PLUS_RELATIONS
}
```
