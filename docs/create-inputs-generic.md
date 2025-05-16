```graphql
"""
The input object that defines the fields for the createGenericInventoryAssignee mutation.
"""
input CreateGenericInventoryAssigneeMutationInput {
  """A descriptive name."""
  name: String!
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

"""
The input object that defines the fields for the createGenericInventoryItems mutation.
"""
input CreateGenericInventoryItemsMutationInput {
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """The ID of the entity that owns this generic `InventoryItem`."""
  genericinventoryitemable_type: InventoryitemableType!
  """The type of entity that owns this generic `InventoryItem`."""
  genericinventoryitemable_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int!
  """The purchase price of this item."""
  purchase_price: Float
  """A note about this entity."""
  note: NoteMutationInput
}
```
