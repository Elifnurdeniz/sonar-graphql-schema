```graphql
"""The status of a print to mail batch."""
enum PrintToMailBatchStatus {
  """Pending (Waiting to be processed)"""
  PENDING
  """Insufficient funds."""
  INSUFFICIENT_FUNDS
  """In Progress."""
  IN_PROGRESS
  """Completed."""
  COMPLETED
  """Failed."""
  FAILED
  """Cancelled."""
  CANCELLED
}

"""The batch type of a print to mail batch."""
enum PrintToMailBatchType {
  """Created by a billing run."""
  BILLING_RUN
  """Manually created."""
  USER_DEFINED
}

"""The error type associated with the print to mail order."""
enum PrintToMailOrderErrorType {
  """Address"""
  ADDRESS
  """General"""
  GENERAL
}

"""The status of a print to mail order."""
enum PrintToMailOrderStatus {
  """Sent"""
  SENT
  """Error"""
  ERROR
  """Complete"""
  COMPLETE
  """Cancelled"""
  CANCELLED
}

"""The print method for a print to mail batch."""
enum PrintToMailPrintMethod {
  """Print on one side of the page."""
  SIMPLEX
  """Print on both sides of the page."""
  DUPLEX
}

"""The print type for a print to mail batch."""
enum PrintToMailPrintType {
  """Print in black and white."""
  BLACK_AND_WHITE
  """Print in color."""
  COLOR
}
```
