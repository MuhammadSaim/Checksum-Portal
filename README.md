# CheckSum Portal

## Requirements
- Python 3.10
- Django 4
- NodeJs 16 or above
- Yarn or NPM
- Virtualenv

## Configuration

1. Clone the repo
```shell
git clone https://github.com/MuhammadSaim/Checksum-Portal.git checksum-portal
```
2. Step into folder
```shell
cd checksum-portal
```
3. Create virtual environment
```shell
python -m venv venv
```
4. Activate the venv

For Linux / Mac OS
```shell
source venv/bin/activate
```

For Windows
```shell
\path\to\env\Scripts\activate
```

5. Install the dependencies
```shell
pip install -r requirements.txt
```

6. Install the frontend dependencies

If you have yarn
```shell
yarn install && yarn dev
```

If you have NPM
```shell
npm install && npm run dev
```

7. Copy the <kbd>.env.example</kbd> file and make a new file <kbd>.env</kbd>

8. configure the **MySQL** DB with the application in <kbd>.env</kbd> file
```dotenv
DATABASE_HOST=YOUR_DB_HOST
DATABASE_NAME=YOUR_DB_NAME
DATABASE_USERNAME=YOUR_DB_USERNAME
DATABASE_PASSWORD=YOUR_DB_PASSWORD
DATABASE_PORT=YOUR_DB_PORT
```

9. Now run the migration to create the DB structures
```shell
python manage.py migrate
```

10. After that create a supper user for the application
```shell
python manage.py createsuperuser
```
and fill the required fields.

11. Run the application and you are good to go
```shell
python manage.py runserver
```
