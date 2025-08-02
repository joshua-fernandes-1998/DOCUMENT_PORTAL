import sys
from dotenv import load_dotenv
import pandas as pd
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.model import *
from prompt.prompt_library import PROMPT_REGISTRY
from utils.model_loader import ModelLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentComparatorLLM:
    def __init__(self):
        load_dotenv()
        self.logger = CustomLogger().get_logger(__name__)
        self.loader = ModelLoader()
        self.llm = self.loader.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)
        self.prompt = PROMPT_REGISTRY["document_comparison"]
        self.chain = self.prompt | self.llm | self.parser | self.fixing_parser
        self.log.info("DocumentComparatorLLM initialised with model and parsor")
    
    def compare_documents(self):
        """
        Compares two documents and returns the differences.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in compare_documents: {e}")
            raise DocumentPortalException("An error occurred while comparing documents.",sys)
    
    def _format_reponse(self):
        """
        Formats the response from the LLM into a dictionary.
        It's a private method, hence "_" in front of the name.
        """
        try:
            pass
        except Exception as e:
            self.log.error("Error formatting response into DataFrame", error=str(e))
            raise DocumentPortalException("Error formatting response",sys)