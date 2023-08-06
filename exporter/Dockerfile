FROM python:3.8.13-slim

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y curl
RUN adduser --disabled-password nonroot
RUN mkdir /home/app && chown -R nonroot:nonroot /home/app
RUN mkdir -p /opt/venv && chown -R nonroot:nonroot /opt/venv
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app

WORKDIR /home/app
USER nonroot

COPY --chown=nonroot:nonroot . . 
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]