# MailMiner - Email Extractor

MailMiner is a simple command-line tool written in Python to extract email addresses from any public website. It fetches the webpage, scans for email addresses, and optionally saves the results to a file.

## Features

- Fetches a webpage and extracts all email addresses
- Ignores image and media file extensions in email matches
- Saves results to a text file (optional)
- Simple CLI interface


### Requirements

- Python 3.7 or higher
- [requests](https://pypi.org/project/requests/)

Install dependencies:

```bash
pip install requests
```


## Usage

Clone the repository:

```bash
git clone https://github.com/0xRyuk/mailminer.git
cd mailminer
```

```bash
python main.py -u <website_url> [-o <output_file>]
```

### Example

Extract emails from example.com and save to `emails.txt`:

```bash
python main.py -u https://example.com -o emails
```

## Output

- Prints the number of emails found and lists them in the terminal
- If `-o` is provided, saves the emails to the specified file


## License

MIT

## Author

[0xRyuk](https://github.com/0xRyuk)
