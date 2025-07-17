from dotenv import load_dotenv
import os
import json
import re
from pydantic import BaseModel, ValidationError
from typing import Optional
from langchain_community.graphs import Neo4jGraph
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import GraphCypherQAChain
from neo4j import GraphDatabase
from neo4j.graph import Relationship
from prompts import NORMALIZE_PROMPT, CYPHER_GENERATION_TEMPLATE, ANALYSIS_PROMPT_TEMPLATE
# from langchain_neo4j import Neo4jGraph
load_dotenv()

# Environment
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")

# LLM
llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    openai_api_version=AZURE_OPENAI_VERSION,
    azure_deployment=AZURE_DEPLOYMENT,
    temperature=0,
    max_tokens=None,
)

# Neo4j Graph
graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USER,
    password=NEO4J_PASSWORD,
)

# Markdown Entity Extraction
def extract_nodes_by_label_from_markdown(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md = f.read()

    def extract_section(title):
        pattern = rf"### {re.escape(title)}\n((?:- .+\n)+)"
        match = re.search(pattern, md)
        return "\n".join([line[2:].strip() for line in match.group(1).strip().split("\n") if line.startswith("- ")]) if match else ""

    group_companies = extract_section("GroupCompany")
    inventorylevel1 = extract_section("InventoryLevel1")
    inventorylevel2 = extract_section("InventoryLevel2")
    inventorylevel3 = extract_section("InventoryLevel3")
    inventorylevel4 = extract_section("InventoryLevel4")
    inventory_type = "\n".join([inventorylevel1, inventorylevel2, inventorylevel3, inventorylevel4])
    return group_companies, inventory_type

# Pydantic Normalization
class NormalizationResult(BaseModel):
    company_name: Optional[str]
    inventory_type: Optional[str]
    year: Optional[str]
    canonicalized_query: Optional[str]

def normalize_entities(user_query):
    prompt = NORMALIZE_PROMPT.format(user_query=user_query, group_companies=group_companies, inventory_type=inventory_type)
    result = llm.invoke(prompt)
    content = getattr(result, 'content', str(result))
    print("Raw LLM output:", content)
    match = re.search(r"\{.*\}", content, re.DOTALL)
    json_str = match.group(0) if match else "{}"
    try:
        return NormalizationResult.model_validate_json(json_str)
    except ValidationError as ve:
        print("Validation error:", ve)
        return None

# Neo4j Result Serialization
def serialise_record(rec):
    out = {}
    for key, val in rec.items():
        if hasattr(val, "labels"):  # Node
            out[key] = {"_labels": list(val.labels), **dict(val)}
        elif isinstance(val, list):  # Path
            out[key] = [{"_type": rel.type, **dict(rel)} for rel in val]
        elif isinstance(val, Relationship):
            out[key] = {"_type": val.type, **dict(val)}
        else:
            out[key] = val
    return out

def run_and_format(uri, user, pwd, query):
    driver = GraphDatabase.driver(uri, auth=(user, pwd))
    with driver.session() as ses:
        rows_raw = [serialise_record(r) for r in ses.run(query)]
    return rows_raw

# Extract schema
md_path = "kg_schema_overview3.md"
group_companies, inventory_type = extract_nodes_by_label_from_markdown(md_path)

# Setup GraphCypherQAChain
cypher_prompt = PromptTemplate(
    input_variables=["query"],
    template=CYPHER_GENERATION_TEMPLATE,
)

chain = GraphCypherQAChain.from_llm(
    graph=graph,
    cypher_llm=llm,
    qa_llm=llm,
    cypher_prompt=cypher_prompt,
    verbose=False,
    allow_dangerous_requests=True,
    return_intermediate_steps=True
)

# Main Execution

# Exception
user_query="which inventory tools has the highest difference for AS from 2023 to 2024?"


# Correct
# user_query="What is the difference in Stock-in-trade count for the company 133-FES from FY24 to FY23?"

# Correct
# user_query="Which inventory has the highest difference and the lowest difference in count for year 2023 and 2024"

# Correct
# user_query="which group company have lowest 'Finished products produced' count in 2023?"



# Test Problem
# user_query="What factors contribute to the difference in Finished Goods for SWARAJ for 2023 and 2024?"

# Test Correct
# user_query="Which GroupCompany nodes have HAS_AMOUNT relationships to both 'Finished Goods' (Level2) and 'Clg Stock - Finished Goods - B/s' (Level4) within the same year, and list the relationship properties for the first overlapping year chronologically?"


# Example madhe dilay tari wrong
user_query="For each GroupCompany in ['AS','MDS'], find all InventoryLevel3 nodes under 'Raw Material & Mfg. Componets' and the corresponding HAS_AMOUNT for year '2023', then also include any direct HAS_AMOUNT from the same companies to that InventoryLevel1 parent for comparative analysis."


# Test Correct
# user_query="For every GroupCompany, show all direct HAS_AMOUNT links to any InventoryLevel2 or InventoryLevel3 where the year is either '2023' or '2024', and include any parent InventoryLevel1 node that leads into those InventoryLevel2 nodes."


# Test Correct
# user_query="Identify every InventoryLevel4 connected to 'Tools' via any depth of HAS_SUB_INVENTORY, then find all GroupCompany amount relationships to both the InventoryLevel2 'Tools' and each discovered InventoryLevel4, filtering to year '2023', and return every node and relationship property."






# Wrong
# user_query="Can you explain the reasons for the increase in the purchase of stock in trade as shown in the Inventory schedule?"

# Test Correct
user_query="What factors contributed to the rise in inventory purchases compared to the previous period?"

# Test Correct
# user_query="How does the increase in stock purchases align with the company's sales growth and inventory management strategy?"

normalized = normalize_entities(user_query)
query = normalized.canonicalized_query

result = chain.invoke({
    "query": query,
    "verbose": False
})

final_query = result['intermediate_steps'][0]['query']
# final_query = """
# MATCH (inv4:InventoryLevel4 {name: "Inventory Oils, Grease & Chemicals"})
# MATCH (gc:GroupCompany)-[r:HAS_AMOUNT]->(inv4)
# WHERE r.year IN ["FY23","FY24"]
# RETURN gc, r, inv4
# """
print('CYPHER QUERY GENERATED')
print(final_query)


rows = run_and_format(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, final_query)

# Format and analyze
json_results = [row for row in rows]
print('jsopn results')
print(json_results)

# Modern Runnable chain (replaces deprecated LLMChain)
analysis_prompt = ChatPromptTemplate.from_template(ANALYSIS_PROMPT_TEMPLATE)
analysis_chain = analysis_prompt | llm

response = analysis_chain.invoke({"json_data": json_results, "user_query": normalized})

print('FINAL RESULT')
print(response.content if hasattr(response, "content") else response)


'''
No results for this queries
1. "What are the FY23 and FY24 values for Inventory Oils, Grease & Chemicals under each group company?"
2. "What are all sub-inventories under 'Raw Material & Mfg. Componets' and which companies are linked to them?"

'''