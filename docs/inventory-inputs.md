```graphql
"""
The input object that defines the fields for the createInventoryItems mutation.
"""
input InventoryItemFieldsMutationInput {
  """The fields for each inventory item being added."""
  individual_inventory_item_fields: [IndividualInventoryItemFieldsMutationInput]
  """The purchase price of this item."""
  purchase_price: Int
  """The physical status of this item."""
  status: InventoryItemStatus = FUNCTIONAL
  """A decimal latitude."""
  latitude: Latitude
  """A decimal latitude."""
  longitude: Longitude
  """The quantity of this inventory model."""
  quantity: Int
}
```
