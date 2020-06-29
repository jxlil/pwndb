<p align="center">
  <img  width="100" height="100" src="img/openlock.svg" />
</p>

# pwndb
Leaked password finder

## Installation
### Prerequisites
```bash
sudo apt install python3 python3-pip git tor
pip3 install virtualenv --user 
```
### Install
```bash
git clone https://github.com/jxlil/pwndb.git
cd pwndb

virtualenv venv
source venv/bin/activate

pip3 install -r requirements.txt --user
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
The **Tor** service needs to be active `sudo service tor restart`
```bash
# It's character % serves as a wildcard
python3 bin/pwndb.py -t john.%@gmail.com -V -o emails.json

# You can also search by password
python3 bin/pwndb.py -t 123456789 --password -V -o passwords.json
```

---

## Author

**Jalil SA**

Do you want to support this project? You can send a **pull request**, write an **issue** or just **buy me a coffee**!


<a href="https://www.buymeacoffee.com/jxlil" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg"></a>
