```graphql
"""
The priority of the `Note`. Sticky forces it to the top of the note list. Popup forces the note to popup on the screen.
"""
enum NotePriority {
  """A normal priority"""
  NORMAL
  """A sticky note is forced to the top of the list"""
  STICKY
  """Popup notes will popup immediately when the owning entity is accessed"""
  STICKY_WITH_CONFIRMATION
}

"""The priority of a `Ticket`."""
enum TicketPriority {
  """Low."""
  LOW
  """Medium."""
  MEDIUM
  """High."""
  HIGH
  """Critical."""
  CRITICAL
}
```
