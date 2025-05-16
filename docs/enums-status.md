```graphql
"""The status of a `Disbursement`."""
enum DisbursementStatus {
  """Requested"""
  REQUESTED
  """Processing"""
  PROCESSING
  """Processed"""
  PROCESSED
  """Failed"""
  FAILED
  """Denied"""
  DENIED
  """Returned"""
  RETURNED
}

"""The status of a `Dispute`."""
enum DisputeStatus {
  """Open"""
  OPEN
  """Closed"""
  CLOSED
  """Won"""
  WON
  """Lost"""
  LOST
}

"""The status of an `Email`."""
enum EmailStatus {
  """The email was sent successfully"""
  SENT
  """The email was sent to processor successfully"""
  SENT_TO_PROCESSOR
  """The email was bounced by the recipients mail server"""
  BOUNCED
  """The email was rejected by the recipients mail server"""
  REJECTED
  """
  The email failed to send through the mail processor. This indicates a fatal error
  """
  FAILED
  """The email was opened by the recipient"""
  OPENED
  """
  The email was sent, but the receiving server has indicated that emails are
  being delivered to it too quickly and that Mandrill should slow down sending temporarily
  """
  DEFERRED
  """
  The email was unable to be delivered because the recipient's email address is invalid
  """
  HARD_BOUNCED
  """
  The email was unable to be delivered because of a temporary issue with the recipient's inbox
  """
  SOFT_BOUNCED
  """The email recipient clicked a link in the email"""
  CLICKED
  """The email recipient marked the email as spam"""
  MARKED_SPAM
  """The email recipient unsubscribed from seeing any additional emails"""
  UNSUBBED
  """The email has been processed and is in progress."""
  IN_PROGRESS
}

"""The status of an import."""
enum ImportStatus {
  """The import is pending."""
  PENDING
  """The import is not valid."""
  INVALID
  """The import is queued for processing."""
  QUEUED
  """The import is running."""
  IN_PROGRESS
  """The import has successfully completed."""
  SUCCESSFUL
  """The import has failed."""
  FAILED
  """The import is a duplicate of a previously completed import."""
  DUPLICATE
  """The user is not authorized to access this data."""
  UNAUTHORIZED
}

"""The status of a `Payment`."""
enum PaymentStatus {
  """Pending"""
  PENDING
  """Failed"""
  FAILED
  """Succeeded"""
  SUCCEEDED
}

"""The status of a network device as reported by Preseem."""
enum PreseemStatus {
  """Red"""
  RED
  """Yellow"""
  YELLOW
  """Green"""
  GREEN
}

"""The status of current synchronization."""
enum SynchronizationStatus {
  """Never synchronized."""
  NEW
  """Audit in process."""
  AUDIT
  """Synchronization queued."""
  QUEUED
  """Synchronization started, collecting sync data."""
  STARTING
  """Synchronization in process."""
  SYNCING
  """Synchronization completed."""
  COMPLETED
  """Synchronization failed, see message for details."""
  ERROR
}

"""The status of a `Ticket`."""
enum TicketStatus {
  """Open."""
  OPEN
  """Closed."""
  CLOSED
  """Pending an update from an internal party."""
  PENDING_INTERNAL
  """Pending an update from an external party."""
  PENDING_EXTERNAL
}
```
