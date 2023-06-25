# Changelog

All notable changes to this project will be documented in this file starting from version 0.1.3.

Please note that this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). As carter-py is built around an API which is still in beta, breaking changes may be introduced indirectly in minor releases. Major releases will be reserved for breaking changes to the way in carter-py is used. IE. function names, parameter depreciations etc. Where a breaking change is made on the API side, carter-py will be updated to reflect this change.

I will continue to build carter-py with the intention of maintaining backwards compatibility, but this is not guaranteed. Previous versions of carter-py are always likely to be outdated as the API progresses. Please consult the changelog for any breaking changes and try to use the latest version of carter-py.

## [1.01] 2023-06-01 - Switches back to Carter stable URLs

This release has bumped a minor version number to reflect a change in the API.

### Changed

- All URLs have been changed back to the stable API (previously unstable)

## [1.0] - 2023-05-01 - Switches to Carter Unstable API

This release has bumped a major version number to reflect both major usage changes as well as a milestone in the API.

### Changed

- All methods now use the unstable API. This change doesn't affect usage but allows carter-py users to benefit from the latest features.
- The `player_id` parameter has been renamed to `user_id` in all methods to reflect the change in the API. THIS CHANGE IS BREAKING
- `carter.personalise()` now requires a `user_id` parameter. THIS CHANGE IS BREAKING.

## [0.2.0] - 2023-04-28

### Changed

- Updated the `speak` parameter to be false by default when creating a carter

## [0.1.3] - 2023-04-19

### Added

- Created `CHANGELOG.md` to track project changes from version 0.1.3 onwards.
- Added the speak parameter to both carter classes. This allows you to set the default behaviour of the `speak` parameter on all methods. This can be overridden on a per-method basis.

### Changed

- No Changes

### Fixed

- Fixed first readme example to use the correct import statement.

### Removed

- Nothing removed.
