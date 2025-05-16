```graphql
"""
The input object that defines the fields for the createGeoTaxZone mutation.
"""
input CreateGeoTaxZoneMutationInput {
  """A descriptive name."""
  name: String!
  """The ID of a Tax."""
  tax_id: Int64Bit!
  """
  The rate for a tax. For a percentage based tax, this is a percentage. For a
  flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
  """
  rate: Float!
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A city."""
  city: String
  """A US county. Only used for US addresses."""
  county: UsCounty
  """A two character country code."""
  country: Country
  """A ZIP or postal code."""
  zip: String
  """Whether to match on partial ZIP/postal codes."""
  zip_partial_match: Boolean!
  """A note about this entity."""
  note: NoteMutationInput
}
```
