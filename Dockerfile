FROM python:3
ENV PYTHONVBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
RUN ls -la
# COPY code/* /code/
