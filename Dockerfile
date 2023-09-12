FROM python:3.10

LABEL maintainer="AIscribe-app"

COPY requirements.txt /tmp/requirements.txt
COPY requirements-dev.txt /tmp/requirements-dev.txt
WORKDIR /app
COPY api/ /app/api/
EXPOSE 8000

ARG DEV=true
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && \
    rm -rf /var/lib/apt/lists/* && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements-dev.txt ; \
    fi

RUN /py/bin/pip install --upgrade pip &&\
    apt-get upgrade &&\
    /py/bin/pip install hnswlib

RUN /py/bin/pip install langchain[docarray]

ENV PATH="/py/bin:$PATH"

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]