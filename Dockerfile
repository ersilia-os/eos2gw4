FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install eosce==0.2.0
RUN pip install numpy==1.22.3

WORKDIR /repo
COPY . /repo
