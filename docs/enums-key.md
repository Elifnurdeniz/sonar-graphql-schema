```graphql
"""Indicates what has been aggregated."""
enum AggregateKey {
  """The number of accounts with a given account status."""
  ACCOUNT_STATUS_COUNTS
  """The average revenue per user."""
  ARPU
  """The number of active customers."""
  ACTIVE_CUSTOMER_COUNT
  """The number of inactive customers."""
  INACTIVE_CUSTOMER_COUNT
  """The number customer accounts that are delinquent."""
  DELINQUENT_CUSTOMER_COUNT
  """The percentage of active customers who have delinquent accounts."""
  DELINQUENCY_PERCENTAGE
  """The total current recurring revenue."""
  RECURRING_REVENUE
  """The total current recurring discounts."""
  RECURRING_DISCOUNTS
  """The total debits for the day excluding adjustments."""
  DEBITS_WITHOUT_ADJUSTMENTS_TODAY
  """The total debits from adjustments for the day."""
  DEBIT_ADJUSTMENTS_TODAY
  """The total discounts/credits for the day excluding adjustments."""
  DISCOUNTS_WITHOUT_ADJUSTMENTS_TODAY
  """The total discounts/credits from adjustments for the day."""
  DISCOUNT_ADJUSTMENTS_TODAY
  """The total payments for the day."""
  PAYMENTS_TODAY
  """The total current amount due on invoices."""
  BALANCE_DUE
}
```
