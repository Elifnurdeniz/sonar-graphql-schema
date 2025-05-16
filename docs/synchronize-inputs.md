```graphql
"""
The input object that defines the fields for the synchronizeCableModemProvisioner mutation.
"""
input SynchronizeCableModemProvisionerMutationInput {
  """The ID of a `CableModemProvisioner`."""
  cable_modem_provisioner_id: Int64Bit!
}

"""
The input object that defines the fields for the synchronizeCalixCloud mutation.
"""
input SynchronizeCalixCloudMutationInput {
  """The ID of a `CalixCloudSetting`."""
  calix_cloud_setting_id: Int64Bit!
}

"""
The input object that defines the fields for the synchronizeDhcpServer mutation.
"""
input SynchronizeDhcpServerMutationInput {
  """The ID of a `DhcpServer`."""
  dhcp_server_id: Int64Bit!
}

"""
The input object that defines the fields for the synchronizeInlineDevice mutation.
"""
input SynchronizeInlineDeviceMutationInput {
  """The ID of an `InlineDevice`."""
  inline_device_id: Int64Bit!
}

"""
The input object that defines the fields for the synchronizeLteProvider mutation.
"""
input SynchronizeLteProviderMutationInput {
  """The ID of an `LteProvider`."""
  lte_provider_id: Int64Bit!
}

"""
The input object that defines the fields for the synchronizeRadiusServer mutation.
"""
input SynchronizeRadiusServerMutationInput {
  """The ID of a `RadiusServer`."""
  radius_server_id: Int64Bit!
}
```
