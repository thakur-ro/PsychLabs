# PsychLabs

Welcome to the project! Follow these steps to set up the project environment and install all necessary dependencies.

## Prerequisites
Ensure you have the following installed:
1. **Python**: Version 3.8 or higher.
2. **Poetry**: [Installation Guide](https://python-poetry.org/docs/#installation).

## Setting Up the Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thakur-ro/PsychLabs.git
   cd PsychLabs
   ```

2. **Install Project Dependencies**:
   Poetry will handle the creation of a virtual environment and install all dependencies specified in the `pyproject.toml` file.
   ```bash
   poetry install
   ```

3. **Activate the Virtual Environment** (if necessary):
   Poetry usually manages this automatically. If needed, you can manually activate it:
   ```bash
   poetry shell
   ```

4. **Verify Installation**:
   Ensure all dependencies are installed correctly by running:
   ```bash
   poetry check
   ```

## Run checks locally
Below command will help in running pre-commit hooks on all git tracked files to commit.
To check files that are tracked
```bash
git ls-files
```
Then run
```bash
make static-analysis
```

## Additional Notes

- If any dependencies are missing or require updates, use the following command to add or update them:
  ```bash
  poetry add <package-name>
  ```

- To install dev dependencies (e.g., for testing or linting):
  ```bash
  poetry install --with dev
  ```
