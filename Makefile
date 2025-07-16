PYTHON=python
VENV=.venv

setup-venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/Scripts/pip install -r requirements.txt

run:
	$(VENV)/Scripts/python -m src.main

run-question:
	$(VENV)/Scripts/python -m src.main "$(q)"
