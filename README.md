# Codeavour Competition Management and Evaluation Portal

## Overview

The **Codeavour Competition Management and Evaluation Portal** is a web-based platform designed to manage and evaluate student submissions for the Codeavour coding competition. The portal allows partners and admins to view, grade, and track project submissions, generate winners lists, and monitor progress across regional, national, and international levels. It also provides real-time notifications and data dashboards for effective event management.

## Tech Stack

- **Frontend**: React.js, Axios, Chart.js/D3.js for visualization.
- **Backend**: Node.js, Express.js, Socket.io for real-time communication.
- **Database**: PostgreSQL with Sequelize ORM.
- **Background Jobs**: Bull.js with Redis for task queuing.
- **Deployment**: Docker, AWS Elastic Beanstalk, Nginx for reverse proxy.

## Features

### Core Features:
- **Submission Management**: Teams can upload projects, which are stored securely.
- **Grading System**: Partners can evaluate and grade submissions, adding feedback for each project.
- **Real-time Notifications**: Partners receive notifications when new submissions are uploaded or grading deadlines approach.
- **Winners List**: Automatically generates winners lists for each stage (regional, national, international) and allows for downloads.
- **Data Dashboard**: Displays country-wise registration data, submission statistics, and event information.
  
### Data Analytics Features:
- **Country-wise Registrations**: Visualize registration trends by country or region.
- **Submission Progress**: Track the number of projects submitted in real-time.
- **Grading Status**: Monitor grading progress and completion rates for partners.

## Architecture

### Frontend (React.js)
- **Dashboard**: Displays key competition statistics and submission data.
- **Forms**: Submission form for teams to upload projects, and grading form for partners.
- **Visualization**: Uses **Chart.js** or **D3.js** to visualize data like submission progress and country-wise registrations.

### Backend (Node.js + Express)
- **APIs**: RESTful APIs to handle authentication, submissions, grading, and event data.
- **Real-Time Notifications**: Uses **Socket.io** for real-time updates and notifications to partners.
- **Background Jobs**: **Bull.js** and **Redis** to handle background tasks like file processing and sending notifications.

### Database (PostgreSQL + Sequelize)
- **Tables**:
  - **Users**: Role-based access control (admin, partner).
  - **Teams**: Stores team details and partner codes.
  - **Submissions**: Stores project submission data.
  - **Grades**: Stores grading data and feedback.
  - **Events**: Stores event information (regional, national, international).

## Installation

### Prerequisites
- **Node.js** (v14+)
- **PostgreSQL** (v12+)
- **Redis** (for background jobs)
- **Docker** (for containerization)

### Steps to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/codeavour-portal.git
   cd codeavour-portal
