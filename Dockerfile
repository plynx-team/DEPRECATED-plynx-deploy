FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl

ADD ./configs/kubeconfig.yaml /app/kubeconfig.yaml

RUN mkdir test_data


# Install plugins
ADD ./plynx_deploy /app/plynx_deploy
ADD ./setup.py /app/setup.py
RUN python /app/setup.py install
