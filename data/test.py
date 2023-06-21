#用TextLoader
from langchain.document_loaders import TextLoader
file_type = "**/*.pdf"
loader = DirectoryLoader(file, glob = file_type, loader_cls=TextLoader)
docs = loader.load()