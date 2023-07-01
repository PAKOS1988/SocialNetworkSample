FROM python:3.10

WORKDIR /SocialNet

COPY ./requirements.txt /SocialNet/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /SocialNet/requirements.txt

COPY . /SocialNet/

CMD ["python3.10", "main.py"]

EXPOSE 5000