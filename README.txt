# Django Inventory Web Application


## Usage Requirements

- Clone the repository (`git clone <repository link>`)
- `cd <repository directory>`
- remove existing virtual environment (`rm -r ./env`)
- make a new python virtual environment (`python3 -m venv Django_Project`)
- activate virtual environment python path `source <Virtual Environment Directory Name>/bin/activate`
- Install required packages/libraries (`pip install -r requirements.txt`)

> - Now that all dependancies are installed, you need to add the secrets and credentials to `settings.txt` like the database credentials, the email credentials as well as the OAuth and the Captcha keys.
> - Consider checking out my [**Notion notes**](https://soapy-reply-39f.notion.site/Python-Django-Inventory-Management-020a02db319e4268b43788c8a225f903?pvs=4) about this project to understand how to add the credentials required 
- Finally, run the server (`python manage.py runserver`) and access it from `127.0.0.1:8000`.