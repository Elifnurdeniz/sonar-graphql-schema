```graphql
"""
The input object that defines the fields for the createVoiceServiceGenericParameter mutation.
"""
input VoiceServiceGenericParameterMutationInput {
  """The type."""
  type: VoiceServiceGenericParameterType!
  """A human readable description."""
  description: String!
  """The price per unit of this item."""
  price: Int!
  """The ID of a tax definition on a transaction."""
  tax_definition_id: Int64Bit
  """The ID of a tax definition on a reversed transaction."""
  reverse_tax_definition_id: Int64Bit
  """Indicates if changes to this entity trigger proration."""
  proratable: Boolean!
}

"""Taxes applied to this voice service generic parameter."""
input VoiceServiceGenericParameterTaxMutationInput {
  """The ID of a Tax."""
  tax_id: Int64Bit!
  """
  The amount of the service that is exempt from taxation in the smallest currency value (e.g. cents, pence, pesos.)
  """
  exemption_amount: Int!
}
```
