
test:
    PYTHONPATH="." poetry run pytest

get_root:
    poetry run python-lambda-local -f get_root todo_app.py events/empty.json

deploy: test
    sam build --use-container
    sam local invoke
    sam deploy --guided