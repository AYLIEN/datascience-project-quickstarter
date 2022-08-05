.PHONY: upload-to-pip
upload-to-pip:
	python setup.py sdist
	pip3 install twine && twine upload --non-interactive -u $PYPI_USERNAME -p $PYPI_PASSWORD dist/*


.PHONY: upload-to-testpypi
upload-to-testpypi:
	python setup.py sdist
	pip3 install twine && twine upload --repository testpypi dist/*
