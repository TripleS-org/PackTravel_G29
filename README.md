# 🐺 PackTravel
[![Build](https://github.com/VSangarya/PackTravel/actions/workflows/build.yml/badge.svg)](https://github.com/VSangarya/PackTravel/actions/workflows/build.yml)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/df6694ed8d644df1822a1caa1669e504)](https://app.codacy.com/gh/VSangarya/PackTravel?utm_source=github.com&utm_medium=referral&utm_content=VSangarya/PackTravel&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/df6694ed8d644df1822a1caa1669e504)](https://www.codacy.com/gh/VSangarya/PackTravel/dashboard?utm_source=github.com&utm_medium=referral&utm_content=VSangarya/PackTravel&utm_campaign=Badge_Coverage)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/w/VSangarya/PackTravel)](https://github.com/VSangarya/PackTravel/pulse)
[![Issues](https://img.shields.io/github/issues/VSangarya/PackTravel?color=red)](https://github.com/VSangarya/PackTravel/issues)
[![Contributors](https://img.shields.io/github/contributors/VSangarya/PackTravel)](https://github.com/VSangarya/PackTravel/graphs/contributors)
[![License](https://img.shields.io/github/license/VSangarya/PackTravel)](LICENSE)
![Languages](https://img.shields.io/github/languages/count/VSangarya/PackTravel)
[![Code Size](https://img.shields.io/github/languages/code-size/VSangarya/PackTravel)](https://github.com/VSangarya/PackTravel/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE-OF-CONDUCT.md)
[![Repo Size](https://img.shields.io/github/repo-size/VSangarya/PackTravel)](https://github.com/VSangarya/PackTravel/)

PackTravel is a web-application that connects people who want to carpool, share a cab or ride a bus together. Users can offer rides with their own vehicles, or travel together as a group in a cab or a bus. PackTravel helps you stay on a budget by reducing your travel expenses so that you don't have to miss out on that concert you've been wanting to attend 😉.

## 💎 Features
*   Users can create rides - personal vehicle, cab or taxi
*   Autocomplete for source and destination points
*   Users can send requests to join rides, cancel a ride request
*   Ride owners can accept requests from other riders to join rides, ride owners can delete their own rides
*   Forum for every ride to discuss logistics
*   Integration with Google Maps to show ride route , distance and duration.
*   Users can now get an estimated cab fare predicted with machine learning using date and time of the ride as attribute.
*   Emails are sent to ride owners when a ride capacity is reached.

https://user-images.githubusercontent.com/111834635/194171771-962a585e-5dc7-4ea3-af35-732ebd34e76c.mp4

## 👥 Audience
Any person who is looking to reduce spending on their commute expenditure can use our application.

## ⚒️ Deployment and Installation
*   PackTravel is built using MongoDB Atlas database, Django (Python) for backend-services, and HTML/CSS/JS/Bootstrap for the front-end.
*   The application can be deployed on any web-server running on premise or in the cloud. See [django deployment](https://docs.djangoproject.com/en/4.1/howto/deployment/) to setup django on a VM.
*   See [developer environment setup](INSTALL.md#--developer-environment-setup) to setup your development server.
*   Common issues faced by users while setting up the developer environment are listed [here](INSTALL.md#debugging).

## Scaling PackTravel
![Scale PackTravel](images/scale-PackTravel.png "Scale PackTravel")
*  It is possible to scale PackTravel horizontally because of how we designed the application.
*  All APIs are stateless (REST); Therefore, any application server in a cluster can handle a request.
*  We can use a CDN such as Amazon S3, Cloudflare to serve static assets (images). This enables quicker load time as CDN servers are spread across geographic reasons.
*  The bottleneck in PackTravel is the email sending feature. If we use a message queue such as Kafka to offload the task of sending an email to a different application (Kafka consumer), it will free our application server's resources quickly.
*  MongoDB is designed to handle large amounts of data and high levels of throughput. It can distribute data across multiple servers and process it in parallel. It has built-in support for sharding and this makes it easy to scale MongoDB horizontally by adding more servers as needed to handle the increased load.

## 🎯 Enhancements
*   Merge rides - users should be able to join rides in a via point between a source and a destination (feature). 
*   Ride ratings - users should be able to rate other users after a ride is complete (feature).
*   2FA - Add functionality to support 2 factor authentication to login (security)
*   Cab Fare estimation to help make a more informed ride choice

## 📨 Help and Troubleshooting
For any help or assistance regarding the software, please e-mail any of the developers with the query or a detailed description. Additionally, please use issues on GitHub for any software related issues, bugs or questions.
*   mquresh@ncsu.edu
*   apandit3@ncsu.edu
*   vnagara3@ncsu.edu
*   schopra4@ncsu.edu
*   lsangar@ncsu.edu
