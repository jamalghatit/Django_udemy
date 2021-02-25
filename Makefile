test: flake8 pylint coverage

flake8:
	flake8 adc core scripts

pylint:
	pylint adc core scripts

coverage:
	mkdir coverage-reports || true
	coverage run manage.py test && coverage report -m && coverage html
	coverage xml -i -o coverage-reports/coverage-all.xml

setup:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver