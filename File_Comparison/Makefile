virtualenv_setup:
	rm -rf ../fcmp_env
	virtualenv ../fcmp_env
install_req:
	../fcmp_env/bin/pip install -r requirements.txt
	../fcmp_env/bin/python manage.py migrate
run:
	../fcmp_env/bin/python manage.py runserver 0.0.0.0:8001 &