pip install fastapi
pip install "uvicorn[standard]"
uvicorn main:app --reload

docker:
build img:
docker build -t supercheap-da-fastapi:0.1 .
create docker and run:
docker run -p 5001:8000 --name SuperCheapDA-api-server supercheap-da-fastapi:0.1

to stop docekr:
docker kill SuperCheapDA-api-server

example url for testing:
http://localhost:5001/items?item_id=5&q=somequery