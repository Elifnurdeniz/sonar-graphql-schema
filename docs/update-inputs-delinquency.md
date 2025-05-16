```graphql
"""
The input object that defines the fields for the updateDelinquencyExclusion mutation.
"""
input UpdateDelinquencyExclusionMutationInput {
  """A descriptive name."""
  name: String
  """The day that this exclusion covers."""
  day: Int
  """The month that this exclusion covers."""
  month: Int
  """The year that this exclusion covers."""
  year: Int
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `year` to null."""
  unset_year: Boolean
}
```
