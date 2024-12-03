import requests
import csv

def fetch_indian_region_codes(country_code):
    api_url = f"https://country-state-city-search-rest-api.p.rapidapi.com/cities-by-countrycode"
    headers = {
        "X-RapidAPI-Key": "654d8cdc45mshe01e78a2bdaeb9bp1e514bjsn81319adce348",
        "X-RapidAPI-Host": "country-state-city-search-rest-api.p.rapidapi.com"
    }
    params = {
        "countrycode": country_code
    }

    try:
        response = requests.get(api_url, headers=headers, params=params)

        cities = response.json() 
        if not cities:
            print("No cities found or empty response.")
            return
        
        with open("Indian_cities.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["City Names"])
            for city in cities:
                city_name = city.get('name', 'Unknown')
                writer.writerow([city_name])
        
        print("City names have been saved to Indian_cities.csv")

    except requests.exceptions.RequestException as e:
        print("Error fetching cities:", e)

fetch_indian_region_codes("in")
