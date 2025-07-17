from dotenv import load_dotenv
import os

load_dotenv()

neo4j_uri = os.getenv("NEO4J_URI")
neo4j_username = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai_api_version = os.getenv("AZURE_OPENAI_VERSION")
deployment_name = os.getenv("AZURE_DEPLOYMENT")

print(openai_api_key)
print(openai_api_base)
print(openai_api_version)
print(deployment_name)