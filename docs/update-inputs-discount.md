```graphql
"""
The input object that defines the fields for the updateDiscount mutation.
"""
input UpdateDiscountMutationInput {
  """A description for the transaction."""
  description: String
  """Setting this value to `true` will set `description` to null."""
  unset_description: Boolean
}
```
