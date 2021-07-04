# simple-django
Repository for learning how to partition Django prod ready project
inspired by "https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html"

venv environment is outside git rep folder 
simple-django folder = git repostory

django: {
    templates: holding static templates,
    static: storing static files e.g js, css, etc ...
    requirements folder: split so as to enable diff packegs for diff build, eg. installing django-debug-toolbar or health check for,
                        test/local nly while absent for prd

}

packages: {
    django: obviously,
    psycopg2: postgres bindings,
    python-decouple: store secret/env variables. life is easier,
    pytz: for timezone,
    django-sendgrid-v5: sendgrid app for sending emails,
    black: formatter, think eslint for js,
    tox: interface for ci tools,
    flake8: PEPs, code formatting,
    django-debug-toolbar: for local debug info and settings,
    ipython: quick code test,
    gunicorn: for server hosting,
    sentrysdk: security rest etc..
}

django manage.py edited to add "simple.settings.local" as default from dictionary get method