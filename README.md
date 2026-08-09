# Robot Task Validator

A small Python application that validates robot task commands and demonstrates a CI/CD workflow using GitHub Actions and Docker.

## Features

- Validates robot object, action, and destination inputs
- Handles invalid commands and multiple validation errors
- Includes automated tests using pytest
- Runs inside a Docker container
- Uses GitHub Actions for continuous integration
- Automatically runs tests and builds a Docker image on every push to main

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Runs the automated pytest test suite
5. Builds the Docker image

If an automated test fails, the pipeline stops and reports the failure.

## Run Locally

```bash
python app.py