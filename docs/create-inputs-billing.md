```graphql
"""
The input object that defines the fields for the createBillingDefault mutation.
"""
input CreateBillingDefaultLinkedInput {
  """A descriptive name."""
  name: String!
  """The ID of an AccountType."""
  account_type_id: Int64Bit
  """
  Whether or not to use a fixed bill day, versus anniversary day billing. Use `bill_day_mode` for further customization.
  """
  fixed_bill_day: Boolean
  """The day that billing runs."""
  bill_day: Int
  """The number of days after the invoice date that it is due."""
  due_days: Int!
  """
  The number of days after the invoice due date that the invoice is marked delinquent.
  """
  grace_days: Int!
  """
  The number of days after `auto_pay_day` that autopay runs for an invoice.
  """
  auto_pay_days: Int!
  """The number of months to bill at a time."""
  months_to_bill: Int!
  """Whether or not this account is tax exempt."""
  tax_exempt: Boolean!
  """The type of bill this account receives."""
  bill_mode: BillMode!
  """Whether this account receives a printed invoice."""
  print_invoice: Boolean!
  """
  The day that automatic billing invoices are generated for. If this is `null`, then `bill_day` is used.
  """
  invoice_day: Int
  """
  If `invoice_day` is not null, this allows you to select whether
  `auto_pay_days` is calculated from the billing day, or the invoice day.
  """
  auto_pay_day: BillingParameterDayOption!
  """
  If `invoice_day` is not null, this allows you to select whether `due_days` is
  calculated from the billing day, or the invoice day.
  """
  due_days_day: BillingParameterDayOption!
  """
  Whether or not this account should be moved into another status after being delinquent for a preset period.
  """
  switch_status_after_delinquency: Boolean!
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
  """
  Determines if the billing parameters apply by account type or for anchor / linked types.
  """
  default_for: BillingDefaultFor = ACCOUNT_TYPE
  """
  Determines if delinquency settings on an Anchor default is applied only to the
  Anchor account or the Linked accounts as well.
  """
  anchor_delinquency_logic: AnchorDelinquencyLogic
  """
  Services specific to a Linked billing default. Includes the service, name
  override, price override, and anchor allowance of each.
  """
  billing_services: [BillingServiceMutationInput]
  """Whether or not to aggregate linked debits on Anchor invoices."""
  aggregate_linked_debits: Boolean
}

"""
The input object that defines the fields for the createBillingDefault mutation.
"""
input CreateBillingDefaultMutationInput {
  """A descriptive name."""
  name: String!
  """The ID of an AccountType."""
  account_type_id: Int64Bit
  """
  Whether or not to use a fixed bill day, versus anniversary day billing. Use `bill_day_mode` for further customization.
  """
  fixed_bill_day: Boolean
  """The day that billing runs."""
  bill_day: Int
  """The number of days after the invoice date that it is due."""
  due_days: Int!
  """
  The number of days after the invoice due date that the invoice is marked delinquent.
  """
  grace_days: Int!
  """
  The number of days after `auto_pay_day` that autopay runs for an invoice.
  """
  auto_pay_days: Int!
  """The number of months to bill at a time."""
  months_to_bill: Int!
  """Whether or not this account is tax exempt."""
  tax_exempt: Boolean!
  """The type of bill this account receives."""
  bill_mode: BillMode!
  """Whether this account receives a printed invoice."""
  print_invoice: Boolean!
  """
  The day that automatic billing invoices are generated for. If this is `null`, then `bill_day` is used.
  """
  invoice_day: Int
  """
  If `invoice_day` is not null, this allows you to select whether
  `auto_pay_days` is calculated from the billing day, or the invoice day.
  """
  auto_pay_day: BillingParameterDayOption!
  """
  If `invoice_day` is not null, this allows you to select whether `due_days` is
  calculated from the billing day, or the invoice day.
  """
  due_days_day: BillingParameterDayOption!
  """
  Whether or not this account should be moved into another status after being delinquent for a preset period.
  """
  switch_status_after_delinquency: Boolean!
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
  """
  Determines if the billing parameters apply by account type or for anchor / linked types.
  """
  default_for: BillingDefaultFor = ACCOUNT_TYPE
  """
  Determines if delinquency settings on an Anchor default is applied only to the
  Anchor account or the Linked accounts as well.
  """
  anchor_delinquency_logic: AnchorDelinquencyLogic
  """
  Services specific to a Linked billing default. Includes the service, name
  override, price override, and anchor allowance of each.
  """
  billing_services: [BillingServiceMutationInput]
  """Whether or not to aggregate linked debits on Anchor invoices."""
  aggregate_linked_debits: Boolean
  """The linked billing defaults for the anchor."""
  linked_billing_default: CreateBillingDefaultLinkedInput
}
```
