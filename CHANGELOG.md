## v1.0
### Changed
- `check_password`: now requires at least 10 characters instead of 8. Passwords of 8 or 9 characters that were accepted before are now rejected. (#1)
- `is_valid_email`: now requires both "@" and "." in the address. Addresses without a "." are now rejected. (#2)
### Fixed
- `count_vowels`: now also counts uppercase vowels, so `count_vowels("ANA")` returns 2 instead of 0. (#3)
