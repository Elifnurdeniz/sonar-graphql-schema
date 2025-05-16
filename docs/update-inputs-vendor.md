```graphql
"""
The input object that defines the fields for the updateVendorItem mutation.
"""
input UpdateVendorItemMutationInput {
  """A descriptive name."""
  name: String
  """
  Archived vendor items may not be used for creating new purchase orders or product requests.
  """
  archived: Boolean
  """The type of entity that is referred to by this vendor item."""
  vendoritemable_type: VendoritemableType
  """The ID of the entity that is referred to by this vendor item."""
  vendoritemable_id: Int64Bit
  """Part number used by the vendor to identify this vendor item."""
  part_number: String
  """The purchase price of this item from the vendor."""
  price: Int
  """
  Number of inventory models that are included in a single unit of this vendors product.
  """
  quantity_per_unit: Int
  """
  Flag for vendor items that should create a one-time service for retail sale to customers.
  """
  retail_item: Boolean
  """The price of the one-time service created for this vendor item"""
  retail_item_price: Int
  """
  The ID of the one-time service created when this vendor item was created.
  """
  retail_item_service_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `part_number` to null."""
  unset_part_number: Boolean
  """
  Setting this value to `true` will set `retail_item_service_id` to null.
  """
  unset_retail_item_service_id: Boolean
}

"""
The input object that defines the fields for the updateVendor mutation.
"""
input UpdateVendorMutationInput {
  """A descriptive name."""
  name: String
  """
  Archived vendors may not be used for creating new Purchase Orders or Product Requests.
  """
  archived: Boolean
  """The currency used for all transactions with this vendor."""
  currency: Currency
  """
  Determines if approved purchase orders for this vendor should automatically dispatch an email to the vendor.
  """
  automate_approved_purchase_orders: Boolean
  """
  A list of IDs belonging to the taxes that should be applied to each item sold by this vendor.
  """
  taxes: [Int64Bit]
  """The terms of payment for deliveries from this vendor."""
  payment_terms: PaymentTerm
  """The physical address of the inventory location."""
  address: CreateAddressMutationInput
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
