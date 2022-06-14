from ubuntu
RUN apt update
RUN apt install dnsutils -y
RUN apt install python3 -y
RUN apt install python3-pip -y 
RUN pip install flask


EXPOSE 80
WORKDIR /code
COPY . /code/
ENTRYPOINT ["python3"]
CMD ["hello.py"]