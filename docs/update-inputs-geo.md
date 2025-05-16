```graphql
"""
The input object that defines the fields for the updateGeoTaxZone mutation.
"""
input UpdateGeoTaxZoneMutationInput {
  """A descriptive name."""
  name: String
  """
  The rate for a tax. For a percentage based tax, this is a percentage. For a
  flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
  """
  rate: Float
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
  zip_partial_match: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `subdivision` to null."""
  unset_subdivision: Boolean
  """Setting this value to `true` will set `city` to null."""
  unset_city: Boolean
  """Setting this value to `true` will set `county` to null."""
  unset_county: Boolean
  """Setting this value to `true` will set `country` to null."""
  unset_country: Boolean
  """Setting this value to `true` will set `zip` to null."""
  unset_zip: Boolean
}
```
