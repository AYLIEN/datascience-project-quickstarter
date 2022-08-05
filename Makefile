.PHONY: upload-to-pip
upload-to-pip:
	python setup.py sdist
	pip3 install twine && twine upload --non-interactive -u $PYPI_USERNAME -p $PYPI_PASSWORD dist/*
