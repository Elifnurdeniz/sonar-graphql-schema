```graphql
"""The `ExternalMarketingProvider` credentials for integration."""
enum ExternalMarketingProviderAuthCredential {
  """MarketBroadband.com account number."""
  MARKET_BROADBAND_ACCOUNT_NUMBER
  """MarketBroadband.com radius mailing quantity."""
  MARKET_BROADBAND_RADIUS_MAILING_QUANTITY
}

"""
A `ExternalMarketingProviderType` for `ExternalMarketingProvider` 3rd party integration.
"""
enum ExternalMarketingProviderType {
  """A 3rd party marketing provider called MarketBroadband.com."""
  MARKET_BROADBAND
}
```
