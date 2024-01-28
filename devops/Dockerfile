#
FROM python:3.11 as requirements-stage


#
RUN pip install poetry

#
COPY ../pyproject.toml ./
COPY ../poetry.lock ./

#
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

#
FROM python:3.11

#
WORKDIR /code

#
COPY --from=requirements-stage requirements.txt requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ../ /code

#
CMD ["uvicorn", "command.server:app", "--host", "0.0.0.0", "--port", "80"]