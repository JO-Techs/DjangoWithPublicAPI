# Holiday Color Explorer

A beautiful Django REST Framework application that integrates three public APIs:
- **Calendarific API**: For fetching holiday information based on date ranges
- **Colormind.io API**: For generating beautiful color palettes that automatically change the website theme
- **Useless Facts API**: For displaying random interesting facts

## Features

- Search for holidays by country and date range
- Automatic color palette generation that changes the website theme
- Random useless facts that update with each search
- Responsive design that adapts to the color palette
- RESTful API endpoints for all services

## Setup Instructions

1. Clone this repository
2. Install dependencies:
   ```
   pip install django djangorestframework requests
   ```
3. Get a free API key from [Calendarific](https://calendarific.com/)
4. Update the API key in `api/views.py`
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Visit http://localhost:8000 in your browser

## API Endpoints

- `GET /api/holidays/`: Get holidays for a specific date range
  - Parameters:
    - `country`: Country code (default: US)
    - `year`: Year (default: current year)
    - `start_date`: Start date in YYYY-MM-DD format
    - `end_date`: End date in YYYY-MM-DD format

- `POST /api/colors/`: Generate a new color palette
  - No parameters required

- `GET /api/useless-fact/`: Get a random useless fact
  - No parameters required

## Technologies Used

- Django
- Django REST Framework
- HTML/CSS/JavaScript
- Bootstrap 5
- Calendarific API
- Colormind.io API
- Useless Facts API

## License

MIT