# Getting Started
The api documentation can be found [here](##APIDoc).

## Requirements

* python3

### Clone the repository, Make virtual environment and install dependencies

* Windows
```
# clone the repository
git clone https://github.com/triaton/fastapi-email-sender.git

cd fastapi-email-sender

# make virtual environemnt
py -m venv env

# activate the virtual environment
.\env\Scripts\activate.bat

# install dependencies
py -m pip install -r requirements.txt

# start the server for development
uvicorn main:app --reload

# start the server for production
uvicorn main:app --port 80 --host 0.0.0.0
```

* Linux
```
# clone the repository
git clone https://github.com/triaton/fastapi-email-sender.git

cd fastapi-email-sender

# make virtual environemnt
virtuanenv env

# activate the virtual environment
source ./env/Scripts/activate

# install dependencies
pip install -r requirements.txt

# start the server for development
uvicorn main:app --reload

# start the server for production
uvicorn main:app --port 80 --host 0.0.0.0
```

## How to test the api
You can test the API with PostMan and directly using curl command.
```bash
curl --data-raw "{\"data\":\"aGVsbG8sIHdvcmxkIQ==\"}" --location --request POST 'http://localhost/api/parse' --header 'Content-Type: application/json'
```

## How to integrate the ML part
You can find the `# TODO` commented part from `main.py` file. You can customize the code there. That's all.

## APIDoc

1. parse api
```
url: /api/parse
method: POST
payload:
{
    data: "string"
}
Response format
{
    "success": "boolean",
    "data": "string"
}
```