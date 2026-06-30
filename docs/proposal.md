# UMCSSA Event Management Platform Proposal

## 1. Project Overview

The UMCSSA Event Management Platform is a full-stack web application designed to streamline the management of student events organized by the University of Michigan Chinese Students and Scholars Association (UMCSSA).

The platform aims to automate repetitive administrative tasks such as event registration, invitation distribution, participant check-in, reimbursement submission, airport pickup coordination, and volunteer management. By replacing manual Excel-based workflows with a centralized web system, the platform will improve efficiency, reduce human error, and provide a better experience for both organizers and participants.

---

## 2. Background

Currently, many UMCSSA activities rely on Google Forms and Excel spreadsheets.

Examples include:

* New Student Meet & Greet registration
* Airport Pickup registration
* Reimbursement requests
* Volunteer recruitment
* Event attendance tracking

While these tools are convenient, organizers still perform many tasks manually, including:

* Searching participant names during check-in
* Verifying registration status
* Sending invitations individually
* Tracking reimbursement progress
* Managing participant statistics

These repetitive tasks become increasingly inefficient as event sizes grow.

---

## 3. Objectives

This project aims to build a reusable platform that can support multiple UMCSSA events while minimizing manual administrative work.

The platform should:

* simplify event registration
* automate participant verification
* support real-time event check-in
* centralize participant information
* provide administrative dashboards
* improve data management and organization

---

## 4. Minimum Viable Product (MVP)

The first version of the platform will include:

### Event Registration

* online registration form
* participant database
* administrator dashboard

### Check-in System

* participant lookup using UM email
* automatic registration verification
* attendance recording
* check-in timestamp

### Dashboard

* registered participants
* checked-in participants
* attendance rate
* total attendees

---

## 5. Future Development

Planned future features include:

* QR Code check-in
* Invitation generator
* Airport pickup management
* Volunteer management
* Reimbursement system
* Email notification system
* Member database
* Analytics dashboard
* Multi-event support
* Role-based administrator accounts

---

## 6. Technology Stack

### Frontend

* React
* Tailwind CSS

### Backend

* FastAPI (Python)

### Database

* Excel (development)
* SQLite (MVP)
* PostgreSQL (future)

### Deployment

* Vercel
* Render

### Version Control

* Git
* GitHub

---

## 7. Expected Outcomes

After completion, the platform will significantly reduce manual administrative work for UMCSSA organizers and provide a scalable solution for future student organization events.

The project also serves as a practical full-stack software engineering experience integrating frontend development, backend APIs, database management, cloud deployment, and version control.
