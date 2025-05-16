```graphql
"""The authentication factor type."""
enum AuthenticationFactorType {
  """Receive one-time passcodes via email"""
  EMAIL
  """Receive one-time passcodes via SMS"""
  SMS
  """
  Generate time-based one-time passcodes with a user-configured application
  """
  TOTP
  """
  Generate a set of single-use codes for use when no other authentication factors are available
  """
  RECOVERY_CODES
}
```
