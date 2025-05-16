```graphql
"""
The input object that defines the fields for the createTaxExemption mutation.
"""
input CreateTaxExemptionMutationInput {
  """The ID of an `TaxProvider`."""
  tax_provider_id: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
  """A descriptive name."""
  name: String!
  """The jurisdictions of this `TaxExemption`."""
  jurisdictions: [TaxJurisdiction]!
  """A list of `AvalaraTaxCategory` IDs."""
  avalara_tax_category_ids: [Int64Bit]!
  """A note about this entity."""
  note: NoteMutationInput
}

"""The input object that defines the fields for the createTax mutation."""
input CreateTaxMutationInput {
  """A descriptive name."""
  name: String!
  """
  Whether this `Tax` is applied as a percentage of the `Service` charge, or as a flat rate.
  """
  application: TaxApplication!
  """
  The rate for a tax. For a percentage based tax, this is a percentage. For a
  flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
  """
  rate: Float!
  """
  Whether this tax is applied based on the account being in a specific geography, or whether it is applied to all accounts.
  """
  type: TaxType!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createTaxOverride mutation.
"""
input CreateTaxOverrideMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of a Tax."""
  tax_id: Int64Bit!
  """
  The rate for a tax. For a percentage based tax, this is a percentage. For a
  flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
  """
  rate: Float!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createTaxProvider mutation.
"""
input CreateTaxProviderMutationInput {
  """A descriptive name."""
  name: String!
  """The type of `TaxProvider`."""
  type: TaxProviderType!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The list of subdivisions where this tax provider will collect taxes."""
  subdivisions: [Subdivision]
  """Credentials for the tax provider."""
  tax_provider_credentials: [TaxProviderCredentialMutationInput]!
  """A note about this entity."""
  note: NoteMutationInput
}
```
