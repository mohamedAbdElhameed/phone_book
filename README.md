# phonebook

simple phonebook application that has contact names and their numbers.

## Database schema

```
+----------------+     +-----------------+
| Contact        |     | PhoneNumber     |
+----------------+     +-----------------+
| id             |<-+  | id              |
| name           |  +--| contact_id (FK) |
+----------------+     | number          |
                       +-----------------+
```

description of the models:

## Database Schema

The database has two tables: `Contact` and `PhoneNumber`.

### Contact Table

| Column | Type        | Description             |
| ------ | ----------- | ----------------------- |
| id     | integer     | Primary key for contact |
| name   | varchar(50) | Name of the contact     |

### PhoneNumber Table

| Column     | Type        | Description                                       |
| ---------- | ----------- | ------------------------------------------------- |
| id         | integer     | Primary key for phone number                      |
| contact_id | integer     | Foreign key to `Contact` table (one-to-many link) |
| number     | varchar(20) | Phone number for the contact                      |

The `contact_id` column in the `PhoneNumber` table is used to establish a one-to-many relationship between the `Contact` and `PhoneNumber` tables, so that a single contact can have multiple phone numbers.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy phonebook

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
