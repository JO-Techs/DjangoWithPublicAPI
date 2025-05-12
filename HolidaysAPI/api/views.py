import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import json

class ColorMindAPI(APIView):
    """
    API endpoint to interact with the Colormind.io API
    """
    def post(self, request):
        try:
            # Colormind API endpoint
            url = "http://colormind.io/api/"
            
            # Request a random color palette
            payload = {"model": "default"}
            
            # Make the request with proper headers
            response = requests.post(
                url, 
                data=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": f"Failed to fetch color palette from Colormind API. Status code: {response.status_code}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CalendarificAPI(APIView):
    """
    API endpoint to interact with the Calendarific API
    """
    def get(self, request):
        try:
            # Get parameters from request
            country = request.query_params.get('country', 'US')
            year = request.query_params.get('year', datetime.now().year)
            month = request.query_params.get('month')
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            
            # For demo purposes, we'll use mock data instead of the actual API
            # since we don't have a real API key
            mock_holidays = [
                {
                    "name": "New Year's Day",
                    "description": "New Year's Day is the first day of the year in the Gregorian calendar.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-01-01",
                        "datetime": {
                            "year": int(year),
                            "month": 1,
                            "day": 1
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Martin Luther King Jr. Day",
                    "description": "Martin Luther King Jr. Day honors the life and work of the civil rights activist.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-01-16",
                        "datetime": {
                            "year": int(year),
                            "month": 1,
                            "day": 16
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Valentine's Day",
                    "description": "Valentine's Day is a time to celebrate romance and love.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-02-14",
                        "datetime": {
                            "year": int(year),
                            "month": 2,
                            "day": 14
                        }
                    },
                    "type": ["Observance"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Presidents' Day",
                    "description": "Presidents' Day honors all past presidents of the United States.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-02-20",
                        "datetime": {
                            "year": int(year),
                            "month": 2,
                            "day": 20
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Memorial Day",
                    "description": "Memorial Day commemorates all men and women who have died in military service for the United States.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-05-29",
                        "datetime": {
                            "year": int(year),
                            "month": 5,
                            "day": 29
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Independence Day",
                    "description": "Independence Day celebrates the Declaration of Independence of the United States from Great Britain in 1776.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-07-04",
                        "datetime": {
                            "year": int(year),
                            "month": 7,
                            "day": 4
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Labor Day",
                    "description": "Labor Day celebrates the achievements of workers.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-09-04",
                        "datetime": {
                            "year": int(year),
                            "month": 9,
                            "day": 4
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Halloween",
                    "description": "Halloween is a celebration observed in many countries on October 31.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-10-31",
                        "datetime": {
                            "year": int(year),
                            "month": 10,
                            "day": 31
                        }
                    },
                    "type": ["Observance"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Veterans Day",
                    "description": "Veterans Day honors those who have served in the United States Armed Forces.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-11-11",
                        "datetime": {
                            "year": int(year),
                            "month": 11,
                            "day": 11
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Thanksgiving Day",
                    "description": "Thanksgiving Day is a national holiday celebrated on various dates in the United States, Canada, and other countries.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-11-23",
                        "datetime": {
                            "year": int(year),
                            "month": 11,
                            "day": 23
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "Christmas Day",
                    "description": "Christmas Day celebrates the birth of Jesus Christ.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-12-25",
                        "datetime": {
                            "year": int(year),
                            "month": 12,
                            "day": 25
                        }
                    },
                    "type": ["National holiday"],
                    "locations": "All",
                    "states": "All"
                },
                {
                    "name": "New Year's Eve",
                    "description": "New Year's Eve is the last day of the year in the Gregorian calendar.",
                    "country": {
                        "id": "us",
                        "name": "United States"
                    },
                    "date": {
                        "iso": f"{year}-12-31",
                        "datetime": {
                            "year": int(year),
                            "month": 12,
                            "day": 31
                        }
                    },
                    "type": ["Observance"],
                    "locations": "All",
                    "states": "All"
                }
            ]
            
            # Filter by date range if provided
            if start_date and end_date:
                start = datetime.strptime(start_date, '%Y-%m-%d')
                end = datetime.strptime(end_date, '%Y-%m-%d')
                
                filtered_holidays = []
                for holiday in mock_holidays:
                    holiday_date = datetime.strptime(holiday['date']['iso'], '%Y-%m-%d')
                    if start <= holiday_date <= end:
                        filtered_holidays.append(holiday)
                
                return Response({"holidays": filtered_holidays}, status=status.HTTP_200_OK)
            
            # Format the response to match Calendarific API structure
            response_data = {
                "meta": {
                    "code": 200
                },
                "response": {
                    "holidays": mock_holidays
                }
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UselessFactAPI(APIView):
    """
    API endpoint to interact with the Useless Facts API
    """
    def get(self, request):
        try:
            # Useless Facts API endpoint
            url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
            
            # Parameters
            params = {
                "language": "en"
            }
            
            # Make request to Useless Facts API
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Failed to fetch useless fact"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )