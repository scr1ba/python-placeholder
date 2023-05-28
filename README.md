# Python Placeholder App

This repository contains a simple Python Flask application that serves as a placeholder or dummy app for testing purposes. The application simply returns a "Hello, world!" message in JSON format when accessed. It can be containerized using Docker, making it suitable for testing pipeline processes.

You can deploy it to a test environment, then send HTTP requests to it and check the responses to verify that your pipeline is working correctly.

## Getting Started

Here are the instructions to get the application up and running.

### Prerequisites

- Python 3.9+
- Docker

### Running the App Locally

To run the application locally, first install the necessary Python dependencies:

```bash
pip install flask
```

Then, you can run the application with:
```
HOST=<your-host> PORT=<your-port> python app.py
```

### Running the App as a Docker Container

To build and run the application as a Docker container, first build the Docker image:

```
docker build -t tiny-python-placeholder .
```

Then, you can run the Docker container with:
```
docker run -p <your-local-port>:<your-container-port> -e HOST=<your-host> -e PORT=<your-container-port> tiny-python-placeholder
```
Replace <your-host> and <your-port> with your desired host and port.

### Configuration
The application can be configured via the following environment variables:

- HOST: The host to run the application on. Defaults to '0.0.0.0'.
- PORT: The port to run the application on. Defaults to 5000.