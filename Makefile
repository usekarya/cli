lint:
	black karya -l 120
	isort karya

build:
	python3 -m build

check:
	python3 -m twine check dist/*

