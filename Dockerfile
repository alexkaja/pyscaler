FROM python:3

#copy the scaler to the container image
COPY scaler.py /

#install kubernetes python client library
RUN pip install kubernetes

#run the script
CMD ["python", "/scaler.py"]