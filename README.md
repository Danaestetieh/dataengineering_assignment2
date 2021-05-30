# Dataengineering_assignment2
# This application is to represent covid 19 data for United Kingdom 
I used docker compose to build three images: 
 1- Apache Airflow: to build the pipeline
 2- PostgresSQL Database: to load the CSVs files
 3- Redis
 
 # To run the application:
 Use this command docker-compose up
 
 # To run Airflow:
 URL: http://localhost:8080
 username: airflow
 password: airflow
 
 all DAGs names will be appeared, my DAG name is "dana_assignment2", click on the DAG and run the flow using run button.
 
 # To check the stored data in postgresSQL database
 
 I used pgAdmin to check the data (after connect with postgres server I used), the table created under uk_scoring_report_2021_05_30. 
 or run this query SELECT * FROM public."uk_scoring_report_2021-05-30"
 
 
