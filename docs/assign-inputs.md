```graphql
"""
The input object that defines the fields for the assignGenericInventoryItems mutation.
"""
input AssignGenericInventoryItemsMutationInput {
  """The ID of the entity that owns this generic `InventoryItem`."""
  genericinventoryitemable_type: InventoryitemableType!
  """The ID of the entity that owns this generic `InventoryItem`."""
  genericinventoryitemable_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int!
}

"""
The input object that defines the fields for the assignInventoryItems mutation.
"""
input AssignInventoryItemsMutationInput {
  """The type of entity that this inventory item is assigned to."""
  inventoryitemable_type: InventoryitemableType
  """The ID of the entity that this inventory item is assigned to."""
  inventoryitemable_id: Int64Bit
  """The ID of a `DeploymentType`."""
  deployment_type_id: Int64Bit
  """Setting this value to `true` will set `deployment_type_id` to null."""
  unset_deployment_type_id: Boolean
}
```
