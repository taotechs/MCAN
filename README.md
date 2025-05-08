# MCAN Lagos Website

Official website for the Muslim Corpers' Association of Nigeria (MCAN), Lagos State Chapter.

## Features

- Responsive and modern Islamic-themed design
- Member management system with digital ID cards
- Event management and calendar
- News and blog section
- Gallery and media management
- Admin dashboard
- Donation portal integration
- Corps member registration system

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Authentication**: Flask-Login
- **Payment Integration**: Paystack/Flutterwave

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
5. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
6. Run the development server:
   ```bash
   flask run
   ```

## Project Structure

```
mcan/
├── app/
│   ├── static/          # Static files (CSS, JS, images)
│   ├── templates/       # HTML templates
│   ├── models/         # Database models
│   ├── routes/         # Route handlers
│   ├── utils/          # Utility functions
│   └── __init__.py     # App initialization
├── migrations/         # Database migrations
├── tests/             # Test files
├── .env               # Environment variables
├── config.py          # Configuration
└── run.py            # Application entry point
```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 