# Use multi-stage build for efficiency
FROM golang:latest AS build

WORKDIR /go/src/app

# Install Interactsh client
RUN go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest

# Switch to Python runtime environment
FROM python:latest

WORKDIR /app

# Copy the built Interactsh client from the previous stage
COPY --from=build /go/bin/interactsh-client /app/interactsh-client

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Copy the start script into the container
COPY start.sh /app/start.sh

# Make start.sh executable
RUN chmod +x /app/start.sh

# Run the start script
CMD ["/app/start.sh"]
