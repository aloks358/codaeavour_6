# codaeavour_6
All the projects made for Codeavour Competition can be found here.

# Codeavour Competition Management and Evaluation Portal

## Overview

The **Codeavour Competition Management and Evaluation Portal** is a web-based platform designed to manage and evaluate student submissions for the Codeavour coding competition. This portal facilitates the collection of online project submissions, offline pitch evaluations, and grading, while generating downloadable winners lists at regional, national, and international levels. Additionally, the portal provides analytics to monitor key competition metrics such as registrations, submissions, and event progress across different countries.

## Features

### Core Features:
- **Submission Management**: Allows teams to submit their projects (online presentations and offline pitches).
- **Grading System**: Regional and country partners can evaluate teams' submissions and record grades and feedback.
- **Notification System**: Sends email notifications to partners when submissions are received or evaluations are due.
- **Winners List Generation**: Automatically generates winners lists for regional, national, and international events, with downloadable reports.
- **Dashboard**: Displays key statistics such as country-wise registrations, project submissions, event dates, and winners lists for administrators and partners.

### Data Analytics Features:
- **Country-Wise Registration Data**: View and track the number of teams registered from each country.
- **Submission Progress**: Monitor the number of teams that have submitted projects.
- **Grading Completion**: Track which partners have completed grading for their teams.
- **Trends and Insights**: Basic visual analytics (graphs, charts) to help organizers track event readiness and performance.

## System Architecture

The application follows a **three-tier architecture** comprising a frontend, backend, and database. The portal integrates with the main Codeavour website for fetching team data, and supports role-based access for different users (partners, admins).

### High-Level Architecture Diagram:

```plantuml
@startuml
actor Admin
actor Partner
Admin --> WebApp: Login / Dashboard
Partner --> WebApp: Login / Dashboard
WebApp --> Database: Fetch student/team data
WebApp --> NotificationService: Send Submission Notification
WebApp --> AnalyticsService: Fetch stats for dashboard
WebApp --> GradingService: Enter scores / comments
Admin --> GradingService: View scores / Generate winners list
GradingService --> Database: Store grades
Database --> WebApp: Return data for display
AnalyticsService --> Database: Query event/submission data
@enduml
