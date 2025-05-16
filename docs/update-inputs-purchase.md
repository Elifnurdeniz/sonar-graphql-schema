```graphql
"""
The input object that defines the fields for the updatePurchaseOrder mutation.
"""
input UpdatePurchaseOrderMutationInput {
  """The source of the shipping address for a purchase order."""
  inventory_location_id: Int64Bit
  """A unique number identifying an approved purchase order."""
  order_number: Int
  """The current status of this purchase order."""
  status: PurchaseOrderStatus
  """
  The ID of the company that will be used in the header of this purchase order.
  """
  company_id: Int64Bit
  """A message to be included on purchase orders when sent to vendors."""
  external_message: String
  """The order items to attach to a new purchase order."""
  purchase_order_items: [UpdatePurchaseOrderOrderItemsMutationInput]
  """The ID of an order group related to this purchase order."""
  order_group_id: Int64Bit
  """The name of a vendor."""
  vendor_name: String
  """The terms of payment for deliveries from this vendor."""
  payment_terms: PaymentTerm
  """The currency used for all transactions with this vendor."""
  currency: Currency
  """Whether or not the purchase order has been marked as being paid."""
  is_paid: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """Setting this value to `true` will set `external_message` to null."""
  unset_external_message: Boolean
}

"""Add items to a new purchase order."""
input UpdatePurchaseOrderOrderItemsMutationInput {
  """The ID of a purchase order item"""
  id: Int64Bit
  """The ID of a vendor item."""
  vendor_item_id: Int64Bit
  """The quantity of a vendor item on a purchase order."""
  units: Int
  """
  The price of the vendor item at the time the purchase order was created.
  """
  price: Int64Bit
  """The current status of a purchase order item."""
  status: PurchaseOrderItemStatus
  """A list of tax IDs that should be applied to this purchase order item."""
  taxes: [Int64Bit]
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """
  Number of inventory models that are included in a single unit of this vendors product.
  """
  quantity_per_unit: Int
  """Part number used by the vendor to identify this vendor item."""
  part_number: String
  """A descriptive name."""
  name: String
  """The order this item is shown in a list."""
  list_order: Int
  """Part number used by the vendor to identify this vendor item."""
  unset_part_number: Boolean
}

"""
The input object that defines the fields for the updatePurchaseOrderSystemSettings mutation.
"""
input UpdatePurchaseOrderSystemSettingsInput {
  """The starting number for system generated purchase order numbers."""
  initial_purchase_order_number: Int
  """
  The ID of an inventory location to be the default shipping location for purchase orders.
  """
  default_inventory_location_id: Int64Bit
}
```
