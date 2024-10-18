# `aws configure` first
# `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 891377169881.dkr.ecr.us-east-1.amazonaws.com`

ECR_REPO=891377169881.dkr.ecr.us-east-1.amazonaws.com
IMAGE_NAME=nyit-etic
FUNCTION_NAME=ecg
TAG=latest
PLATFORM=linux/amd64
DOCKERFILE=Dockerfile.aws

all: build tag push

build:
	docker build -f $(DOCKERFILE) --platform $(PLATFORM) -t $(IMAGE_NAME):$(TAG) .

tag:
	docker tag $(IMAGE_NAME):$(TAG) $(ECR_REPO)/$(IMAGE_NAME):$(TAG)

push:
	docker push $(ECR_REPO)/$(IMAGE_NAME):$(TAG)

clean:
	docker rmi $(IMAGE_NAME):$(TAG)
	docker rmi $(ECR_REPO)/$(IMAGE_NAME):$(TAG)

update:
	aws lambda update-function-code --function-name $(FUNCTION_NAME) --image-uri $(ECR_REPO)/$(IMAGE_NAME):$(TAG)