# Note Management API

A simple Note Management API built with Django, providing endpoints to create, fetch, query, and update notes. The API supports PostgreSQL as the primary database but can be easily configured to use other databases like SQLite.

## Features

- **Create Note**: Create a new note with a title and body.
- **Fetch Note by ID**: Retrieve a note using its primary key.
- **Query Notes by Title Substring**: Search for notes containing a substring in their title.
- **Update Note**: Update the title and body of an existing note.

## Requirements

- Python 3.x
- Django 5.1.1
- PostgreSQL or SQLite
- `dj-database-url`
- `python-decouple`
- Other dependencies as listed in `requirements.txt`

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/note_api.git
    cd note_api
    ```

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv nodevenv
    source nodevenv/bin/activate  # On Windows use `nodevenv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the project root and add the following environment variables:

    ```env
    DJANGO_SECRET_KEY=your_secret_key_here
    DJANGO_DEBUG=True
    DATABASE_URL=postgres://yourusername:yourpassword@yourhost:yourport/yourdatabase
    ```

5. **Run Migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

    The API will be available at `http://127.0.0.1:8000/`.

## Endpoints

- **Create a new note**: `POST /notes/`
- **Fetch a note by ID**: `GET /notes/<id>/`
- **Query notes by title substring**: `GET /notes?title=<substring>`
- **Update a note**: `PUT /notes/<id>/`

## Testing

To run the tests, use the following command:

```bash
python manage.py test
