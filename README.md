# Interactsh API Wrapper

This API wrapper is designed to interact with the Interactsh API using FastAPI. It provides two endpoints for different functionalities.

### Endpoints

#### 1. `api/getURL`

- **Functionality:** Retrieves multiple endpoints (currently 5) from Interactsh.
- **Method:** GET

#### 2. `api/getInteractions`

- **Functionality:** Accepts a POST request to fetch the HTTP request IP and timestamp.
- **Method:** POST

### Usage

1. Clone the repository:

   ```bash
   https://github.com/arup1221/api-wrapper.git
   ```

### TO install it locally

install packages

```bash
   pip3 install --no-cache-dir -r requirements.txt
   ```

or manually 
```bash
   pip install uvicorn annotated-types fastapi python-dotenv pydantic_core pydantic
   ```

For mac use `pip3` and for windows use `pip` only

if the data folder is not empty then use the command

```bash
   rm ./data/* 
   ```

### To run the Application

#### Step1 

You should have installed the golang to install Interactsh. To install the interactsh command

```bash
   go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
   ```

 TO run the script update the path in `line 6` your golang path`(path = "/Users/arupgope")`. Then run the script


```bash
   python3 test_threaded_session.py
   ```
#### step 2

then run the server

```bash
   uvicorn myapi:app --reload
   ```
It will starts in - http://localhost:8000/

### Using Docker

Pull the image
```bash
   docker pull arup1221/api_wrappers:0.1
   ```

Run the image
```bash
   docker run -p 8080:80 arup1221/api_wrappers:0.1
   ```

you get a output in http://localhost:8000/

<br>

### Output

you get the api of interactsh in `api/getURL` path, by making a `GET` request.

Form  the apis take one api and make a HTTP request 

```bash
   curl -H "myrandomheader: dummy" -X POST -d "random values"  <URL>
   ```

Then `api/getInteractions` make a post request
```bash
   {
  "url": "cmr7t1hk5epn5ksnulk0fita6ijo1rds1.oast.pro"
}
   ```

you get the api HTTP request information(Ip and Timestamp).
