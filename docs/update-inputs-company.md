```graphql
"""
The input object that defines the fields for the updateCompany mutation.
"""
input UpdateCompanyMutationInput {
  """A descriptive name."""
  name: String
  """The address of the company website."""
  website_address: URL
  """A telephone number."""
  phone_number: Numeric
  """The primary color to use in Sonar."""
  primary_color: HtmlHexColor
  """The secondary color to use in Sonar."""
  secondary_color: HtmlHexColor
  """Whether or not this entity is a default entry."""
  default: Boolean
  """Whether or not this is enabled."""
  enabled: Boolean
  """A two character country code."""
  country: Country
  """
  A tax identification number. Should only be entered if you are required to
  share some type of tax identification information with your customers.
  """
  tax_identification: String
  """Whether or not to include a detachable remittance slip on the invoice."""
  show_remittance_slip: Boolean
  """On an enabled remittance slip, who should checks be made payable to?"""
  checks_payable_to: String
  """
  The address shown on the invoice, and on the remittance slip, if it is enabled.
  """
  address: UpdateOrCreateAddressMutationInput
  """
  The IDs of `CustomField`s that should be displayed on invoices. A maximum of 3
  fields can be selected, and they must all be associated with `Account`s.
  """
  custom_field_ids: [Int64Bit]
  """The URL to your customer portal."""
  customer_portal_url: URL
  """The ISP type of this `Company`."""
  isp_type: IspType
  """Departments."""
  departments: [CompanyDepartmentInput]
  """
  The daily start time of the period during which billing communication e.g. new
  invoices, delinquency, etc. will not be sent.
  """
  billing_communication_delay_start_local_time: Time
  """
  The daily end time of the period during which billing communication e.g. new invoices, delinquency, etc. will not be sent.
  """
  billing_communication_delay_end_local_time: Time
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """Setting this value to `true` will set `tax_identification` to null."""
  unset_tax_identification: Boolean
  """Setting this value to `true` will set `checks_payable_to` to null."""
  unset_checks_payable_to: Boolean
  """Setting this value to `true` will set `customer_portal_url` to null."""
  unset_customer_portal_url: Boolean
  """Setting this value to `true` will set `isp_type` to null."""
  unset_isp_type: Boolean
  """Setting this value to `true` will set `website_address` to null."""
  unset_website_address: Boolean
  """Setting this value to `true` will set `phone_number` to null."""
  unset_phone_number: Boolean
  """
  Setting this value to `true` will set `billing_communication_delay_start_local_time` to null.
  """
  unset_billing_communication_delay_start_local_time: Boolean
  """
  Setting this value to `true` will set `billing_communication_delay_end_local_time` to null.
  """
  unset_billing_communication_delay_end_local_time: Boolean
}
```
