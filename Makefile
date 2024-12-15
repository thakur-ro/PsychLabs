ruff:
	ruff check --fix
	ruff format
static-analysis:
	pre-commit run --all-files --verbose
