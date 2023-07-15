# Loan App With Django Framework

Money lending application with Django framework. Only Django Framework and HTMX plugin are used for Ajax validation and Ajax logout.


## Screenshots

![Loan App](https://raw.githubusercontent.com/tajbinkhan/loan-app/main/screenshots/1.png)

![Loan App](https://raw.githubusercontent.com/tajbinkhan/loan-app/main/screenshots/2.png)

![Loan App](https://raw.githubusercontent.com/tajbinkhan/loan-app/main/screenshots/3.png)

![Loan App](https://raw.githubusercontent.com/tajbinkhan/loan-app/main/screenshots/4.png)

![Loan App](https://raw.githubusercontent.com/tajbinkhan/loan-app/main/screenshots/5.png)

## Features

- Loan Request Form
- Loan Editable Security
- Loan Can Not Be Approved Without Requested User
- Login and Register
- Password Reset Feature
- Email Address Validation
- Count of Loan Given, Taken, Approved, Requested, Rejected
- Change Email Feature
- Notification History Added

## New Features

- Bank Statement Added
- Crud Functionality Added
- Add Balance Feature to Profile
- Some Bug Fixes


## Installation

Install my-project with pip

Clone the project

```bash
git clone https://github.com/tajbinkhan/loan-app.git
```

Go to the project directory

```bash
cd loan-app
```

In the command panel, run this command.
```bash
pip install -r requirements.txt
```
After successful installation, you need to start the migration to create tables in the database.
```bash
python manage.py makemigrations
python manage.py migrate
```
After migration, start the server by running this command.
```bash
python manage.py runserver
```

## Demo

https://loanapp.pythonanywhere.com/
## Tech Stack

**Client:** HTMX, JavaScript, BootStrap 4

**Server:** Django, Python


## Authors

- [Webphics](https://www.webphics.com)


## License

[MIT](https://choosealicense.com/licenses/mit/)

