```graphql
"""How a task gets marked as complete."""
enum TaskCompletionType {
  """Checking a box completes the task."""
  BOOLEAN
  """Providing the configured field value completes the task."""
  CUSTOM_FIELD
  """Attaching a file completes the task."""
  FILE
  """Attaching an image file completes the task."""
  IMAGE_FILE
}
```
