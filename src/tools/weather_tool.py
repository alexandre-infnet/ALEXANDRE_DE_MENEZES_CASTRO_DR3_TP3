import requests
from langchain.tools import Tool


#API_KEY_WEATHER = "757116922b4645a18e7111413241512"


def get_weather(location: str) -> str:
    """
    Consulta as condições climáticas atuais para uma localização específica.

    Args:
        location (str): Nome da cidade ou coordenadas (latitude,longitude) para a qual as condições climáticas devem ser consultadas.

    Returns:
        str: Informações detalhadas sobre o clima, incluindo temperatura, condição do tempo, sensação térmica e velocidade do vento.
        Em caso de erro, retorna uma mensagem informando que a consulta falhou.
    """
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": API_KEY_WEATHER, "q": location}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        location_name = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        feels_like = data["current"]["feelslike_c"]
        wind = data["current"]["wind_kph"]

        return (
            f"O clima em {location_name}, {region} ({country}) é {condition}, "
            f"com temperatura de {temperature}°C (sensação térmica de {feels_like}°C) "
            f"e vento a {wind} km/h."
        )
    else:
        return "Não foi possível obter informações climáticas. Verifique a localização ou tente novamente mais tarde."


def get_weather_tool():
    tool = Tool(
        name="ConsultaClima",
        func=get_weather,
        description="Consulta as condições climáticas para uma localização específica. Informe a cidade ou coordenadas.",
    )

    return tool
