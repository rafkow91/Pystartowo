# Pystartowo.pl

*Python knowledge base for beginners*

[![Built with Django Bootstrap Template](https://img.shields.io/badge/Built%20with-Django%20Bootstrap%20Template-blueviolet.svg)](https://github.com/griceturrble/django-bootstrap-template/) [![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Module 'users' based on [Django-Crash-Starter](https://github.com/feldroy/django-crash-starter)

Favicon downloaded from [Icons8](https://icons8.com) site.

Icons downloaded from [Font Awersome](https://fontawesome.com/) site.

## License

This project uses the MIT license. Please see the [LICENSE](LICENSE) for details.


## Installation

1. Create a new Python virtual environment.

   - Using `venv` on Linux:

     ```bash
     python3 -m venv .venv --prompt pystartowo
     ```

   - Using `venv` on Windows:

     ```bash
     python3 -m venv .venv --prompt pystartowo
     ```

   - Or, use whichever style of virtual environment management you prefer!

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. *PostgreSQL settings*: if not present already create a new `.env` file at `pystartowo/core/.env`. This file should be gitignored from the repo, and should contain credentials for connecting to the PostgreSQL database:

   - `POSTGRES_NAME`: database name
   - `POSTGRES_USER`: username
   - `POSTGRES_PASSWORD`: password
   - `POSTGRES_HOST`: host serving the database
   - `POSTGRES_PORT`: port

1. Migrate models to the database:

   ```bash
   python pystartowo/manage.py migrate
   ```

1. Create a superuser:

   ```bash
   python pystartowo/manage.py createsuperuser
   ```

1. Run the development server:

   ```bash
   python pystartowo/manage.py runserver
   ```

1. Open http://localhost:8000 to view the running site.
