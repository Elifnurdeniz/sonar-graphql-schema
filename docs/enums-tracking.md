```graphql
"""`GpsTrackingProvider` credentials."""
enum GpsTrackingProviderAuthCredential {
  """Geotab username"""
  GEOTAB_USERNAME
  """Geotab password"""
  GEOTAB_PASSWORD
  """Geotab database"""
  GEOTAB_DATABASE
  """Geotab session ID"""
  GEOTABSESSIONID
  """Linxup username"""
  LINXUP_USERNAME
  """Linxup password"""
  LINXUP_PASSWORD
  """Linxup API access URL"""
  LINXUP_APIURL
  """Linxup access token"""
  LINXUPACCESSTOKEN
  """Test username - Use `test` to pass"""
  TEST_USERNAME
  """Test password - Use `password` to pass"""
  TEST_PASSWORD
  """Test API token generated with correct username and password"""
  TESTAPITOKEN
  """Track Your Truck client ID"""
  TRACKYOURTRUCK_CLIENTID
  """Track Your Truck PIN"""
  TRACKYOURTRUCK_PIN
  """Track Your Truck access token"""
  TRACKYOURTRUCKACCESSTOKEN
  """Verizon Connect client ID"""
  VERIZONCONNECT_CLIENTID
  """Verizon Connect client secret"""
  VERIZONCONNECT_CLIENTSECRET
  """Verizon Connect OAuth access token"""
  VERIZONCONNECTACCESSTOKEN
  """Verizon Connect OAuth refresh token"""
  VERIZONCONNECTREFRESHTOKEN
  """Zubie client ID"""
  ZUBIE_CLIENTID
  """Zubie client secret"""
  ZUBIE_CLIENTSECRET
  """Zubie OAuth access token"""
  ZUBIEACCESSTOKEN
  """Zubie OAuth refresh token"""
  ZUBIEREFRESHTOKEN
}

"""A `GpsTrackingProvider` type."""
enum GpsTrackingProviderType {
  """Geotab"""
  GEOTAB
  """Linxup"""
  LINXUP
  """Track Your Truck"""
  TRACKYOURTRUCK
  """Verizon Connect"""
  VERIZONCONNECT
  """Zubie"""
  ZUBIE
}
```
