from python:3.5

COPY the_base /code/the_base
COPY the_plugin /code/the_plugin

RUN pip install --upgrade pip

RUN pip install -v /code/the_base

RUN pip install -v /code/the_plugin
