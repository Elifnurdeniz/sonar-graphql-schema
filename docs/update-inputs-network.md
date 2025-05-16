```graphql
"""
The input object that defines the fields for the updateNetworkMonitoringGraph mutation.
"""
input UpdateNetworkMonitoringGraphMutationInput {
  """A descriptive name."""
  name: String
  """The type."""
  type: NetworkMonitoringGraphType
  """Stacked"""
  stacked: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateNetworkMonitoringTemplate mutation.
"""
input UpdateNetworkMonitoringTemplateMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not to collect interface statistics."""
  collect_interface_statistics: Boolean
  """Whether or not ICMP monitoring is enabled."""
  icmp_monitoring: Boolean
  """ICMP latency threshold (ms)."""
  icmp_latency_threshold: Int
  """ICMP loss threshold (%)."""
  icmp_loss_threshold: Int
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
  """
  Setting this value to `true` will set `icmp_latency_threshold` to null.
  """
  unset_icmp_latency_threshold: Boolean
  """Setting this value to `true` will set `icmp_loss_threshold` to null."""
  unset_icmp_loss_threshold: Boolean
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

"""Update the address details for a network site."""
input UpdateNetworkSiteAddressMutationInput {
  """Address line 1."""
  line1: String
  """Address line 2."""
  line2: String
  """A city."""
  city: String
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String
  """A two character country code."""
  country: Country
  """A decimal latitude."""
  latitude: Latitude
  """A decimal longitude."""
  longitude: Longitude
  """The timezone you want times in the system displayed in."""
  timezone: Timezone
}

"""
The input object that defines the fields for the updateNetworkSite mutation.
"""
input UpdateNetworkSiteMutationInput {
  """A descriptive name."""
  name: String
  """Height in meters."""
  height_in_meters: Float
  """The address for the network site."""
  address: UpdateNetworkSiteAddressMutationInput
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """The task to be performed."""
  tasks: [TaskMutationInput]
}
```
