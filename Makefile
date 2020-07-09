compile-reqs:
	pip-compile -o requirements.txt requirements.in

sync-env:
	pip install -r requirements.txt