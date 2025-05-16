```graphql
"""
Provides the ability to return aggregate mathematical data about your results.
For example, you can `SUM` all the payment amounts, or `AVG` ICMP response times.
"""
input Aggregator {
  """The field you wish to run the aggregation against."""
  field_name: String!
  """An aggregation function, used by the `Aggregator`."""
  aggregation_function: AggregationFunction!
  """
  An aggregator that is run based on the results of the parent aggregation.
  """
  sub_aggregators: [Aggregator]
}
```
