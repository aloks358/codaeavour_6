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

2. **Install dependencies**:

    ```bash
      Copy code
      cd backend
      npm install
      cd ../frontend
      npm install

3. **Set up environment variables: Create a .env file in the backend folder**:

      DATABASE_URL=your-database-url
      REDIS_URL=your-redis-url
      JWT_SECRET=your-jwt-secret

4. **Run the PostgreSQL database: Make sure PostgreSQL is running on your local machine or use a hosted version.**

5. **Run the Redis server: Ensure Redis is running locally or hosted for background jobs.**

6. **Run the app**:

**Start the backend**:
    ```bash
      cd backend
      npm run dev

**Start the frontend**:
    ```bash
    Copy code
      cd frontend
      npm start

7. **Run with Docker: Alternatively, you can run the entire application using Docker**:

    ```bash
    Copy code
    docker-compose up

## API Endpoints
### Authentication
POST /api/auth/login: Login a user (admin or partner).
POST /api/auth/register: Register a new partner.
### Submissions
GET /api/submissions: Fetch all submissions for a partner.
POST /api/submissions: Upload a new project submission.
### Grading
POST /api/grades: Submit grades for a project.
GET /api/grades: Fetch grading information for a partner.
### Winners List
GET /api/winners/regional: Fetch the regional winners.
GET /api/winners/national: Fetch the national winners.
GET /api/winners/international: Fetch the international winners.

## Deployment

### Docker:

**Build Docker images**:
    ```bash
    Copy code
    docker build -t codeavour-portal
**Run the Docker containers**:
    ```bash
    Copy code
    docker-compose up

## AWS Elastic Beanstalk:

Deploy the backend and frontend using Elastic Beanstalk environments.
Set up the PostgreSQL database and Redis as external services.

Contribution

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add some feature').
