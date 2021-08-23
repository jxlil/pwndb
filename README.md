# pwndb

Leaked emails finder. Powered by: `pwndb2am4tzkvold.onion`

## Installation

### Prerequisites

```bash
sudo apt install tor
```

### Install

```bash
git clone https://github.com/jxlil/pwndb.git; cd pwndb

virtualenv venv 
source venv/bin/activate

pip3 install -r requirements.txt
```

---

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

---

## Example

The **Tor** service needs to be active `sudo service tor restart`

```bash
# It's character % serves as a wildcard
python3 bin/pwndb.py -t john.%@gmail.com -V -o emails.json

# You can also search by password
python3 bin/pwndb.py -t 123456789 --password -V -o passwords.json
```

