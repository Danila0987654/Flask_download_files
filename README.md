
# Test project for download files from flask

That's project for understand how download file


## Run application

Clone the project

```bash
git clone https://github.com/Danila0987654/Flask_download_files.git
```

Go to the project directory

```bash
cd Flask_download_files
```

Create file .env and put with your value this:

```bash
HOST=
PORT=
FLASK_ENV=
DEBUG=
SECRET_KEY=
DATA_DIR=
```

Create venv, activate and update pip

```bash
python3 -m venv venv
. ./venv/bin/activate
pip install -U pip
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start application

```bash
flask run
```