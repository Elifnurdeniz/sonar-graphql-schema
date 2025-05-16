```graphql
"""Determines how delinquency on the Anchor is handled."""
enum AnchorDelinquencyLogic {
  """Anchor Delinquency also applies to Linked"""
  ALL
  """Linked not affected by Anchor Delinquency"""
  ANCHOR_ONLY
}
```
