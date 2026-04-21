from mcp.server.fastmcp import FastMCP  

mcp = FastMCP("travel-tools")

@mcp.tool()  # met cet outil en vitrine — le client pourra le voir et l'utiliser.

def get_weather(city: str) -> str: #fct qui prend une ville en entrée et retourne un texte
    """Retourne une météo simplifiée."""
    fake_weather = { #dictionnaire de fausse donnnées météo, on simule une vraie API météo 
        "Alger": "22°C, ensoleillé",
        "Oran": "19°C, venteux",
        "Constantine": "16°C, nuageux",
    }
    return fake_weather.get(city, f"Météo indisponible pour {city}")
    #On retourne la météo de la ville demandée. Si la ville n'existe pas dans le dictionnaire, on retourne un message d'erreur.
@mcp.tool() #2eme outil, prend un montant en euros et retourne du texte.


def eur_to_dzd(amount_eur: float) -> str:
    """Convertit EUR en DZD."""
    rate = 145.0
    dzd = amount_eur * rate
    return f"{amount_eur:.2f} EUR = {dzd:.2f} DZD"

if __name__ == "__main__":
    mcp.run()
