```graphql
"""The input object that defines the fields for the updateJob mutation."""
input UpdateJobMutationInput {
  """The ID of a `JobType`."""
  job_type_id: Int64Bit
  """The ID of a `Ticket`."""
  ticket_id: Int64Bit
  """The date and time this `Job` is scheduled for."""
  scheduled_datetime: Datetime
  """The length in minutes for this `Job`."""
  length_in_minutes: Int
  """The type of entity that this `Job` is associated with."""
  jobbable_type: JobbableType
  """The ID of the entity that this `Job` is associated with."""
  jobbable_id: Int64Bit
  """IDs of `User`s."""
  user_ids: [Int64Bit]
  """Any notes entered when this `Job` was completed."""
  completion_notes: Text
  """
  If this is `true` then the new `JobType`'s task template will be applied and existing uncompleted tasks will be removed.
  """
  replace_existing_tasks: Boolean
  """The ID of the serviceable address account assignment future."""
  serviceable_address_account_assignment_future_id: Int64Bit
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """The task to be performed."""
  tasks: [TaskMutationInput]
  """Setting this value to `true` will set `ticket_id` to null."""
  unset_ticket_id: Boolean
  """Setting this value to `true` will set `scheduled_datetime` to null."""
  unset_scheduled_datetime: Boolean
  """Setting this value to `true` will set `completion_notes` to null."""
  unset_completion_notes: Boolean
  """
  Setting this value to `true` will set `serviceable_address_account_assignment_future_id` to null.
  """
  unset_serviceable_address_account_assignment_future_id: Boolean
}

"""
The input object that defines the fields for the updateJobService mutation.
"""
input UpdateJobServiceMutationInput {
  """The quantity for this service."""
  quantity: Int!
}

"""
The input object that defines the fields for the updateJobType mutation.
"""
input UpdateJobTypeMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The default length for a `Job` created using this `JobType`."""
  default_length_in_minutes: Int
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor
  """An icon."""
  icon: Icon
  """
  Whether `Job`s associated with this `JobType` should be able to be completed with incomplete tasks.
  """
  allow_completion_with_incomplete_tasks: Boolean
  """Whether or not this `JobType` is valid for all `Companies`."""
  all_companies: Boolean
  """
  If this is set, any `Job` using this `JobType` that is completed successfully
  while associated with an `Account` will trigger the disconnection of the `Account`.
  """
  disconnects_account: Boolean
  """
  If this is set, any `Job` using this `JobType` that is completed successfully
  while associated with an `Account` will change the `Account` to this
  `AccountStatus`.
  """
  account_status_id_completion: Int64Bit
  """
  If this is set, any `Job` using this `JobType` that is completed
  unsuccessfully while associated with an `Account` will change the `Account` to
  this `AccountStatus`.
  """
  account_status_id_failure: Int64Bit
  """
  If this is set, any `Job` using this `JobType` that is completed successfully
  will create a `Ticket` and assign it to this `TicketGroup`.
  """
  ticket_group_id_completion: Int64Bit
  """
  If this is set, any `Job` using this `JobType` that is completed
  unsuccessfully will create a `Ticket` and assign it to this `TicketGroup`.
  """
  ticket_group_id_failure: Int64Bit
  """The ID of a `ContractTemplate`."""
  contract_template_id: Int64Bit
  """The ID of a `TaskTemplate`."""
  task_template_id: Int64Bit
  """IDs of `Companies`."""
  company_ids: [Int64Bit]
  """IDs of `Service`s."""
  service_ids: [Int64Bit]
  """Completion ticket action."""
  action_on_completion: JobTypeAction
  """Failure ticket action."""
  action_on_failure: JobTypeAction
  """Ticket status on completion."""
  ticket_status_on_completion: TicketStatus
  """Ticket status on failure."""
  ticket_status_on_failure: TicketStatus
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `account_status_id_completion` to null.
  """
  unset_account_status_id_completion: Boolean
  """
  Setting this value to `true` will set `account_status_id_failure` to null.
  """
  unset_account_status_id_failure: Boolean
  """
  Setting this value to `true` will set `ticket_group_id_completion` to null.
  """
  unset_ticket_group_id_completion: Boolean
  """
  Setting this value to `true` will set `ticket_group_id_failure` to null.
  """
  unset_ticket_group_id_failure: Boolean
  """Setting this value to `true` will set `contract_template_id` to null."""
  unset_contract_template_id: Boolean
  """Setting this value to `true` will set `task_template_id` to null."""
  unset_task_template_id: Boolean
}
```
