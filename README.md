
# Maven

**Maven** is a women's safety app designed with the Indian audience in mind, focusing on secure navigation, real-time alerts, and advanced movement detection. This project is intended to showcase the implementation and features rather than for public use.

## Project Overview

Maven integrates the following key features:

- **Safe Route Navigation**: Provides routes with the highest number of police stations and other safety features.
- **Red Zone Alerts**: Sends notifications if a user enters a high-risk area, alerting trusted contacts.
- **Smart Movement Detection**: Uses machine learning to detect unusual phone movements and triggers alerts, locks the phone, and captures essential data.

## Technology Stack

- **Frontend**: React Native
- **Backend**: Django
- **Machine Learning**: TensorFlow Lite
- **Maps & Location**: Google Maps API, Geofencing
- **Notifications**: Firebase Cloud Messaging

## Project Structure

- **Backend**: Contains Django code for APIs and database management.
- **Frontend**: Contains React Native code for the mobile application, including maps integration and UI/UX design.
- **Machine Learning**: Includes TensorFlow Lite model for movement detection and processing.

## Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AsHuToShSiNgH02/Maven
   cd maven/backend
   ```

2. Set up a Python virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Configure environment variables in a `.env` file and run migrations:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the React Native project directory:
   ```bash
   cd MavenMobile
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the React Native development server:
   ```bash
   npm start
   ```

## Features Showcase

- **Safe Route Navigation**: Demonstrates how routes are calculated and prioritized based on safety features.
- **Red Zone Alerts**: Shows the notification system for entering high-risk areas.
- **Movement Detection**: Illustrates how the machine learning model detects unusual movements and responds.

## Contributing

This repository is primarily for showcasing purposes. Contributions are welcome to improve the implementation or add new features. Please fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For more information about the project or any inquiries, please contact [your-ashutoshin7499@gmail.com](mailto:your-ashutoshin7499@gmail.com).

---

**Maven**: Showcasing advanced features in women's safety technology.
