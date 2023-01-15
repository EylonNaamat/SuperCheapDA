FROM python:3.9-slim
COPY  ./src /SuperCheapDA/src
COPY  ./modules /SuperCheapDA/modules
COPY ./requirements.txt /SuperCheapDA
COPY ./firebase-sdk.json /SuperCheapDA

WORKDIR /SuperCheapDA

RUN pip install fastapi uvicorn requests 
RUN pip install --user firebase-admin
RUN pip install -r requirements.txt

EXPOSE 5001
CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", "--reload" ]