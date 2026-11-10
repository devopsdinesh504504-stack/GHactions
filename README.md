# Flask DevOps CI/CD Project

This project demonstrates a beginner-friendly Python Flask application with GitHub Actions CI/CD. It includes a simple web API, unit tests, linting, security scanning, containerization, and automation using GitHub Actions.

## Project architecture

```text
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   ├── __init__.py
│   └── routes.py
├── tests/
│   └── test_app.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── run.py
├── README.md
└── LICENSE (optional)
```

### Main components

- `app/`: Flask application package
- `tests/`: Unit tests for the API
- `Dockerfile`: Container definition for the app
- `requirements.txt`: Python dependencies
- `.github/workflows/ci-cd.yml`: CI/CD pipeline
- `pyproject.toml`: Ruff and pytest configuration

## Python application

The Flask app exposes three endpoints:

- `/` -> Returns the homepage message: `Welcome to DevOps CI/CD Project`
- `/health` -> Returns application health status JSON
- `/api/info` -> Returns basic metadata JSON

### Environment variables

The app reads environment variables for configuration. Copy the sample file:

```bash
cp .env.example .env
```

Example values:

```bash
APP_ENV=development
FLASK_DEBUG=false
PORT=5000
```

## Run the Python application locally

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# On Linux/macOS
source .venv/bin/activate
# On Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Start the Flask app:

```bash
python run.py
```

4. Open the app in a browser:

- http://localhost:5000/
- http://localhost:5000/health
- http://localhost:5000/api/info

## Run unit tests

Run the tests with:

```bash
pytest -q
```

Optional coverage report:

```bash
pytest --cov=app --cov-report=term-missing
```

## Docker instructions

### Build the image

```bash
docker build -t flask-devops-demo:latest .
```

### Run the container locally

```bash
docker run --rm -p 5000:5000 --env-file .env flask-devops-demo:latest
```

Then open:

- http://localhost:5000/
- http://localhost:5000/health

### Docker security best practices used here

- Lightweight Python base image: `python:3.12-slim`
- Non-root user created inside the container
- `.dockerignore` excludes development and Git metadata
- `PYTHONDONTWRITEBYTECODE=1` and `PYTHONUNBUFFERED=1` improve runtime behavior

## Push code to GitHub

1. Initialize git (if needed):

```bash
git init
git add .
git commit -m "Initial Flask DevOps project"
```

2. Create a remote repository on GitHub.

3. Push the code to `main`:

```bash
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

4. Create a pull request to target `main` to trigger CI checks.

## GitHub Actions workflow behavior

The workflow file is located at `.github/workflows/ci-cd.yml`.

It triggers on:

- Pushes to `main`
- Pull requests targeting `main`

### Jobs and purpose

1. `code_checkout` - checks out the repository code
2. `python_setup` - installs Python and dependencies
3. `code_quality` - runs Ruff and Bandit
4. `unit_tests` - runs pytest and coverage
5. `dependency_security` - runs `pip-audit` for vulnerabilities
6. `docker_build` - builds the Docker image after all earlier checks pass
7. `docker_push` - pushes the final image to GitHub Container Registry (GHCR) only on `main`

### Job dependency chain

The workflow uses `needs` to ensure proper order:

```yaml
needs: code_checkout
needs: python_setup
needs: code_quality
needs: unit_tests
needs: dependency_security
needs: docker_build
```

This means a downstream job does not run until the previous job succeeds. If any job fails, the pipeline stops in the next dependent stages and the overall workflow is marked as failed.

### Security note for pull requests

The Docker image push step runs only when the workflow is triggered by a direct push to `main`. Pull requests are validated, but images are not published from untrusted PRs.

## Troubleshooting pipeline failures

Common checks and fixes:

- `ruff check .` fails: fix import ordering or lint issues
- `bandit` fails: review security warnings in the app code
- `pytest` fails: inspect failing assertions and fix the app or tests
- `pip-audit` fails: upgrade vulnerable packages in `requirements.txt`
- Docker build fails: check the Dockerfile and app file paths

Check workflow logs in GitHub:

1. Open the repository on GitHub
2. Click the `Actions` tab
3. Select the failed workflow run
4. Open the failed job and inspect the logs

## Summary

This project teaches the basics of:

- Python Flask development
- API testing with pytest
- Linting and security scanning
- Docker containerization
- GitHub Actions automation
- CI/CD basics for a starter DevOps project

It is intentionally simple and suitable for learning and demonstration in a public repository.
