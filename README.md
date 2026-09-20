# CivicClean AI – AI-Powered Community Waste Management System

CivicClean AI is a web-based prototype designed to make community waste reporting more organized and accessible. Citizens can explore the platform, submit waste reports, view report status, explore rewards and community information, and preview AI-assisted waste analysis concepts.

## Project Status

This submission is a **frontend/prototype demonstration** created for the AI for Sustainability internship project.

The current prototype does **not require Supabase, a database, API keys, or external authentication** to demonstrate the user interface and workflow.

The login/register flow is implemented for **prototype demonstration only** and should not be treated as production authentication.

## Main Features

- CivicClean AI landing page
- Citizen registration and login prototype
- Citizen dashboard
- Waste reporting interface
- AI Detection Preview
- My Reports
- Rewards and points interface
- Community section
- Citizen profile
- Admin portal interface
- Responsive green-and-white sustainability-focused UI
- Real photographic assets for the interface

## AI Concept

The prototype demonstrates the concept of using AI-assisted analysis to support:

- Waste category identification
- Priority assessment
- Suggested actions for reported waste
- More organized handling of community waste reports

The current version presents these capabilities as a prototype interface. A production implementation can connect the AI layer to a real model/API in a future phase.

## Technology Stack

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- IBM Bob AI – used during development for project review, improvement suggestions, user-experience feedback, and responsible-AI considerations

## Running the Prototype Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Future Backend Integration – Supabase

Supabase is **not required for the current prototype**. For a future production version, Supabase can be used for authentication, PostgreSQL database storage, file storage, and other backend services.

A future `.env` file can contain values such as:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_PUBLISHABLE_KEY=your_supabase_publishable_key
```

**Never commit `.env` or real API/secret keys to GitHub.** Keep `.env` in `.gitignore` and configure production credentials through the deployment platform's environment variables.

## Future Enhancements

- Supabase authentication and database
- Secure image/file storage
- Real AI waste classification
- Automated priority scoring
- Waste hotspot analytics
- Duplicate/fraud report detection
- Notifications
- Municipality workflow integration
- Sustainability and impact analytics

## SDG Alignment

- **SDG 11 – Sustainable Cities and Communities**
- **SDG 12 – Responsible Consumption and Production**
- **SDG 13 – Climate Action**

## Demo Video

The final demo recording is included in this repository: [Watch / Open Demo Video](demo/CivicClean-AI-Demo.mp4)

## Project Presentation

Project presentation/PPT can be added here after the final presentation file is prepared.

## IBM Bob AI Usage

IBM Bob AI was used during the development of CivicClean AI to obtain practical development ideas and improvement suggestions related to user experience, AI-assisted categorization, responsible AI, accessibility, security, backend planning, and future AI integration. The suggestions were reviewed during the development process.

## Important Security Note

This repository is intended for the prototype version. No real Supabase credentials, passwords, secret keys, or other sensitive credentials should be stored in the repository.
