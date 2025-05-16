```graphql
"""
The input object that defines the fields for the createMassEmail mutation.
"""
input CreateMassEmailMutationInput {
  """
  The name to send from when using this email message. If `null`, then the system default will be used.
  """
  from_name: String!
  """
  The email address to send from when using this email message. If `null`, then the system default will be used.
  """
  from_email_address: EmailAddress!
  """The subject."""
  subject: String!
  """The message."""
  message: Text!
  """
  A short sentence that will be shown as a preview in compatible email clients.
  """
  inbox_preview: String
  """IDs of `AccountStatus`es."""
  account_status_ids: [Int64Bit]
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """IDs of `Service`s."""
  service_ids: [Int64Bit]
  """IDs of `InventoryItem`s."""
  inventory_item_ids: [Int64Bit]
  """
  A list of MessageCategory IDs to apply to this contact. If this property is
  excluded, then the contact will inherit the default message categories, which
  is the typical behavior. You should only include this property if you want to
  override the default behavior.
  """
  message_category_ids: [Int64Bit]
  """
  A list of MessageCategory IDs to apply to this contact. If this property is
  excluded, then the contact will inherit the default message categories, which
  is the typical behavior. You should only include this property if you want to
  override the default behavior.
  """
  email_category_ids: [Int64Bit]
  """IDs of `Subnet`s."""
  subnet_ids: [Int64Bit]
  """IDs of `IpPool`s."""
  ip_pool_ids: [Int64Bit]
  """IDs of `NetworkSite`s."""
  network_site_ids: [Int64Bit]
  """List of language codes."""
  languages: [String]
  """Whether or not this entity is delinquent."""
  delinquent: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}

"""
The input object that defines the fields for the createMassMessage mutation.
"""
input CreateMassMessageMutationInput {
  """Whether or not to send an e-mail message."""
  send_email: Boolean!
  """Whether or not to send an SMS message."""
  send_sms: Boolean!
  """
  The name to send from when using this email message. If `null`, then the system default will be used.
  """
  from_name: String
  """
  The email address to send from when using this email message. If `null`, then the system default will be used.
  """
  from_email_address: EmailAddress
  """The subject."""
  subject: String
  """The message."""
  message: Text
  """
  A short sentence that will be shown as a preview in compatible email clients.
  """
  inbox_preview: String
  """The ID of the SMS message."""
  sms_message_id: Int64Bit
  """The ID of a signature."""
  signature_id: Int64Bit
  """Start date/time of outage"""
  outage_start: Datetime
  """End date/time of outage"""
  outage_end: Datetime
  """IDs of `AccountStatus`es."""
  account_status_ids: [Int64Bit]
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """IDs of `Service`s."""
  service_ids: [Int64Bit]
  """IDs of `InventoryItem`s."""
  inventory_item_ids: [Int64Bit]
  """
  A list of MessageCategory IDs to apply to this contact. If this property is
  excluded, then the contact will inherit the default message categories, which
  is the typical behavior. You should only include this property if you want to
  override the default behavior.
  """
  message_category_ids: [Int64Bit]
  """IDs of `Subnet`s."""
  subnet_ids: [Int64Bit]
  """IDs of `IpPool`s."""
  ip_pool_ids: [Int64Bit]
  """IDs of `NetworkSite`s."""
  network_site_ids: [Int64Bit]
  """List of language codes."""
  languages: [String]
  """Whether or not this entity is delinquent."""
  delinquent: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
