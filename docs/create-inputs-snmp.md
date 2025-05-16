```graphql
"""
The input object that defines the fields for the createSnmpOid mutation.
"""
input CreateSnmpOidMutationInput {
  """A descriptive name."""
  name: String!
  """An OID"""
  oid: String!
  """Whether or not to auto scale."""
  auto_scale: Boolean = false
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor = "3498db"
  """Divide by"""
  divide_by: Int
  """Display as table"""
  display_as_table: Boolean = false
  """Unit of measurement"""
  unit_of_measurement: String
  """The ID of a `NetworkMonitoringGraph`."""
  network_monitoring_graph_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createSnmpOidThreshold mutation.
"""
input CreateSnmpOidThresholdMutationInput {
  """
  An operator that defines how to apply the threshold value to the attribute.
  """
  operator: RangeOperator!
  """The value."""
  value: String!
  """
  The amount of time in minutes that the threshold must be violated before it is triggered.
  """
  time_period_in_minutes: Int!
  """The ID of an `SnmpOid`."""
  snmp_oid_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createSnmpOverride mutation.
"""
input CreateSnmpOverrideMutationInput {
  """The ID of an `InventoryItem`."""
  inventory_item_id: Int64Bit!
  """SNMP version"""
  snmp_version: SnmpVersion
  """SNMP community/securityName"""
  snmp_community: String
  """SNMPv3 security level"""
  snmp3_sec_level: Snmp3SecurityLevel
  """SNMPv3 auth protocol"""
  snmp3_auth_protocol: Snmp3AuthProtocol
  """SNMPv3 auth passphrase"""
  snmp3_auth_passphrase: String
  """SNMPv3 privacy protocol"""
  snmp3_priv_protocol: Snmp3PrivProtocol
  """SNMPv3 privacy passphrase"""
  snmp3_priv_passphrase: String
  """SNMPv3 context name"""
  snmp3_context_name: String
  """SNMPv3 context engine ID"""
  snmp3_context_engineid: String
  """A note about this entity."""
  note: NoteMutationInput
}
```
