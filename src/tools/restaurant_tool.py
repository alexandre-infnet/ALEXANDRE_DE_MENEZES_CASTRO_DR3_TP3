import requests
from langchain.tools import Tool


def search_restaurants(radius: int = 500) -> str:
    """
    Busca restaurantes próximos ao centro de New York dentro de um raio especificado.

    Args:
        radius (int, optional): Raio em metros para buscar restaurantes em New York. O valor padrão é 500 metros.

    Returns:
        str: Lista de até cinco restaurantes encontrados no raio especificado, incluindo seus nomes e coordenadas.
        Em caso de falha ou se nenhum restaurante for encontrado, retorna uma mensagem informativa.
    """
    latitude, longitude = 40.7128, -74.0060
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
        node["amenity"="restaurant"](around:{radius},{latitude},{longitude});
    );
    out body;
    """
    response = requests.get(overpass_url, params={"data": query})

    if response.status_code == 200:
        data = response.json()
        elements = data.get("elements", [])

        if not elements:
            return "Nenhum restaurante encontrado no raio especificado em New York. Tente aumentar o raio ou verificar os critérios."

        restaurants = []
        for element in elements[:5]:
            name = element.get("tags", {}).get("name", "Nome não disponível")
            lat = element["lat"]
            lon = element["lon"]
            restaurants.append(f"{name} (Localização: {lat},{lon})")

        return "Restaurantes em New York encontrados:\n" + "\n".join(restaurants)
    else:
        return "Não foi possível realizar a busca no momento. Por favor, tente novamente mais tarde."


def get_restaurant_tool():
    tool = Tool(
        name="BuscaRestaurantes",
        func=search_restaurants,
        description="Busca restaurantes próximos no centro de New York (coordenadas fixas). Os resultados são limitados a New York.",
    )

    return tool
