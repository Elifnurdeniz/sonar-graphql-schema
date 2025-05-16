```graphql
"""
The input object that defines the fields for the updatePasswordPolicy mutation.
"""
input UpdatePasswordPolicyMutationInput {
  """The minimum length a password must be."""
  minimum_length: Int
  """Does a password require both upper and lower case characters?"""
  requires_upper_and_lower_case_characters: Boolean
  """
  Does a password require at least one special (non alpha-numeric) character?
  """
  requires_at_least_one_special_character: Boolean
  """
  Must a password be alpha-numeric (contain at least one letter and one number)
  or can it have any combination of characters?
  """
  requires_alpha_numeric: Boolean
  """
  A score for the zxcvbn password strength estimation library that this password
  must match. 0 allows all passwords, 4 requires a very strong password. See
  https://github.com/dropbox/zxcvbn for details.
  """
  minimum_password_strength: Int
}
```
