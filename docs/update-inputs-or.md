```graphql
"""The fields necessary to update or create an address."""
input UpdateOrCreateAddressMutationInput {
  """Address line 1."""
  line1: String!
  """Address line 2."""
  line2: String
  """A city."""
  city: String!
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String!
  """A two character country code."""
  country: Country!
  """Address line 2."""
  unset_line2: Boolean
}
```
