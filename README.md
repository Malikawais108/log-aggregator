# Log Aggregator CI/CD Pipeline

This project demonstrates a Jenkins pipeline that:
1. Clones the repository from GitHub
2. Builds a Docker image
3. Runs unit tests with pytest
4. Validates the exporter
5. Pushes the image to Docker Hub

## Technologies
- Jenkins
- Docker
- GitHub
- Docker Hub
- Pytest

## Pipeline Stages
- **Clone Repository**: Pulls code from GitHub
- **Build Docker Image**: Builds container from Dockerfile
- **Run Tests**: Executes pytest inside container
- **Run Exporter**: Smoke test for `main.py`
- **Push to Docker Hub**: Publishes image
- **Cleanup**: Clears Jenkins workspace
