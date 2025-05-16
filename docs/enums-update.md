```graphql
"""An account update event."""
enum AccountUpdateEvent {
  """Account activated"""
  ACTIVATED
  """Account archived"""
  ARCHIVED
  """Account groups removed"""
  GROUPS_REMOVED
  """Account groups added"""
  GROUPS_ADDED
  """Account services added"""
  SERVICES_ADDED
  """Account services removed"""
  SERVICES_REMOVED
  """Account services updated"""
  SERVICES_UPDATED
  """Account status updated"""
  STATUS_UPDATED
  """Account type updated"""
  TYPE_UPDATED
  """Account unarchived"""
  UNARCHIVED
  """Credit card added"""
  CREDIT_CARD_ADDED
  """Credit card updated"""
  CREDIT_CARD_UPDATED
  """Credit card removed"""
  CREDIT_CARD_REMOVED
}
```
