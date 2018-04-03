# Base64 Decode Popup
This utility displays the contents of Base64 and Base64Url encoded strings
selected in files.

# To Install
This plugin is not yet available on package control. Until it is, manual
installation can be performed by:

1. Clone this repo.
2. Navigate to your package installation directory (You can do this by opening
sublime text and Navigating to `Preferences` --> `Browse Packages`).
4. Copy the `base64_decode_popup` directory into the installation
directory.

Optionally, if you are using Linux, just run `install.sh`, which will do the
same thing.

# To Remove
Simply delete the folder you created during the install, or use Package Control:
`PackageControl: Remove Package` --> `base64-decode-popup`.

# Usage
Select a base64 encoded string. The resulting decoded string is displayed in a
popup by the cursor.

## Example
![using the plugin](https://raw.githubusercontent.com/insert-username/subl-base64-decode-popup/master/example-01.png?token=ALEQbYcGE7t8sxHwUH6K87615zwrMdoOks5av7WtwA%3D%3D)

## Configuration
The following settings can be used to configure plugin behavior.

```
"base64_decode_popup": {
    "min_encoded_string_length_inclusive": 1,
    "max_encoded_string_length_exclusive": 1000,

    // ignore whitespace-only strings.
    "encoded_string_ignore_filter_regex" : "^\\s+$",

    // only display strings that are utf8 encoded (may include false-positives).
    "display_non_utf8_byte_arrays": false
}
```

# Development

## Prerequisites
Python `3.3.6` or later.

## Test
Use `./test.sh` to run the unit tests.

## Contributing
Use git flow and Semantic Versioning rules for contributions.
