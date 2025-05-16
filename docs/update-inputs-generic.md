```graphql
"""
The input object that defines the fields for the updateGenericInventoryAssignee mutation.
"""
input UpdateGenericInventoryAssigneeMutationInput {
  """A descriptive name."""
  name: String
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}
```
