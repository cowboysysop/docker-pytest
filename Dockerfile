FROM python:3.14.2

WORKDIR /tests

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

HEALTHCHECK NONE

USER nobody
CMD [ "pytest", "-p", "no:cacheprovider", "-v" ]
