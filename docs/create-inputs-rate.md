```graphql
"""
The input object that defines the fields for the createRateCenter mutation.
"""
input CreateRateCenterMutationInput {
  """A descriptive name."""
  name: String!
  """A note about this entity."""
  note: NoteMutationInput
}
```
