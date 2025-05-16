```graphql
"""
The details of the inventory items that will be created from this purchase order item.
"""
input ReceivePurchaseOrderItemMutationInput {
  """The ID of a purchase order item"""
  purchase_order_item_id: Int64Bit!
  """The type of entity that this inventory item is assigned to."""
  inventoryitemable_type: InventoryitemableType!
  """The ID of the entity that this inventory item is assigned to."""
  inventoryitemable_id: Int64Bit!
  """
  The quantity of a generic purchase order item to receive at a particular inventory location.
  """
  generic_item_quantity: Int
  """The contents of the fields for the items being added."""
  items: [InventoryItemFieldsMutationInput]
}

"""
The input object that defines the fields for the receivePurchaseOrderItems mutation.
"""
input ReceivePurchaseOrderItemsMutationInput {
  """The purchase order items to be received at an inventory location."""
  items: [ReceivePurchaseOrderItemMutationInput]
}
```
