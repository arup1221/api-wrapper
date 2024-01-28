from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
# from typing import Optional
from pydantic import BaseModel
import re

import os

app = FastAPI()


# -----------------------------------------/api/getURL api--------------------------------------------------------#


@app.get("/api/getURL", response_class=JSONResponse)
def getURL():
    data_folder = "data"

    try:
        all_lines = []

        for file_name in os.listdir(data_folder):
            file_path = os.path.join(data_folder, file_name)

            with open(file_path, "r") as file:
                linesURL = [      #it contains the [INF]
                    line.strip()  
                    for line in file
                    if ".oast." in line
                ]

                # all_lines.extend(linesURL)
                
                newLines = [
                    line.replace("[[34mINF[0m]", "")  # Remove "[INF]" for each line
                    for line in linesURL
                ]

                all_lines.extend(newLines)

        return JSONResponse(content=all_lines)

    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------------------------/api/getInteraction api-----------------------------------------------------#

class Item(BaseModel):
    url: str

@app.post("/api/getInteractions", response_class=JSONResponse)
def get_interactions_content(item: Item):
    data_folder = "data"
    url_parts = item.url.split(".oast.")
    if len(url_parts) > 1:
        url_to_search = url_parts[0]
    else:
        url_to_search = item.url

    try:
        all_lines = []

        for file_name in os.listdir(data_folder):
            file_path = os.path.join(data_folder, file_name)

            with open(file_path, "r") as file:
                extracted_data = [
                    {"client_ip": re.search(r'(^|\s)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})($|\s)', line).group(2),
                     "timestamp": re.search(r'(^|\s)(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})($|\s)', line).group(2)}
                    for line in file if "Received" in line and "HTTP" in line and url_to_search in line
                ]

            all_lines.extend(extracted_data)
            
        return JSONResponse(content=all_lines)

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="One or more files not found in the 'data' folder")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



