```graphql
"""
The input object that defines the fields for the updateBillingDefault mutation.
"""
input UpdateBillingDefaultLinkedInput {
  """A descriptive name."""
  name: String
  """The ID of an AccountType."""
  account_type_id: Int64Bit
  """
  Whether or not to use a fixed bill day, versus anniversary day billing. Use `bill_day_mode` for further customization.
  """
  fixed_bill_day: Boolean
  """The day that billing runs."""
  bill_day: Int
  """The number of days after the invoice date that it is due."""
  due_days: Int
  """
  The number of days after the invoice due date that the invoice is marked delinquent.
  """
  grace_days: Int
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
  """Setting this value to `true` will set `account_type_id` to null."""
  unset_account_type_id: Boolean
  """Setting this value to `true` will set `bill_day` to null."""
  unset_bill_day: Boolean
  """Setting this value to `true` will set `invoice_day` to null."""
  unset_invoice_day: Boolean
  """
  Setting this value to `true` will set `delinquency_removal_account_status_id` to null.
  """
  unset_delinquency_removal_account_status_id: Boolean
}

"""
The input object that defines the fields for the updateBillingDefault mutation.
"""
input UpdateBillingDefaultMutationInput {
  """A descriptive name."""
  name: String
  """The ID of an AccountType."""
  account_type_id: Int64Bit
  """
  Whether or not to use a fixed bill day, versus anniversary day billing. Use `bill_day_mode` for further customization.
  """
  fixed_bill_day: Boolean
  """The day that billing runs."""
  bill_day: Int
  """The number of days after the invoice date that it is due."""
  due_days: Int
  """
  The number of days after the invoice due date that the invoice is marked delinquent.
  """
  grace_days: Int
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
  linked_billing_default: UpdateBillingDefaultLinkedInput
  """Setting this value to `true` will set `account_type_id` to null."""
  unset_account_type_id: Boolean
  """Setting this value to `true` will set `bill_day` to null."""
  unset_bill_day: Boolean
  """Setting this value to `true` will set `invoice_day` to null."""
  unset_invoice_day: Boolean
  """
  Setting this value to `true` will set `delinquency_removal_account_status_id` to null.
  """
  unset_delinquency_removal_account_status_id: Boolean
}

"""
The input object that defines the fields for the updateBillingSettings mutation.
"""
input UpdateBillingSettingsMutationInput {
  """Whether or not service addition and removal is prorated by default."""
  prorate_services: Boolean
  """Whether or not service quantity changes are prorated by default."""
  prorate_service_quantity: Boolean
  """
  Whether or not changing the status from an active to inactive status is prorated by default.
  """
  prorate_account_status_change: Boolean
  """
  Whether or not an account going delinquent or no longer delinquent is prorated by default.
  """
  prorate_account_delinquency_status_change: Boolean
  """Whether or not changing an account bill day is prorated by default."""
  prorate_billing_day_change: Boolean
  """
  Whether or not to round prorated transactions to the nearest major unit (e.g. to the nearest dollar, euro, pound, etc.)
  """
  round_prorated_amounts: Boolean
  """The date that the accounting period was closed."""
  accounting_period_close_date: Date
  """How often the accounting period automatically closes."""
  accounting_period_auto_close: AccountingPeriodCloseOption
  """Monday."""
  delinquency_check_day_monday: Boolean
  """Tuesday."""
  delinquency_check_day_tuesday: Boolean
  """Wednesday."""
  delinquency_check_day_wednesday: Boolean
  """Thursday."""
  delinquency_check_day_thursday: Boolean
  """Friday."""
  delinquency_check_day_friday: Boolean
  """Saturday."""
  delinquency_check_day_saturday: Boolean
  """Sunday."""
  delinquency_check_day_sunday: Boolean
  """The smallest credit card payment amount allowed."""
  minimum_credit_card_payment: Int
  """The smallest bank account payment amount allowed."""
  minimum_bank_account_payment: Int
  """
  The minimum account an invoice must be delinquent for before being flagged delinquent.
  """
  minimum_amount_due_for_delinquency: Int
  """Whether or not to delete expired credit cards from Sonar."""
  delete_expired_credit_cards: Boolean
  """
  Whether the automatic payment process should just run the invoice amount, or the entire amount due on the account.
  """
  autopay_runs_entire_amount_due: Boolean
  """The number of times to attempt a credit card automatic payment."""
  autopay_credit_card_attempts: Int
  """The number of days between retries for credit card automatic payments."""
  autopay_credit_card_retry_interval_in_days: Int
  """The number of times to attempt a bank account automatic payment."""
  autopay_bank_account_attempts: Int
  """
  The number of days between retries for bank account automatic payments.
  """
  autopay_bank_account_retry_interval_in_days: Int
  """Autopay the initial invoice."""
  autopay_initial_invoice: Boolean
  """The number of days between invoice date and the Autopay date."""
  autopay_initial_invoice_days: Int64Bit
  """Autopay the account disconnect invoice."""
  autopay_disconnect_invoice: Boolean
  """The number of days between invoice date and the Autopay date."""
  autopay_disconnect_invoice_days: Int
  """Whether or not the daily billing process is enabled."""
  daily_billing: Boolean
  """
  The service ID of a one time `Service` to charge for accounts with
  `print_invoice` enabled in their `AccountBillingParameter`.
  """
  printed_invoice_fee_service_id: Int64Bit
  """The `AccountStatus` for disconnected accounts."""
  disconnect_account_status_id: Int64Bit
  """Whether or not to apply a late fee to past due invoices."""
  apply_late_fees: Boolean
  """Whether late fees should be applied to child invoices."""
  apply_late_fees_to_child_invoices: Boolean
  """
  Whether to invoice and email late fees immediately, or add them to the next invoice.
  """
  invoice_and_email_late_fees_immediately: Boolean
  """Whether to exclude inactive accounts from late fee application."""
  exclude_inactive_accounts_from_late_fees: Boolean
  """The ID of a one time `Service` to use for late fee application."""
  late_fee_service_id: Int64Bit
  """The mode for late fee application."""
  late_fee_mode: LateFeeMode
  """
  If late fees are applied as a percentage, the percentage of the past due balance to apply.
  """
  late_fee_percentage: Float
  """
  The minimum amount an invoice must be past due for a late fee to be applied.
  """
  late_fee_minimum_delinquency_amount: Int
  """
  The number of days after the due date on a delinquent invoice for a late fee to be applied.
  """
  days_after_invoice_due_for_late_fee_application: Int
  """Accounts of these types will be excluded from late fee application."""
  account_type_ids_to_exclude_from_late_fees: [Int64Bit]
  """
  Generate an invoice on an account when it is first activated, if there are any uninvoiced debits.
  """
  generate_invoice_on_initial_activation: Boolean
  """Always round taxes up."""
  always_round_taxes_up: Boolean
  """Printed invoice batch duplex."""
  printed_invoice_batch_duplex: Boolean
  """Use modular invoice templates for all invoices."""
  use_invoice_templates: Boolean
  """Whether or not to include late fee invoices in printed batches."""
  include_late_fee_invoices_in_printed_batches: Boolean
  """The `AccountStatus` for unarchived accounts."""
  unarchive_account_status_id: Int64Bit
  """
  Setting this value to `true` will set `printed_invoice_fee_service_id` to null.
  """
  unset_printed_invoice_fee_service_id: Boolean
  """
  Setting this value to `true` will set `unarchive_account_status_id` to null.
  """
  unset_unarchive_account_status_id: Boolean
}
```
