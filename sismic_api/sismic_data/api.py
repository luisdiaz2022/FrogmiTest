import requests

def get_sismic_data():
        """We get the data from the GeoJSON"""

        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if 'features' in data:
                return data['features']
            else:
                print('No se encontraron características en los datos sísmicos.')
            return None
        
        except requests.exceptions.Timeout:
            print('Tiempo de espera agotado al intentar obtener los datos sísmicos.')
            return None

        except requests.exceptions.ConnectionError:
            print('Error de conexión al intentar obtener los datos sísmicos.')
            return None

        except requests.exceptions.HTTPError as err:
            print('Error HTTP al intentar obtener los datos sísmicos:', err)
            return None

        except Exception as e:
            print('Ocurrió un error al obtener los datos sísmicos:', e)
            return None