# Interactsh API Wrapper

This API wrapper is designed to interact with the Interactsh server API using FastAPI. It provides two endpoints for different functionalities.

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
   docker run -p 8000:8000 arup1221/api_wrappers:0.1
   ```

you get output in  http://0.0.0.0:8000/ 


<br>

### Output

you get the apis(now 5) of interactsh in `api/getURL` path, by making a `GET` request.

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


![Test](https://github.com/arup1221/api-wrapper/blob/main/images/Screenshot%202024-01-28%20at%209.50.22%E2%80%AFPM.png)


![Test](https://github.com/arup1221/api-wrapper/blob/main/images/Screenshot%202024-01-28%20at%209.51.17%E2%80%AFPM.png)

