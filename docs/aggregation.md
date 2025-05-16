```graphql
"""types.aggregation"""
type Aggregation {
  """The field being aggregated."""
  field: String!
  """
  The aggregation value, if the aggregation type is anything other than `COUNT`.
  This is provided as a string to assist with 64bit integer handling in Javascript.
  """
  value: String
  """A list of counts, if the aggregation type is `COUNT`."""
  counts: [AggregationBucketResult]
  """The AggregationFunction used."""
  aggregation_function: AggregationFunction!
}

"""The results of an aggregation."""
type AggregationBucketResult {
  """The string that was matched."""
  value: String!
  """The quantity of items matching the string in `bucket_value`."""
  count: String!
  """The results of a sub-aggregation query."""
  sub_aggregator_results: [Aggregation]
}
```
