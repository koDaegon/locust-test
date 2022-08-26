FROM public.ecr.aws/lambda/python:3.9

COPY . /locust/
WORKDIR /locust

RUN pip install -r requirements.txt

ENTRYPOINT ["locust"]