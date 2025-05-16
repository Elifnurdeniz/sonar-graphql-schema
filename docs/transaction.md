```graphql
"""types.transaction"""
type Transaction {
  """The ID of the entity."""
  id: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
  """
  An ID that uniquely identifies this entity across the whole Sonar system.
  """
  sonar_unique_id: ID!
  """The date and time this entity was created."""
  created_at: Datetime!
  """The last date and time this entity was modified."""
  updated_at: Datetime!
  """The type."""
  amount: Int!
  """A description for the transaction."""
  description: String
  """The date and time of the transaction."""
  datetime: Datetime
  """The balance in relation to prior transactions."""
  running_balance: Int!
  """The type of transaction this is."""
  type: TransactionType!
  """The total of all taxes on this transaction."""
  tax_total: Int!
  """A debit."""
  debit: Debit
  """A discount."""
  discount: Discount
  """A payment."""
  payment: Payment
  """A customer account."""
  account: Account!
  """Whether or not this was successful."""
  successful: Boolean
}

"""The connection wrapper around the `Transaction` type."""
type TransactionConnection {
  """A list of the entities provided by this connection."""
  entities: [Transaction]!
  """
  An object providing information about the page of results being displayed, as
  well as the total amount of pages/records available.
  """
  page_info: PageInfo!
}
```
