# local-llm-rag-and-chatbot
my PrivateGPT with a local RAG system for loading doc 

## Project perposes:
Create privateCPT that ables to give correct answers in context of provided documents such as PDF, CVS 

## Project Components:
- Ollama : as LLM Serve engine
- llama3 : llm model that supports mutli langueges and used for txt embedding too
- langchain : for loading documents, text chuncks splitter and prompts templates
- Chroma DB : as data vector data base

## Install 
- Install Ollama :
  ```bash
      curl -fsSL https://ollama.com/install.sh | sh
      # Download LLAMA3
      ollama download llama3
      ollama serve
- Clone this repo
- install requiements - use py venv is better
- place ducoments inside data/ folder
- run populate_database.py to creat chrome db from loaded documents
- start the privateGPT backedn py running chatbot.py

## TODO
- LOAD CVS FILES 
