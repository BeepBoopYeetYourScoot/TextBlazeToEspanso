A simple script to convert TextBlaze snippets to Espanso matches.

Oriented for the conversion of the whole TextBlaze repository at once using the "Export all folders" button in the
settings. Will work just as fine with a single folder.

I use `\` as a shortcut initiator because I think it is more convenient to access the shortcuts in a single button no
matter the keyboard layout.

### Prerequisites
- Python 3.12
- pip

### Installation
- `git clone https://github.com/makeyouswag/TextBlazeToEspanso.git`
- `python -m venv venv`
- `pip install -r requirements.txt`

### Usage

1. Configure paths in `settings.py`. **Please configure the `replacer_character` attribute.**
2. Execute `converter.py` as a script: `python converter.py`
3. Locate the matches inside the configured directory
4. Try to use your snippets. They should work in all environments from the get-go. You may need to reload Espanso
