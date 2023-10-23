lint:
	black karya -l 120
	isort karya

pip_compile:
	pip-compile pyproject.toml

build:
	python3 -m build

check:
	python3 -m twine check dist/*

upload:
	twine upload dist/* --verbose