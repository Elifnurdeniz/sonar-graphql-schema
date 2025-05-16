```graphql
"""
The input object that defines the fields for the updateAccountActivationDate mutation.
"""
input UpdateAccountActivationDateMutationInput {
  """The date an account was first activated."""
  activation_date: Date!
  """The time an account was first activated."""
  activation_time: Time
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
The input object that defines the fields for the updateAccountAdtranMosaicServiceDetail mutation.
"""
input UpdateAccountAdtranMosaicServiceDetailMutationInput {
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
  """
  Setting this value to `true` will set `uplink_content_provider_name` to null.
  """
  unset_uplink_content_provider_name: Boolean
  """Setting this value to `true` will set `uplink_inner_tag_vlan` to null."""
  unset_uplink_inner_tag_vlan: Boolean
  """Setting this value to `true` will set `uplink_outer_tag_vlan` to null."""
  unset_uplink_outer_tag_vlan: Boolean
  """
  Setting this value to `true` will set `downlink_interface_name` to null.
  """
  unset_downlink_interface_name: Boolean
  """
  Setting this value to `true` will set `downlink_inner_tag_vlan` to null.
  """
  unset_downlink_inner_tag_vlan: Boolean
  """
  Setting this value to `true` will set `downlink_outer_tag_vlan` to null.
  """
  unset_downlink_outer_tag_vlan: Boolean
}

"""
The input object that defines the fields for the updateAccountBillingParameter mutation.
"""
input UpdateAccountBillingParameterMutationInput {
  """
  The next date this service will bill. If this is null, it will bill on the next account billing date.
  """
  next_bill_date: Date
  """The day that billing runs."""
  bill_day: Int
  """The number of days after the invoice date that it is due."""
  due_days: Int
  """
  The number of days after the invoice due date that the invoice is marked delinquent.
  """
  grace_days: Int
  """
  A temporary override that stops the account becoming delinquent until this date.
  """
  grace_until: Date
  """
  The number of days after `auto_pay_day` that autopay runs for an invoice.
  """
  auto_pay_days: Int
  """The number of months to bill at a time."""
  months_to_bill: Int
  """Whether or not this account is tax exempt."""
  tax_exempt: Boolean
  """The type of bill this account receives."""
  bill_mode: BillMode
  """Whether this account receives a printed invoice."""
  print_invoice: Boolean
  """
  The day that automatic billing invoices are generated for. If this is `null`, then `bill_day` is used.
  """
  invoice_day: Int
  """
  If `invoice_day` is not null, this allows you to select whether
  `auto_pay_days` is calculated from the billing day, or the invoice day.
  """
  auto_pay_day: BillingParameterDayOption
  """
  If `invoice_day` is not null, this allows you to select whether `due_days` is
  calculated from the billing day, or the invoice day.
  """
  due_days_day: BillingParameterDayOption
  """
  Whether or not this account should be moved into another status after being delinquent for a preset period.
  """
  switch_status_after_delinquency: Boolean
  """
  If `switch_status_after_delinquency` is `true`, then this is the number of
  days of delinquency to allow before the status switch.
  """
  days_of_delinquency_for_status_switch: Int
  """
  If `switch_status_after_delinquency` is true, this is the account status that
  the account will be moved into after `days_of_delinquency_for_status_switch`
  days of delinquency.
  """
  delinquency_account_status_id: Int64Bit
  """
  If `switch_status_after_delinquency` is `true`, then this is the status the
  account will be moved back into if delinquency is cleared while the account is
  set to the `delinquency_account_status_id` account status.
  """
  delinquency_removal_account_status_id: Int64Bit
  """Whether or not changing an account bill day is prorated by default."""
  prorate: Boolean
  """
  Whether the account bill and invoice day are fixed, the account activation day
  is used as bill day, or the account activation day is used as the invoice day.
  """
  bill_day_mode: BillDayModeOption
  """
  Whether or not this account participates in the federal Lifeline program.
  """
  lifeline: Boolean
  """
  Whether or not to aggregate invoice taxes instead of printing with each charge.
  """
  aggregate_invoice_taxes: Boolean
  """Whether or not to aggregate linked debits on Anchor invoices."""
  aggregate_linked_debits: Boolean
  """Setting this value to `true` will set `invoice_day` to null."""
  unset_invoice_day: Boolean
  """Setting this value to `true` will set `grace_until` to null."""
  unset_grace_until: Boolean
  """
  Setting this value to `true` will set `delinquency_removal_account_status_id` to null.
  """
  unset_delinquency_removal_account_status_id: Boolean
}

"""
The input object that defines the fields for the updateAccountCalixServiceDetail mutation.
"""
input UpdateAccountCalixServiceDetailMutationInput {
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
  """Setting this value to `true` will set `vlan` to null."""
  unset_vlan: Boolean
  """Setting this value to `true` will set `cvlan` to null."""
  unset_cvlan: Boolean
  """Setting this value to `true` will set `global_vlan` to null."""
  unset_global_vlan: Boolean
  """Setting this value to `true` will set `policy_map` to null."""
  unset_policy_map: Boolean
  """Setting this value to `true` will set `ont_port_id` to null."""
  unset_ont_port_id: Boolean
  """Setting this value to `true` will set `custom_json` to null."""
  unset_custom_json: Boolean
}

"""
The input object that defines the fields for the updateAccountGroup mutation.
"""
input UpdateAccountGroupMutationInput {
  """A descriptive name."""
  name: String
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateAccount mutation.
"""
input UpdateAccountMutationInput {
  """A descriptive name."""
  name: String
  """The ID of an AccountStatus."""
  account_status_id: Int64Bit
  """The ID of an AccountType."""
  account_type_id: Int64Bit
  """The ID of the serviceable address to use for this account."""
  serviceable_address_id: Int64Bit
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """
  If you are changing the account status from an active status to an inactive
  status, this allows you to override the system default proration policy, if
  you have the appropriate permissions.
  """
  prorate: Boolean
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
  """
  Setting this value to `true` will set `serviceable_address_id` to null.
  """
  unset_serviceable_address_id: Boolean
}

"""
The input object that defines the fields for the updateAccountService mutation.
"""
input UpdateAccountServiceMutationInput {
  """The quantity for this service."""
  quantity: Int
  """
  The amount that this service price has been overridden to. If this is null, then the service price is used.
  """
  price_override: Int
  """The reason that the price of a service has been overridden."""
  price_override_reason: String
  """
  Overriding the service name will alter the service name printed on an invoice.
  """
  name_override: String
  """
  The next date this service will bill. If this is null, it will bill on the next account billing date.
  """
  next_bill_date: Date
  """
  Service metadata allows you to store individualized information about a
  service, as it relates to a specific account. For example, on a domain renewal
  service, you could store the domain name as metadata.
  """
  service_metadata: [AccountServiceMetadataMutationInput]
  """
  Unset the values inside service metadata fields for this `AccountService`.
  """
  unset_service_metadata: [Int64Bit]
  """Whether or not to prorate the transaction."""
  prorate: Boolean
  """
  If the amount for this service is zero, it will still display on invoices.
  """
  display_if_zero: Boolean
  """
  The number of billing cycles that have already been consumed by this
  particular service. This is only used for expiring services. NOTE: Typically
  this is the number of times billed but the value may be modified manually to
  adjust service expiration. See also the the `ExpiringServiceDetail`
  `times_to_run` field.
  """
  number_of_times_billed: Int
  """Setting this value to `true` will set `price_override` to null."""
  unset_price_override: Boolean
  """Setting this value to `true` will set `name_override` to null."""
  unset_name_override: Boolean
  """Setting this value to `true` will set `next_bill_date` to null."""
  unset_next_bill_date: Boolean
}

"""
The input object that defines the fields for the updateAccountStatus mutation.
"""
input UpdateAccountStatusMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this status activates the account."""
  activates_account: Boolean
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor
  """An icon."""
  icon: Icon
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateAccountType mutation.
"""
input UpdateAccountTypeMutationInput {
  """A descriptive name."""
  name: String
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor
  """An icon."""
  icon: Icon
  """The type."""
  type: AccountTypeEnum
  """The ID of an `InvoiceMessage`."""
  invoice_message_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `invoice_message_id` to null."""
  unset_invoice_message_id: Boolean
}

"""
The input object that defines the fields for the updateAccountVoiceServiceDetail mutation.
"""
input UpdateAccountVoiceServiceDetailMutationInput {
  """The quantity for this service."""
  quantity: Int
  """
  The amount that this service price has been overridden to. If this is null, then the service price is used.
  """
  price_override: Int
  """The reason that the price of a service has been overridden."""
  price_override_reason: String
  """Whether or not to prorate the transaction."""
  prorate: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `price_override` to null."""
  unset_price_override: Boolean
  """Setting this value to `true` will set `price_override_reason` to null."""
  unset_price_override_reason: Boolean
}
```
