# base image
FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Here you define the env vars that will be used IN your app
ENV TEST_ENV_VAR='hello it got it'
ENV SECRET_KEY='wesf987giub2no1eqwfd098f9eguwi2b3jl3rpefwv980we97yiv1hk13on2wpfs90v89yij'

ENV EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
ENV EMAIL_HOST='smtp.gmail.com'
ENV EMAIL_PORT=587
ENV EMAIL_USE_TLS=True
 
ENV EMAIL_HOST_USER='your@email.com'
ENV EMAIL_HOST_PASSWORD='your_password'


# RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt .
#let pip install required packages
RUN pip install -r requirements.txt

COPY . .
