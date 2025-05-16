```graphql
"""The level of severity of a `Log` entry."""
enum LogLevel {
  """
  An informational message is one where the normal operation of the system has
  been observed, and some information has been stored for future reference
  """
  INFO
  """
  An error message is one where an error occurred that was unexpected or could
  not be resolved by the underlying process, and a log has been stored for
  future reference
  """
  ERROR
  """
  A critical message is one where an underlying Sonar process failed in an
  unexpected or unallowed manner. Notifications of this level automatically
  notify Sonar support
  """
  CRITICAL
}
```
