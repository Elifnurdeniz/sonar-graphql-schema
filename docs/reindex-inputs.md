```graphql
"""
The input object that defines the fields for the reindexModel mutation.
"""
input ReindexModelMutationInput {
  """The id of the model to reindex."""
  model_id: Int64Bit!
  """The type of the model to reindex."""
  model_type: IndexedModelType!
  """Indicates whether the index should be deleted instead of updated."""
  delete_index: Boolean! = false
}
```
