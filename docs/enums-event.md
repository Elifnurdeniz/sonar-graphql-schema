```graphql
"""The type of event being fired by this `ScheduledEvent`."""
enum ScheduledEventEvent {
  """Make a credit card payment."""
  CREDIT_CARD_PAYMENT
  """Make a bank account payment."""
  BANK_ACCOUNT_PAYMENT
  """Remove a service."""
  REMOVE_SERVICE
  """Add a service."""
  ADD_SERVICE
  """Change the account status."""
  CHANGE_STATUS
  """Price override an existing service on the account."""
  ADD_PRICE_OVERRIDE
  """Remove a price override from a service on the account."""
  REMOVE_PRICE_OVERRIDE
  """Add a package."""
  ADD_PACKAGE
  """Remove a package."""
  REMOVE_PACKAGE
  """Disconnect an Account"""
  DISCONNECT_ACCOUNT
  """Apply a one time transaction from a service"""
  ONE_TIME_TRANSACTION
  """Assign a serviceable address to an account"""
  ASSIGN_SERVICEABLE_ADDRESS
}
```
