```graphql
"""
The input object that defines the fields for the createServiceableAddressAccountAssignmentFuture mutation.
"""
input CreateServiceableAddressAccountAssignmentFutureMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of the address."""
  address_id: Int64Bit!
  """The date this is targeted to happen."""
  target_date: Date!
  """
  A note about this expected change of serviceable address account assignment.
  """
  note: Text
}

"""
The input object that defines the fields for the createServiceableAddress mutation.
"""
input CreateServiceableAddressMutationInput {
  """The ID of the entity."""
  id: Int64Bit
  """Address line 1."""
  line1: String!
  """Address line 2."""
  line2: String
  """A city."""
  city: String!
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String!
  """A two character country code."""
  country: Country!
  """A decimal latitude."""
  latitude: Latitude!
  """A decimal latitude."""
  longitude: Longitude!
  """The timezone you want times in the system displayed in."""
  timezone: Timezone
  """IDs of `NetworkSite`s."""
  network_site_ids: [Int64Bit]
  """Address status ID."""
  address_status_id: Int64Bit
  """Whether or not this address is an anchor"""
  is_anchor: Boolean = false
  """The address ID for the Anchor address"""
  anchor_address_id: Int64Bit
  """The ID of a BillingDefault."""
  billing_default_id: Int64Bit
  """The attainable download speed in kilobits per second."""
  attainable_download_speed: Int
  """The attainable upload speed in kilobits per second."""
  attainable_upload_speed: Int
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
