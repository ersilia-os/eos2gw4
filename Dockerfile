FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install eosce==0.2.0

WORKDIR /repo
COPY . /repo
