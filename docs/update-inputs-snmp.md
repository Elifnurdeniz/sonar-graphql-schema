```graphql
"""
The input object that defines the fields for the updateSnmpOid mutation.
"""
input UpdateSnmpOidMutationInput {
  """A descriptive name."""
  name: String
  """An OID"""
  oid: String
  """Whether or not to auto scale."""
  auto_scale: Boolean
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor
  """Divide by"""
  divide_by: Int
  """Display as table"""
  display_as_table: Boolean
  """Unit of measurement"""
  unit_of_measurement: String
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `divide_by` to null."""
  unset_divide_by: Boolean
  """Setting this value to `true` will set `unit_of_measurement` to null."""
  unset_unit_of_measurement: Boolean
}

"""
The input object that defines the fields for the updateSnmpOidThreshold mutation.
"""
input UpdateSnmpOidThresholdMutationInput {
  """
  An operator that defines how to apply the threshold value to the attribute.
  """
  operator: RangeOperator
  """The value."""
  value: String
  """
  The amount of time in minutes that the threshold must be violated before it is triggered.
  """
  time_period_in_minutes: Int
  """The ID of an `SnmpOid`."""
  snmp_oid_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateSnmpOverride mutation.
"""
input UpdateSnmpOverrideMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
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
  """Setting this value to `true` will set `snmp_version` to null."""
  unset_snmp_version: Boolean
  """Setting this value to `true` will set `snmp_community` to null."""
  unset_snmp_community: Boolean
  """Setting this value to `true` will set `snmp3_sec_level` to null."""
  unset_snmp3_sec_level: Boolean
  """Setting this value to `true` will set `snmp3_auth_protocol` to null."""
  unset_snmp3_auth_protocol: Boolean
  """Setting this value to `true` will set `snmp3_auth_passphrase` to null."""
  unset_snmp3_auth_passphrase: Boolean
  """Setting this value to `true` will set `snmp3_priv_protocol` to null."""
  unset_snmp3_priv_protocol: Boolean
  """Setting this value to `true` will set `snmp3_priv_passphrase` to null."""
  unset_snmp3_priv_passphrase: Boolean
  """Setting this value to `true` will set `snmp3_context_name` to null."""
  unset_snmp3_context_name: Boolean
  """
  Setting this value to `true` will set `snmp3_context_engineid` to null.
  """
  unset_snmp3_context_engineid: Boolean
}
```
