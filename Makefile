# Project name (used for tagging the Docker image)
PROJECT_NAME := ea2_p2

# Docker image name
IMAGE_NAME := $(PROJECT_NAME)

# Target to build the Docker image
build:
	@echo "Building Docker image: $(IMAGE_NAME)"
	uv pip compile pyproject.toml -o requirements.txt
	docker build -t $(IMAGE_NAME) .

# Target to run the Docker image
run:
	@echo "Running Docker container: $(IMAGE_NAME)"
	docker run -p 8000:8000 $(IMAGE_NAME)

# Target to build and run the Docker image
all: build run

# Target to stop the running container
stop:
	@echo "Stopping Docker container: $(IMAGE_NAME)"
	docker stop $$(docker ps -q --filter "name=$(PROJECT_NAME)")

# Target to remove the Docker image
clean:
	@echo "Removing Docker image: $(IMAGE_NAME)"
	docker rmi $(IMAGE_NAME)

# Target to remove the Docker container (if running) and the image
distclean: stop clean

# Target to display help messages
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  build    Build the Docker image"
	@echo "  run      Run the Docker image"
	@echo "  all      Build and run the Docker image"
	@echo "  stop     Stop the running Docker container"
	@echo "  clean    Remove the Docker image"
	@echo "  distclean Stop the container and remove the image"
	@echo "  help     Display this help message"

# Default target
.DEFAULT_GOAL := help
