```graphql
"""
The input object that defines the fields for the updateTaxExemption mutation.
"""
input UpdateTaxExemptionMutationInput {
  """A descriptive name."""
  name: String
  """The jurisdictions of this `TaxExemption`."""
  jurisdictions: [TaxJurisdiction]
  """A list of `AvalaraTaxCategory` IDs."""
  avalara_tax_category_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""The input object that defines the fields for the updateTax mutation."""
input UpdateTaxMutationInput {
  """A descriptive name."""
  name: String
  """
  The rate for a tax. For a percentage based tax, this is a percentage. For a
  flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
  """
  rate: Float
  """
  Whether this `Tax` is applied as a percentage of the `Service` charge, or as a flat rate.
  """
  application: TaxApplication
  """
  Whether this tax is applied based on the account being in a specific geography, or whether it is applied to all accounts.
  """
  type: TaxType
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateTaxOverride mutation.
"""
input UpdateTaxOverrideMutationInput {
  """
  The rate for a tax. For a percentage based tax, this is a percentage. For a
  flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
  """
  rate: Float!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateTaxProvider mutation.
"""
input UpdateTaxProviderMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The list of subdivisions where this tax provider will collect taxes."""
  subdivisions: [Subdivision]
  """Credentials for the tax provider."""
  tax_provider_credentials: [TaxProviderCredentialMutationInput]
  """A note about this entity."""
  note: NoteMutationInput
}
```
