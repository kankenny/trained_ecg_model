##### Requirements for the CLI

- Python 3.x
- pip

# ECG model training

A python notebook for the complete machine learning workflow to build a classifier for ECG-related biometrics data.

### Running with Python
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Navigate to the `train_analysis_pynb` dir
  ```bash
  cd train_analysis_pynb
  ```
- Train the model using the `ECG_training.pynb` notebook
  ```
  Run all cells of the notebook
  ```

# Trained ECG model

A trained ECG model with modes={`dev`, `prod`}. You can execute the app directly using Python or containerize it using Docker.


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
  docker build -t dev-trained-ecg-model:v1 -f Dockerfiles/Dockerfile.dev
  ```
- Run via the CLI:
  ```docker
  docker run -p 8001:8001 dev-trained-ecg-model:v1
  ```

### Running with Docker Production Mode

- Build the image:
  ```docker
  docker build -t prod-trained-ecg-model:v1 -f Dockerfiles/Dockerfile.prod
  ```
- Run via the CLI:
  ```docker
  docker run prod-trained-ecg-model:v1
  ```
