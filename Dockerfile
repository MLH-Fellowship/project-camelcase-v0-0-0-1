FROM python:3.9-slim-buster

WORKDIR /personal-portfolio

COPY requirements/prod.txt .

ENV FLASK_APP=run.py

COPY . . 

RUN pip3 install -r requirements/prod.txt

# ENTRYPOINT [ "flask", "deploy" ]

# CMD [ "flask", "run", "--host=0.0.0.0" ]
# CMD [ "flask", "run", "--host=0.0.0.0" ]


EXPOSE 5000
ENTRYPOINT ["./scripts/entry.sh"]