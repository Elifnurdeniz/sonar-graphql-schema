```graphql
"""Precision of the costs associated with the funded service."""
enum FundedServiceCostPrecision {
  """Smallest denomination."""
  SMALLEST_DENOMINATION
  """Hundredths."""
  HUNDREDTHS
}

"""The instance service fund type"""
enum InstanceServiceFundType {
  """Print To Mail"""
  PRINT_TO_MAIL
  """SMS"""
  SMS
}

"""The sub type of a voice service."""
enum VoiceServiceDetailSubType {
  """Voice"""
  VOICE
  """Hosted PBX"""
  HOSTED_PBX
}

"""The type of configurable attribute for a voice service."""
enum VoiceServiceGenericParameterType {
  """Lines"""
  LINES
  """PBX Seats"""
  PBX_SEATS
  """Other"""
  OTHER
}
```
