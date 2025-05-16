```graphql
"""Status of a purchase order item."""
enum PurchaseOrderItemStatus {
  """Pending"""
  PENDING
  """Received"""
  RECEIVED
  """Defective/Return Merchandise Authorization"""
  DEFECTIVE_RMA
  """Missing"""
  MISSING
  """Canceled"""
  CANCELED
  """Returned"""
  RETURNED
}

"""Status of a purchase order / product request."""
enum PurchaseOrderStatus {
  """Product Request"""
  PRODUCT_REQUEST
  """Approved"""
  APPROVED
  """Dispatched to vendor"""
  DISPATCHED_TO_VENDOR
  """Failed to dispatch"""
  DISPATCH_FAILED
  """Receiving"""
  RECEIVING
  """Incomplete"""
  INCOMPLETE
  """Complete"""
  COMPLETE
  """Canceled"""
  CANCELED
  """Rejected"""
  REJECTED
  """Paid"""
  PAID
  """Uninitialized"""
  UNINITIALIZED
}
```
