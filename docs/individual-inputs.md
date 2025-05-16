```graphql
"""
The input object that defines the fields for the createInventoryItems mutation.
"""
input IndividualInventoryItemFieldsMutationInput {
  """The ID of an `InventoryModelField`."""
  inventory_model_field_id: Int64Bit!
  """The value for the field."""
  value: Text
}
```
