import asyncio
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

async def main(): #On définit la fonction principale en mode asynchrone — nécessaire car on attend des réponses réseau.
    client = MultiServerMCPClient( #créer un client MCP qui connecte au serveur 
        {
            "travel_tools": {
                "command": "python",
                "args": ["mcp_server.py"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools() #Récupérer les outils dynamiquement ; await signifie qu'on attend la réponse

    llm = ChatOllama( #utiliser ollama en local
        model="qwen2.5:0.5b-instruct-q4_K_M",
        temperature=0, #signifie que le modèle sera déterministe — toujours la même réponse pour la même question.
    )

    agent = create_react_agent( #créer l'agent en combinant 
        model=llm, #le modèle
        tools=tools, #les outils
        prompt=( #les interactions 
            "Tu es un assistant voyage. "
            "Tu dois répondre complètement à la question. "
            "Utilise tous les outils nécessaires." 
        ),
    )

    result = await agent.ainvoke( #poser la qst à l'agent,
        #il réflichit, appelle les outils et retourneune une rep
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Je vais à Alger avec 120 euros. "
                        "Combien cela fait en dinars ?"
                    ),
                }
            ]
        }
    )

    for msg in result["messages"]: #On affiche tous les messages échangés pendant l'exécution
        print(type(msg).__name__)
        print(msg)
        print("-" * 50)

    print(result["messages"][-1].content) #msg finale

if __name__ == "__main__":
    asyncio.run(main())