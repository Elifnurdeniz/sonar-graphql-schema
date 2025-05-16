```graphql
"""
Inventory model field data information when updating inventory item fields.
"""
input UpdateInventoryItemFieldMutationInput {
  """The ID of an `InventoryModelField`."""
  inventory_model_field_id: Int64Bit!
  """The value."""
  value: String
  """Unset the contents of this field."""
  unset: Boolean
}

"""
The input object that defines the fields for the updateInventoryItemFields mutation.
"""
input UpdateInventoryItemFieldsMutationInput {
  """The contents of the fields for the items being added."""
  fields: [UpdateInventoryItemFieldMutationInput]!
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
The input object that defines the fields for the updateInventoryItemSegment mutation.
"""
input UpdateInventoryItemSegmentMutationInput {
  """The type of entity that this inventory item is assigned to."""
  inventoryitemable_type: InventoryitemableType
  """The ID of the entity that this inventory item is assigned to."""
  inventoryitemable_id: Int64Bit
  """The quantity of this inventory model."""
  quantity: Int
  """
  Determines how updates or deletions to a segment will handle the quantity adjustment.
  """
  segment_modifier: InventoryItemSegmentModifierType
  """
  The type of entity that this inventory item segment will be assigned to.
  """
  segmentable_type: InventoryitemableType
  """
  The ID of the entity that this inventory item segment will be assigned to.
  """
  segmentable_id: Int64Bit
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
The input object that defines the fields for the updateInventoryItems mutation.
"""
input UpdateInventoryItemsMutationInput {
  """The type of entity that this inventory item is assigned to."""
  inventoryitemable_type: InventoryitemableType
  """The ID of the entity that this inventory item is assigned to."""
  inventoryitemable_id: Int64Bit
  """The purchase price of this item."""
  purchase_price: Int
  """The physical status of this item."""
  status: InventoryItemStatus
  """The ID of a `DeploymentType`."""
  deployment_type_id: Int64Bit
  """A decimal latitude."""
  latitude: Latitude
  """A decimal latitude."""
  longitude: Longitude
  """The quantity of this inventory model."""
  quantity: Int
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """The task to be performed."""
  tasks: [TaskMutationInput]
  """Setting this value to `true` will set `purchase_price` to null."""
  unset_purchase_price: Boolean
  """Setting this value to `true` will set `deployment_type_id` to null."""
  unset_deployment_type_id: Boolean
  """Setting this value to `true` will set `latitude` to null."""
  unset_latitude: Boolean
  """Setting this value to `true` will set `longitude` to null."""
  unset_longitude: Boolean
}

"""
The input object that defines the fields for the updateInventoryItemStatus mutation.
"""
input UpdateInventoryItemStatusMutationInput {
  """The overridden status of an `InventoryItem`."""
  override_status: InventoryItemDeviceStatus
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """The task to be performed."""
  tasks: [TaskMutationInput]
  """Setting this value to `true` will set `override_status` to null."""
  unset_override_status: Boolean
}

"""Update the address details for an inventory location."""
input UpdateInventoryLocationAddressMutationInput {
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
  country: Country
  """A decimal latitude."""
  latitude: Latitude
  """A decimal longitude."""
  longitude: Longitude
}

"""
The input object that defines the fields for the updateInventoryLocation mutation.
"""
input UpdateInventoryLocationMutationInput {
  """A descriptive name."""
  name: String
  """
  Marks this inventory location as the default shipping location for purchase orders.
  """
  default_shipping_location: Boolean
  """The physical address of the inventory location."""
  address: UpdateInventoryLocationAddressMutationInput
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateInventoryModelCategory mutation.
"""
input UpdateInventoryModelCategoryMutationInput {
  """A descriptive name."""
  name: String
  """An icon."""
  icon: Icon
  """The ID of a GeneralLedgerCode."""
  general_ledger_code_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `general_ledger_code_id` to null.
  """
  unset_general_ledger_code_id: Boolean
}

"""
The input object that defines the fields for the updateInventoryModelField mutation.
"""
input UpdateInventoryModelFieldMutationInput {
  """A descriptive name."""
  name: String
  """Types that inventory model fields can be set to."""
  type: InventoryModelFieldType
  """Secondary types that inventory model fields can be set to."""
  secondary_type: InventoryModelFieldSecondaryType
  """Whether or not this field is required."""
  required: Boolean
  """Whether or not the field contents must be unique."""
  unique: Uniqueness
  """A PCRE regular expression. Omit the leading and closing /."""
  regexp: String
  """
  A single inventory model field can be set to be the primary field. This will
  be used as the primary identifier for items of this model throughout Sonar.
  """
  primary: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `secondary_type` to null."""
  unset_secondary_type: Boolean
}

"""
The input object that defines the fields for the updateInventoryModelMinMax mutation.
"""
input UpdateInventoryModelMinMaxMutationInput {
  """The ID of an `InventoryLocation`."""
  inventory_location_id: Int64Bit
  """Minimum value"""
  minimum: Int!
  """Maximum value"""
  maximum: Int
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `maximum` to null."""
  unset_maximum: Boolean
}

"""
The input object that defines the fields for the updateInventoryModel mutation.
"""
input UpdateInventoryModelMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """The ID of a Manufacturer."""
  manufacturer_id: Int64Bit
  """The ID of an InventoryModelCategory."""
  inventory_model_category_id: Int64Bit
  """An icon."""
  icon: Icon
  """The actual model name/part number."""
  model_name: String
  """A descriptive name."""
  name: String
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
  generic: Boolean
  """The type of inventory model."""
  device_type: InventoryModelDeviceType
  """
  If this is a SIM card for LTE provisioning, which provider this SIM is for.
  """
  lte_sim_type: LteProviderType
  """The ID of a `NetworkMonitoringTemplate`."""
  network_monitoring_template_id: Int64Bit
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
  """Setting this value to `true` will set `model_name` to null."""
  unset_model_name: Boolean
  """Setting this value to `true` will set `port` to null."""
  unset_port: Boolean
  """Setting this value to `true` will set `protocol` to null."""
  unset_protocol: Boolean
  """Setting this value to `true` will set `lte_sim_type` to null."""
  unset_lte_sim_type: Boolean
  """
  Setting this value to `true` will set `network_monitoring_template_id` to null.
  """
  unset_network_monitoring_template_id: Boolean
  """Setting this value to `true` will set `quantity` to null."""
  unset_quantity: Boolean
  """Setting this value to `true` will set `unit_of_measurement` to null."""
  unset_unit_of_measurement: Boolean
}
```
