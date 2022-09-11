FROM python:3.10.7

WORKDIR /tests

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

USER nobody
CMD [ "pytest", "-p", "no:cacheprovider", "-v" ]
