```graphql
"""The category of an outbound SMS."""
enum SmsOutboundCategory {
  """Notification"""
  NOTIFICATION
  """Mass message"""
  MASS_MESSAGE
  """Trigger"""
  TRIGGER
  """Authentication"""
  AUTHENTICATION
}

"""The status of an outbound SMS."""
enum SmsOutboundStatus {
  """Pending (Waiting to be processed)."""
  PENDING
  """Insufficient funds."""
  INSUFFICIENT_FUNDS
  """In Progress."""
  IN_PROGRESS
  """Delivered."""
  DELIVERED
  """Sent."""
  SENT
  """Failed."""
  FAILED
}
```
