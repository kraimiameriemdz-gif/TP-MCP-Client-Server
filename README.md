## MCP Client–Server Travel Assistant

## Description :
-Ce projet implémente une architecture **client–serveur** basée sur le **Model Context Protocol (MCP)** en utilisant **LangChain** et **Ollama**.
-L’objectif est de créer un assistant intelligent capable de :
* convertir des euros en dinars algériens
* fournir la météo d’une ville
* utiliser dynamiquement des outils exposés par un serveur MCP
* 
## Concepts utilisés :
* Model Context Protocol (MCP)
* Architecture client–serveur
* Tool Calling avec un LLM
* Agents LangChain
* LLM local avec Ollama
* 
## Architecture :
Utilisateur
⬇
Client MCP (`mcp_client.py`)
⬇
LLM (Ollama)
⬇
Outils MCP
⬇
Serveur MCP (`mcp_server.py`)

## Outils disponibles : 

### 1- get_weather(city)
Retourne une météo simulée :

* Alger → 22°C, ensoleillé
* Oran → 19°C, venteux
* Constantine → 16°C, nuageux

### 2- eur_to_dzd(amount)
Convertit des euros en dinars algériens :
* Taux utilisé : 1 EUR = 145 DZD
* 
### Question :
Je vais à Alger avec 120 euros. Combien cela fait en dinars et quel temps fait-il ?

### Réponse attendue :
120 euros correspondent à 17400 dinars algériens.
À Alger, le temps est de 22°C et ensoleillé.

## Fonctionnement :
1. Le client envoie la requête au LLM
2. Le LLM décide d’utiliser des outils
3. Le client appelle les outils via MCP :
   * conversion EUR → DZD
   * météo
4. Le LLM combine les résultats
5. Réponse finale générée
## Auteur :
Projet réalisé dans le cadre d’un TP en intelligence artificielle.
