```graphql
"""
The input object that defines the fields for the updatePackage mutation.
"""
input UpdatePackageMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """IDs of `Service`s."""
  services: [PackageServiceMutationInput]
  """
  Setting to indicate if services in this package should be rolled up into a package total when this package is displayed.
  """
  rollup_services: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `company_id` to null."""
  unset_company_id: Boolean
}
```
