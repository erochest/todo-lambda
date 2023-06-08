
test:
    PYTHONPATH="." poetry run pytest

get_root:
    poetry run python-lambda-local -f get_root todo_app.py events/empty.json