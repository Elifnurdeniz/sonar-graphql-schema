```graphql
"""
The input object that defines the fields for the createInventoryItemSegment mutation.
"""
input CreateInventoryItemSegmentMutationInput {
  """The ID of an `InventoryItem`."""
  inventory_item_id: Int64Bit!
  """The type of entity that this inventory item is assigned to."""
  inventoryitemable_type: InventoryitemableType!
  """The ID of the entity that this inventory item is assigned to."""
  inventoryitemable_id: Int64Bit!
  """The quantity of this inventory model."""
  quantity: Int!
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """The task to be performed."""
  tasks: [TaskMutationInput]
}

"""
The input object that defines the fields for the createInventoryItems mutation.
"""
input CreateInventoryItemsMutationInput {
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """The type of entity that this inventory item is assigned to."""
  inventoryitemable_type: InventoryitemableType!
  """The ID of the entity that this inventory item is assigned to."""
  inventoryitemable_id: Int64Bit!
  """The ID of a `DeploymentType`."""
  deployment_type_id: Int64Bit
  """The contents of the fields for the items being added."""
  items: [InventoryItemFieldsMutationInput]!
}

"""Provides address details for an inventory location."""
input CreateInventoryLocationAddressMutationInput {
  """Address line 1."""
  line1: String
  """Address line 2."""
  line2: String
  """A city."""
  city: String
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String
  """A two character country code."""
  country: Country!
  """A decimal latitude."""
  latitude: Latitude!
  """A decimal longitude."""
  longitude: Longitude!
}

"""
The input object that defines the fields for the createInventoryLocation mutation.
"""
input CreateInventoryLocationMutationInput {
  """A descriptive name."""
  name: String!
  """
  Marks this inventory location as the default shipping location for purchase orders.
  """
  default_shipping_location: Boolean
  """The physical address of the inventory location."""
  address: CreateInventoryLocationAddressMutationInput!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createInventoryModelCategory mutation.
"""
input CreateInventoryModelCategoryMutationInput {
  """A descriptive name."""
  name: String!
  """An icon."""
  icon: Icon!
  """The ID of a GeneralLedgerCode."""
  general_ledger_code_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createInventoryModelField mutation.
"""
input CreateInventoryModelFieldMutationInput {
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """A descriptive name."""
  name: String!
  """Types that inventory model fields can be set to."""
  type: InventoryModelFieldType!
  """Secondary types that inventory model fields can be set to."""
  secondary_type: InventoryModelFieldSecondaryType
  """Whether or not this field is required."""
  required: Boolean!
  """Whether or not the field contents must be unique."""
  unique: Uniqueness!
  """A PCRE regular expression. Omit the leading and closing /."""
  regexp: String
  """
  A single inventory model field can be set to be the primary field. This will
  be used as the primary identifier for items of this model throughout Sonar.
  """
  primary: Boolean!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createInventoryModelMinMax mutation.
"""
input CreateInventoryModelMinMaxMutationInput {
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """The ID of an `InventoryModel`."""
  inventory_location_id: Int64Bit!
  """Minimum value"""
  minimum: Int!
  """Minimum value"""
  maximum: Int
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createInventoryModel mutation.
"""
input CreateInventoryModelMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The ID of a Manufacturer."""
  manufacturer_id: Int64Bit!
  """The ID of an InventoryModelCategory."""
  inventory_model_category_id: Int64Bit!
  """An icon."""
  icon: Icon!
  """The actual model name/part number."""
  model_name: String
  """A descriptive name."""
  name: String!
  """
  The TCP port that the web interface of this type of device is available on.
  """
  port: Int
  """The protocol used to access the web interface."""
  protocol: Protocol
  """
  A generic inventory model does not have any fields, and is used for items that
  you don't need to track individually (for example, a box of screws, or a spool of cable.)
  """
  generic: Boolean!
  """The type of inventory model."""
  device_type: InventoryModelDeviceType = OTHER
  """
  Sets the default vendor to be used for purchasing this inventory model.
  """
  default_vendor_id: Int64Bit
  """Whether or not inventory item can be broken down into segments."""
  is_segmentable: Boolean
  """The quantity of this inventory model."""
  quantity: Int
  """The unit of measurement for this inventory model."""
  unit_of_measurement: UnitOfMeasurementType
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
