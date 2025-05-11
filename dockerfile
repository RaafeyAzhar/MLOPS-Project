FROM apache/airflow:latest

USER root
RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean

# Now switch to airflow user to install Python packages
USER airflow
RUN pip install apache-airflow-providers-fab
