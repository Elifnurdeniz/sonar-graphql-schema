```graphql
"""The type of ACH batch (credits or debits)."""
enum AchBatchType {
  """Debits."""
  DEBIT
  """Credits."""
  CREDIT
  """
  Both credits and debits. These are no longer generated, this is a legacy type from Sonar v1.x.
  """
  BOTH
}
```
