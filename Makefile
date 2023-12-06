project_name = globartigos


run:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

install:
	pip install -r requirements.txt

test:
	python manage.py test

shell:
	python manage.py shell

startapp:
	python manage.py startapp $(app_name)
	mv $(app_name) $(project_name)/apps/$(app_name)
	echo "New app created in $(project_name)/apps/$(app_name)"
	echo "Don't forget to add the app in $(project_name)/settings.py"
	echo "and change the app name in $(project_name)/apps/$(app_name)/apps.py"

superuser:
	python manage.py createsuperuser
