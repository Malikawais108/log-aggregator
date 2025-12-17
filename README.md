# 🚀 Log Aggregator CI/CD Pipeline with Monitoring

## 📌 Overview
This project demonstrates a full DevOps workflow that integrates:

- **Jenkins CI/CD pipeline** for automated builds, tests, and deployments
- **Dockerized Python exporter** that exposes application and system metrics
- **Prometheus** for metrics collection
- **Grafana** for visualization and alerting
- **Helm chart** for Kubernetes deployment

The pipeline ensures every commit is tested, validated, and pushed to Docker Hub, while Prometheus + Grafana provide observability into system health.

---

## ⚙️ CI/CD Pipeline Flow
1. **Clone Repository** → Jenkins pulls code from GitHub  
2. **Build Docker Image** → Builds container from root‑level Dockerfile  
3. **Run Tests** → Executes `pytest` inside the container (`tests/` directory)  
4. **Run Exporter** → Smoke test to validate `main.py` exporter  
5. **Push to Docker Hub** → Publishes image to `docker.io/awaismalak/log-aggregator`  
6. **Cleanup** → Jenkins clears workspace  

✅ Pipeline enforces testing before pushing, ensuring only verified builds reach Docker Hub.

---

## 🐳 Docker Setup
**Dockerfile** (root):
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY parser/ /app/
COPY requirements.txt /app/
COPY tests/ /app/tests/
RUN pip install -r requirements.txt
EXPOSE 8087
CMD ["python", "main.py"]





## 👨‍💻 Author

**Malak Awais**  
GitHub: [github.com/Malikawais108](https://github.com/Malikawais108)  
Docker Hub: [docker.io/awaismalak/log-aggregator](https://hub.docker.com/r/awaismalak/log-aggregator)
