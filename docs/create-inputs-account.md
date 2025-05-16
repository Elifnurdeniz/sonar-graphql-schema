```graphql
"""
The input object that defines the fields for the createAccountAdjustmentTransaction mutation.
"""
input CreateAccountAdjustmentTransactionMutationInput {
  """The ID of a Service."""
  service_id: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
  """The amount to apply this adjustment service for."""
  amount: Int!
  """A description for the transaction."""
  description: String
}

"""
The input object that defines the fields for the createAccountAdtranMosaicServiceDetail mutation.
"""
input CreateAccountAdtranMosaicServiceDetailMutationInput {
  """The ID of an AccountService."""
  account_service_id: Int64Bit!
  """The ID of an Adtran Mosaic setting."""
  adtran_mosaic_setting_id: Int64Bit!
  """The name of the Adtran Mosaic content provider."""
  uplink_content_provider_name: String
  """The name of the Adtran Mosaic uplink inner tag vlan."""
  uplink_inner_tag_vlan: String
  """The name of the Adtran Mosaic uplink outer tag vlan."""
  uplink_outer_tag_vlan: String
  """The name of the Adtran Mosaic downlink interface."""
  downlink_interface_name: String
  """The name of the Adtran Mosaic downlink inner tag vlan."""
  downlink_inner_tag_vlan: String
  """The name of the Adtran Mosaic downlink outer tag vlan."""
  downlink_outer_tag_vlan: String
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createAccountCalixServiceDetail mutation.
"""
input CreateAccountCalixServiceDetailMutationInput {
  """The ID of an AccountService."""
  account_service_id: Int64Bit!
  """Calix Inegartion ID."""
  calix_integration_id: Int64Bit!
  """VLAN."""
  vlan: String
  """C-VLAN."""
  cvlan: Int64Bit
  """Global VLAN."""
  global_vlan: String
  """Policy Map."""
  policy_map: String
  """ONT Port ID."""
  ont_port_id: String
  """Custom JSON."""
  custom_json: String
  """Use Custom JSON."""
  use_custom_json: Boolean
}

"""
The input object that defines the fields for the createAccountGroup mutation.
"""
input CreateAccountGroupMutationInput {
  """A descriptive name."""
  name: String!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createAccount mutation.
"""
input CreateAccountMutationInput {
  """The ID of the entity."""
  id: Int64Bit
  """A descriptive name."""
  name: String!
  """The ID of an AccountStatus."""
  account_status_id: Int64Bit!
  """The ID of an AccountType."""
  account_type_id: Int64Bit!
  """The ID of the serviceable address to use for this account."""
  serviceable_address_id: Int64Bit
  """
  An address where this entity receives mail. If this is not set, the physical address will be used as the mailing address.
  """
  mailing_address: CreateAddressMutationInput
  """The primary contact person."""
  primary_contact: CreatePrimaryContactMutationInput!
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit!
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
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
The input object that defines the fields for the createAccountOneTimeTransaction mutation.
"""
input CreateAccountOneTimeTransactionMutationInput {
  """The ID of a Service."""
  service_id: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
  """A description for the transaction."""
  description: String
  """The quantity for this service."""
  quantity: Int!
  """
  The amount to override the cost of the service to. If this is excluded, the service cost will be used.
  """
  price_override: Int
  """
  Items specific to a voice service. Includes the quantity, price override, and related configuration parameter of each.
  """
  account_voice_service_details: [OneTimeTransactionAccountVoiceServiceDetailMutationInput]
}

"""
The input object that defines the fields for the createAccountStatus mutation.
"""
input CreateAccountStatusMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this status activates the account."""
  activates_account: Boolean!
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor!
  """An icon."""
  icon: Icon!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createAccountType mutation.
"""
input CreateAccountTypeMutationInput {
  """A descriptive name."""
  name: String!
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor
  """An icon."""
  icon: Icon
  """The type."""
  type: AccountTypeEnum!
  """The ID of an `InvoiceMessage`."""
  invoice_message_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}
```
