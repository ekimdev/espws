help:
	@echo "flake8		Execute flake8"
	@echo "format		Execute Black code formatter"
	@echo "format-check	Execute Black check formatter"
format:
	@black listener.py api.py

format-check:
	@black listener.py api.py --check

flake8:
	@flake8 . --config=.flake8

.PHONY: flake8
