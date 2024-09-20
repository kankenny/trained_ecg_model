# Python Application

A trained ECG model with modes={`dev`, `prod`}. You can execute the app directly using Python or containerize it using Docker.

## Requirements for the CLI

- Python 3.x
- pip

### Running with Python

- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run via the CLI:
  ```bash
  python endpoint.py ["" | dev | prod]
  ```

## Requirements for Docker

- Docker

### Running with Docker Development Mode

- Build the image:
  ```docker
  docker build -t dev-trained-ecg-model:v1 -f Dockerfile.dev
  ```
- Run via the CLI:
  ```docker
  docker run -p 8001:8001 dev-trained-ecg-model:v1
  ```

### Running with Docker Production Mode

- Build the image:
  ```docker
  docker build -t prod-trained-ecg-model:v1 -f Dockerfile.prod
  ```
- Run via the CLI:
  ```docker
  docker run prod-trained-ecg-model:v1
  ```
