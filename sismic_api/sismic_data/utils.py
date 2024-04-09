import requests

def get_sismic_data():
        """We get the data from the GeoJSON"""

        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Verify if the request was successful
            data = response.json()  # Updates the response to JSON
            return data['features']  # Return the list of sismic events
        except requests.exceptions.RequestException as e:
            print('Error al obtener los datos sismológicos:', e)
            return None