```graphql
"""The `AccountingPeriodCloseOption` that is in use."""
enum AccountingPeriodCloseOption {
  """Never close the accounting period automatically"""
  NEVER
  """Close every Monday at 12AM"""
  MONDAY
  """Close every Tuesday at 12AM"""
  TUESDAY
  """Close every Wednesday at 12AM"""
  WEDNESDAY
  """Close every Thursday at 12AM"""
  THURSDAY
  """Close every Friday at 12AM"""
  FRIDAY
  """Close every Saturday at 12AM"""
  SATURDAY
  """Close every Sunday at 12AM"""
  SUNDAY
  """Close every day at 12AM"""
  DAILY
  """Close on the first day of every month at 12AM"""
  MONTHLY
}
```
