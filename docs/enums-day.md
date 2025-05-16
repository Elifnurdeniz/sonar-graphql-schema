```graphql
"""
The setting which dictates how the bill day and invoice day should be set when activating an account.
"""
enum BillDayModeOption {
  """Fixed bill day"""
  FIXED
  """Anniversary Invoice Day"""
  ANNIVERSARY_INVOICE_DAY
  """Anniversary Bill Day"""
  ANNIVERSARY_BILL_DAY
}
```
