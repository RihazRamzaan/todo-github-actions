# todo-github-actions

A simple Python CLI todo app with full CI/CD pipeline using GitHub Actions and Docker.

![CI](https://github.com/RihazRamzaan/todo-github-actions/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/RihazRamzaan/todo-github-actions/actions/workflows/docker-ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)

## What's Inside

```
todo-github-actions/
├── .github/
│   └── workflows/
│       ├── ci.yml           # Run tests on every push
│       └── docker-ci.yml    # Build & push Docker image
├── src/
│   ├── todo.py              # CLI todo app
│   └── test_todo.py         # Pytest test suite
├── Dockerfile
└── README.md
```

## Run Locally

```bash
git clone https://github.com/RihazRamzaan/todo-github-actions.git
cd todo-github-actions
python src/todo.py
```

**Commands:**
- `a` — add a task
- `l` — list all tasks
- `d` — mark a task done
- `q` — quit

## Run with Docker

```bash
# Pull from Docker Hub
docker pull yourusername/todo-app:latest

# Run
docker run -it yourusername/todo-app
```

## Run Tests

```bash
pip install pytest
cd src
pytest test_todo.py -v
```

## CI/CD Pipeline

Every push triggers:

1. **ci.yml** — runs pytest across Python 3.12
2. **docker-ci.yml** — tests pass → builds Docker image → pushes to Docker Hub

### Setup Docker Hub secrets

Go to **Settings → Secrets → Actions** and add:

| Secret | Value |
|--------|-------|
| `DOCKER_USERNAME` | your Docker Hub username |
| `DOCKER_PASSWORD` | your Docker Hub password or access token |

## Tech Stack

- **Python 3.12**
- **pytest** — unit testing
- **Docker** — containerization
- **GitHub Actions** — CI/CD automation
- **Docker Hub** — image registry
