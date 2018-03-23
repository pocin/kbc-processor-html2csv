# FROM amancevice/pandas:0.22.0-python3-alpine

FROM quay.io/keboola/docker-custom-python:1.4.2

RUN pip install --no-cache-dir --ignore-installed \
    pytest \
    pandas \
    xlrd==1.1 \
    html5lib==0.999999999 \
    beautifulsoup4==4.6 \
    lxml \
    git+git://github.com/keboola/python-docker-application.git@2.0.0

WORKDIR /code

COPY . /code/

# Run the application
CMD python3 -u /code/main.py
