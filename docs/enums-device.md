```graphql
"""An inline device authentication credential."""
enum InlineDeviceAuthenticationCredential {
  """MikroTik username."""
  MIKROTIK_USERNAME
  """MikroTik password."""
  MIKROTIK_PASSWORD
  """PacketLogic username."""
  PACKETLOGIC_USERNAME
  """PacketLogic password."""
  PACKETLOGIC_PASSWORD
  """PacketLogic master object name."""
  PACKETLOGIC_MASTER_OBJECT_NAME
}

"""The type of inline device."""
enum InlineDeviceType {
  """MikroTik."""
  MIKROTIK
  """Procera/Sandvine PacketLogic."""
  PACKETLOGIC
}

"""The status of a device that performs some kind of provisioning."""
enum ProvisioningDeviceStatus {
  """Up."""
  UP
  """Down."""
  DOWN
}
```
