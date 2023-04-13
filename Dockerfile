FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2022.9.4
RUN pip install click==8.1.3
RUN pip install onnxruntime==1.14.0
RUN pip install joblib==1.2.0
RUN pip install git+https://github.com/ersilia-os/compound-embedding-lite.git

WORKDIR /repo
COPY . /repo
