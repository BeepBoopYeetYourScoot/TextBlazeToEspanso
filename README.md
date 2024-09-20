A simple script to convert TextBlaze snippets to Espanso matches.

Oriented for the conversion of the whole TextBlaze repository at once using the "Export all folders" button in the
settings. Will work just as fine with a single folder.

> **Please configure the `replacer` attribute of the `._format_trigger()` method.**

I use `\` as a shortcut initiator because I think it is more convenient to access the shortcuts in a single button no
matter the keyboard layout.

### Usage

1. Enter the paths to the converter constructor, optionally name your snippet directory
2. Execute `converter.py` as a script
3. Locate the matches inside the configured directory
4. Try to use your snippets. They should work in all environments from the get-go. You may need to reload Espanso