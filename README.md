# :zap: BlogState API
This is an under-development API for [BlogState](https://blogstate.pythonanywhere.com), built in [Falcon](https://falconframework.org), and [peewee ORM](http://docs.peewee-orm.com) for database interactions.

# Setting it up

If you plan to contribute, below are the steps you need to follow.

### :arrow_right: Fork, and clone the repository.

If you have SSH keys, use -
```sh
    $ git clone git@github.com:<username>/blogstate-api
```
If you don't, use HTTPS instead -
```sh
    $ git clone https://github.com/<username>/blogstate-api
```
where, `<username>` is your own GitHub username.

### :arrow_right: Navigate to project root
Next, `cd blogstate-api/` to get inside the project directory.

### :arrow_right: Create and activate a virtual environment (optional / recommended)

To create a virtual environment, run:

    $ python3 -m venv venv
(or use `virtualenv` instead).

To activate it in Linux-based systems -

    $ source venv/bin/activate

To activate it in Windows -

    $ \venv\Scripts\activate.bat

### :arrow_right: Install the requirements:

    (venv) $ pip install -r requirements.txt

> Feel free to use pipenv too. Because pipenv is slow, it's better to manually create and activate a virtual environment, and install the requirements.

### :arrow_right: Run the development server

A gunicorn server is used to serve the app.

    (venv) $ gunicorn index:app --reload

This starts the server at http://localhost:8000 by default. The `--reload` flag enables hot reloads, i.e. it restarts the server on any file changes.

### Testing endpoints

You may use `httpie` for a CLI, or  a GUI alternative like [Postman](https://www.getpostman.com/downloads/) or [Insomnia](https://insomnia.rest) to test the necessary endpoints.
