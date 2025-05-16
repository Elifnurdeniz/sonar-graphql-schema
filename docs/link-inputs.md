```graphql
"""
The input object that defines the fields for the linkAccounts mutation.
"""
input LinkAccountsMutationInput {
  """The ID of a child `Account`."""
  child_account_id: Int64Bit!
}

"""
The input object that defines the fields for the linkFibermapServiceLocationToAddress mutation.
"""
input LinkCalixCloudSubscriberToAccountMutationInput {
  """The ID of a `CalixCloudAudit`."""
  calix_cloud_audit_id: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
}

"""
The input object that defines the fields for the linkEntityToTicket mutation.
"""
input LinkEntityToTicketMutationInput {
  """The entity type to link."""
  linked_entityable_type: TicketLinkableEntityType!
  """The entity ID to link."""
  linked_entityable_id: Int64Bit!
}

"""
The input object that defines the fields for the linkFibermapPlanToNetworkSite mutation.
"""
input LinkFibermapPlanToNetworkSiteMutationInput {
  """FiberMap plan ID"""
  fibermap_plan_id: Int64Bit!
  """Network site id."""
  network_site_id: Int64Bit
}

"""
The input object that defines the fields for the linkFibermapServiceLocationToAddress mutation.
"""
input LinkFibermapServiceLocationToAddressMutationInput {
  """Fibermap service location ID."""
  fibermap_service_location_id: Int64Bit!
  """The ID of the address."""
  address_id: Int64Bit
  """A two character country code."""
  country: String
}

"""
The input object that defines the fields for the linkFileToEntity mutation.
"""
input LinkFileToEntityMutationInput {
  """The type of entity that owns this file."""
  fileable_type: FileableType!
  """The ID of the entity that owns this file."""
  fileable_id: Int64Bit!
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}

"""
The input object that defines the fields for the linkInventoryItemToAccountService mutation.
"""
input LinkInventoryItemToAccountServiceMutationInput {
  """The ID of an `InventoryItem`."""
  inventory_item_id: Int64Bit!
  """The ID of an AccountService."""
  account_service_id: Int64Bit
  """Setting this value to `true` will set `account_service_id` to null."""
  unset_account_service_id: Boolean
}

"""
The input object that defines the fields for the linkInventoryModelToAccountServices mutation.
"""
input LinkInventoryModelToAccountServicesMutationInput {
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """The ID of a Service."""
  service_ids: [Int64Bit]!
  """Whether or not to overwrite existing links."""
  overwrite_existing_links: Boolean!
}

"""
The input object that defines the fields for the linkInvoices mutation.
"""
input LinkInvoicesMutationInput {
  """The ID of a child `Invoice`."""
  child_invoice_id: Int64Bit!
}

"""
The input object that defines the fields for the linkTowercoverageSubmissionToServiceableAddress mutation.
"""
input LinkTowercoverageSubmissionToServiceableAddressMutationInput {
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
  """A decimal latitude."""
  longitude: Longitude
  """Setting this value to `true` will set `line2` to null."""
  unset_line2: Boolean
}
```
