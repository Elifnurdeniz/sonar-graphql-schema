```graphql
"""
The input object that defines the fields for the createDelinquencyExclusion mutation.
"""
input CreateDelinquencyExclusionMutationInput {
  """A descriptive name."""
  name: String!
  """The day that this exclusion covers."""
  day: Int!
  """The month that this exclusion covers."""
  month: Int!
  """The year that this exclusion covers."""
  year: Int
  """A note about this entity."""
  note: NoteMutationInput
}
```
