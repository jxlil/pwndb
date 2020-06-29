# pwndb
Leaked password finder

## Install
```
pip3 install git+https://github.com/jxlil/pwndb.git --user
```

## Usage
```
usage: pwndb.py [-h] -t EMAIL [--password] [-V] [-o NAME_FILE] [--tor-proxy TOR_PROXY] [-v]

Leaked password finder

optional arguments:
  -h, --help                Show this help message and exit
  -t EMAIL, --target EMAIL  Set target email.
  --password                Search by password.
  -V, --verbose             Display results on screen.
  -o NAME_FILE, --output NAME_FILE
                        Save output in JSON format.
  --tor-proxy TOR_PROXY     Set Tor proxy.
  -v, --version             show program's version number and exit
```

## Example
```bash
pwndb -t john.%@gmail.com -V -o emails.json

pwndb -t 123456789 --password -V -o passwords.json
```

---

## Author

**Jalil SA**

Do you want to support this project? You can send a **pull request**, write an **issue** or just **buy me a coffee**!


<a href="https://www.buymeacoffee.com/jxlil" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg"></a>