# 🐺 PackTravel
[![Build](https://github.com/TripleS-org/PackTravel_G29/actions/workflows/build.yml/badge.svg)](https://github.com/TripleS-org/PackTravel_G29/actions/workflows/build.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9df7800c90694928ba61e4ff7950359a)](https://app.codacy.com/gh/TripleS-org/PackTravel_G29/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/9df7800c90694928ba61e4ff7950359a)](https://app.codacy.com/gh/TripleS-org/PackTravel_G29/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/w/TripleS-org/PackTravel_G29)](https://github.com/TripleS-org/PackTravel_G29/pulse)
[![Issues](https://img.shields.io/github/issues/TripleS-org/PackTravel_G29?color=red)](https://github.com/TripleS-org/PackTravel_G29/issues)
[![Contributors](https://img.shields.io/github/contributors/TripleS-org/PackTravel_G29)](https://github.com/TripleS-org/PackTravel_G29/graphs/contributors)
[![License](https://img.shields.io/github/license/TripleS-org/PackTravel_G29)](LICENSE)
![Languages](https://img.shields.io/github/languages/count/TripleS-org/PackTravel_G29)
[![Code Size](https://img.shields.io/github/languages/code-size/TripleS-org/PackTravel_G29)](https://github.com/TripleS-org/PackTravel_G29/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE-OF-CONDUCT.md)
[![Repo Size](https://img.shields.io/github/repo-size/TripleS-org/PackTravel_G29)](https://github.com/TripleS-org/PackTravel_G29/)

PackTravel is a web-application that connects people who want to carpool, share a cab or ride a bus together. Users can offer rides with their own vehicles, or travel together as a group in a cab or a bus. PackTravel helps you stay on a budget by reducing your travel expenses so that you don't have to miss out on that concert you've been wanting to attend 😉.

## 💎 Features
*   Users can create rides - personal vehicle, cab or taxi
*   Autocomplete for source and destination points
*   Users can send requests to join rides, cancel a ride request
*   Ride owners can accept requests from other riders to join rides, ride owners can delete their own rides
*   Forum for every ride to discuss logistics
*   Integration with Google Maps to show ride route , distance and duration.
*   Users can now get an estimated cab fare predicted with machine learning using date and time of the ride as attribute.
*   Users can set preferences in their profile
*   Created a feedback system for future analysis


## Watch the Demo Video

[Watch the video](https://github.com/TripleS-org/PackTravel_G29/raw/main/images/VIDEO-2024-11-01-20-28-18.mp4)




## 👥 Audience
Any person who is looking to reduce spending on their commute expenditure can use our application.

## ⚒️ Deployment and Installation
*   PackTravel is built using MongoDB Atlas database, Django (Python) for backend-services, and HTML/CSS/JS/Bootstrap for the front-end.
*   The application can be deployed on any web-server running on premise or in the cloud. See [django deployment](https://docs.djangoproject.com/en/4.1/howto/deployment/) to setup django on a VM.
*   See [developer environment setup](INSTALL.md#--developer-environment-setup) to setup your development server.
*   Common issues faced by users while setting up the developer environment are listed [here](INSTALL.md#debugging).

## Scaling PackTravel
![Scale PackTravel](images/scale-PackTravel.png "Scale PackTravel")
*   It is possible to scale PackTravel horizontally because of how we designed the application.
*   All APIs are stateless (REST); Therefore, any application server in a cluster can handle a request.
*   We can use a CDN such as Amazon S3, Cloudflare to serve static assets (images). This enables quicker load time as CDN servers are spread across geographic regions.
*   The bottleneck in PackTravel is the email sending feature. If we use a message queue such as Kafka to offload the task of sending an email to a different application (Kafka consumer), it will free our application server's resources quickly.
*   MongoDB is designed to handle large amounts of data and high levels of throughput. It can distribute data across multiple servers and process it in parallel. It has built-in support for sharding and this makes it easy to scale MongoDB horizontally by adding more servers as needed to handle the increased load.

## 🎯 Proposed Enhancements
*   Enable viewing of ride history in user account
*   Enable notifications if request is received accepted
*   Enable higher account security using 2FA

## 📨 Help and Troubleshooting
For any help or assistance regarding the software, please e-mail any of the developers with the query or a detailed description. Additionally, please use issues on GitHub for any software related issues, bugs or questions.

*   skulkar6@ncsu.edu
*   spustak@ncsu.edu
*   sakre@ncsu.edu
