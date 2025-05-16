```graphql
"""The monitoring status of an `InventoryItem`."""
enum InventoryItemDeviceStatus {
  """The device is in a healthy state."""
  GOOD
  """The device is down."""
  DOWN
  """The device is in a warning state."""
  WARNING
}

"""The ICMP monitoring threshold violation type of an `InventoryItem`."""
enum InventoryItemIcmpThresholdViolation {
  """Total packet loss."""
  TOTAL_PACKET_LOSS
  """ICMP loss threshold violated."""
  LOSS_THRESHOLD_VIOLATED
  """ICMP latency threshold violated."""
  LATENCY_THRESHOLD_VIOLATED
  """ICMP loss and latency thresholds violated."""
  LOSS_AND_LATENCY_THRESHOLD_VIOLATED
}

"""
Determines how updates or deletions to an inventory item segment are handled.
"""
enum InventoryItemSegmentModifierType {
  """Parent inventory item affected."""
  PARENT
  """New segment to be created."""
  NEW
  """Segment to be deleted."""
  DELETE
}

"""The physical status of an inventory item."""
enum InventoryItemStatus {
  """Failed."""
  FAILED
  """Lost."""
  LOST
  """Functional."""
  FUNCTIONAL
}

"""An inventory item update event."""
enum InventoryItemUpdateEvent {
  """Inventory item assignment updated"""
  ASSIGNED
}
```
