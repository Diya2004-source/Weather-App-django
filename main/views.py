from django.shortcuts import render
import requests

def weather(request):
    city = request.GET.get("city")
    weather_data = None
    error = None

    if city:
        api_key = "a4214440a14fba1bca6aa7ac7c66e689"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            if str(data.get("cod")) != "200":
                error = data.get("message", "Something went wrong!")
            else:
                weather_data = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"]
                }
        except requests.exceptions.RequestException as e:
            error = f"Network error: {e}"

    return render(request, "weather.html", {"weather": weather_data, "error": error})
