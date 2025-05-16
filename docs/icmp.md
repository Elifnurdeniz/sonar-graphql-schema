```graphql
"""types.icmp_network_monitoring_result_connection"""
type IcmpNetworkMonitoringResultConnection {
  """fields.network_monitoring_template"""
  network_monitoring_template: NetworkMonitoringTemplate
  """The ID of an `InventoryItem`."""
  inventory_item_id: Int64Bit!
  """fields.icmp_results"""
  icmp_results: [IcmpResult]!
  """fields.icmp_status_results"""
  icmp_status_results: [IcmpStatusResult]!
}

"""types.icmp_result"""
type IcmpResult {
  """The time."""
  time: Datetime
  """The high latency."""
  high: Float
  """The low latency."""
  low: Float
  """The median latency."""
  median: Float
  """The loss percentage."""
  loss: Float
  """A Unix timestamp in the same timezone as this Sonar instance"""
  epoch_system_timezone: EpochTimestamp
}

"""types.icmp_status_result"""
type IcmpStatusResult {
  """The time."""
  time: Datetime
  """The status."""
  status: String
  """The reason."""
  reason: String
  """A Unix timestamp in the same timezone as this Sonar instance"""
  epoch_system_timezone: EpochTimestamp
}
```
