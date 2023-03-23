FROM python:3.11.2-buster

RUN python -m pip install --upgrade pip && pip install poetry
RUN mkdir /service

COPY ./pyproject.toml /service/pyproject.toml
COPY ./poetry.lock /service/poetry.lock

WORKDIR /service
RUN poetry install --only main --no-root

COPY ./ttsvc /service/ttsvc
COPY ./main.py /service/main.py

EXPOSE 50051
ENTRYPOINT ["poetry", "run", "poe"]
CMD ["serve", "--no-tls"]
