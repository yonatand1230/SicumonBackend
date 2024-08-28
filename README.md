# Sicumon Backend

**Sicumon** is a platform designed to facilitate the sharing of study 
materials and class notes for high school students. The platform allows users 
to upload and access large document files, such as PDFs and DOCX files. This 
repository contains the backend code of the platform, which is built using 
Python3 and FastAPI, and is deployed serverlessly on AWS Lambda. The backend 
integrates with several AWS services, such as S3 for file storage and DynamoDB 
for database management.

The platform is currently in early stages, and is still in development. 

## Overview

The Sicumon platform is designed to assist students in easily accessing and 
uploading study materials. The backend manages file uploads, user data, and 
metadata related to the documents. Everything is designed to be scalable and 
cost-effective, making it suitable for both current and future needs as the 
platform grows.

## Development

As said earlier, the backend code for Sicumon is written in Python3, using 
FastAPI. I decided to use FastAPI because of its simplcity and easy 
integration with AWS services, using Python modules such as Boto3. AWS was 
chosen as the cloud provider and hosting platform, due to the ability to 
manage everything in the same place, and because of recommendations from other 
developers.

AWS Lambda and FastAPI were chosen for their respective strengths in handling 
serverless architecture and asynchronous web requests:

- **AWS Lambda:** Serverless compute allows for a scalable, cost-efficient 
solution. As the platform’s traffic fluctuates, the backend can automatically 
scale without the need for constant server management, saving both time and 
costs. 

- **FastAPI:** The design is perfect for handling simple HTTP requests, such 
as file uploads and metadata retrieval. Python is a language I use regularly, 
and so the development with FastAPI was easy and efficient.

- **Amazon S3:** As file storage is a core aspect of the platform, Amazon S3 
is a reliable, secure, and infinitely scalable storage for large documents. I 
heard a lot of great things about the service, and so I wanted to try it and 
learn how to use it. This is my first time using S3 on a big project.

- **DynamoDB:** Sicumon requires fast and efficient queries on metadata. 
Because of its ease of use, I wanted to use a NoSQL database. I've used 
Firebase and MongoDB before and wanted to try something new, so DynamoDB was 
chosen as the database for this project. The integration with AWS Lambda and 
S3 was also helpful in this use case.

### Frontend

This repository is backend-focused, as the frontend is stored and hosted 
separately using AWS Amplify. It serves as the user interface where students 
are easily able to look for study materials, upload documents and manage 
different files.

The frontend is built using HTML, CSS and pure JS - without any fancy 
frameworks, to maintain efficiency and simplicity of the code. For more info, 
look for the frontend repository and its readme.

### Future Plans

In the future, I'd like to add a few more features to the platform. For 
example, a search engine can be helpful to look for specific files or 
uploaders. User rating and comments can be used to talk about the documents
and let the uploader know about any mistakes or problems. 

As for the long term, I'd like to add support for more user customization,
including features like adding different subjects. The platform could then be 
100% managed by users. 

User roles and different permissions would also be helpful. Developing an
admin interface will allow the platform to be managed more efficiently.

## Setup and Usage

### Run Locally

To run the backend locally, first make sure to clone the repository and 
configure any environment variables needed. Then, install the dependencies
using PyPI: \
`pip3 install -r requirements.txt`

After that, you can start the server using uvicorn: \
`uvicorn main:app --reload`

The server should then start on `http://localhost:8000`. 

### Deployment

1. Install all requirements into 'dependencies' folder: \
`pip3 install -t dependencies -r requirements.txt` 

2. Zip 'dependencies' folder into 'aws_lambda_artifact.zip': \
`(cd dependencies; zip ../aws_lambda_artifact.zip -r .; cd ..)` 

3. Add any additional files to the zip archive: \
`zip aws_lambda_artifact.zip -u main.py api.py sicumon/*`

Then, you can upload 'aws_lambda_artifact.zip' into AWS Lambda. Please make 
sure to test the server locally before deploying to Lambda, or use the 
development environment for deployment first. 