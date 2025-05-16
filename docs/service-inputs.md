```graphql
"""Taxes applied to this service."""
input ServiceTaxMutationInput {
  """The ID of a Tax."""
  tax_id: Int64Bit!
  """
  The amount of the service that is exempt from taxation in the smallest currency value (e.g. cents, pence, pesos.)
  """
  exemption_amount: Int!
}
```
