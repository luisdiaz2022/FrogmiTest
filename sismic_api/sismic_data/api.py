"""GeoJson Api"""

# Utilities
import requests


def get_sismic_data():
    """We get the data from the GeoJSON"""

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = {
            "type": "FeatureCollection",
            "metadata": {
                "generated": 1713233786000,
                "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson",
                "title": "USGS All Earthquakes, Past Month",
                "status": 200,
                "api": "1.10.3",
                "count": 9586,
            },
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "mag": 1.69,
                        "place": "10 km N of Cloverdale, CA",
                        "time": 1713233330270,
                        "updated": 1713233425181,
                        "tz": None,
                        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc74035056",
                        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc74035056.geojson",
                        "felt": None,
                        "cdi": None,
                        "mmi": None,
                        "alert": None,
                        "status": "automatic",
                        "tsunami": 0,
                        "sig": 44,
                        "net": "nc",
                        "code": "74035056",
                        "ids": ",nc74035056,",
                        "sources": ",nc,",
                        "types": ",nearby-cities,origin,phase-data,",
                        "nst": 24,
                        "dmin": 0.07091,
                        "rms": 0.05,
                        "gap": 153,
                        "magType": "md",
                        "type": "earthquake",
                        "title": "M 1.7 - 10 km N of Cloverdale, CA",
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [-123.0058365, 38.8986664, 0.91],
                    },
                    "id": "nc74035056",
                },
            ],
        }

        if "features" in data:
            return data["features"]
        else:
            print("No se encontraron características en los datos sísmicos.")
        return None

    except requests.exceptions.Timeout:
        print("Tiempo de espera agotado al intentar obtener los datos sísmicos.")
        return None

    except requests.exceptions.ConnectionError:
        print("Error de conexión al intentar obtener los datos sísmicos.")
        return None

    except requests.exceptions.HTTPError as err:
        print("Error HTTP al intentar obtener los datos sísmicos:", err)
        return None

    except Exception as e:
        print("Ocurrió un error al obtener los datos sísmicos:", e)
        return None
