from pydantic import BaseModel, Field, RootModel
from typing import Optional, List, Dict, Any, Union

class Metadata(BaseModel):
    """
    Represents metadata for a document.
    """
    Summary: List[str] = Field(default_factory=list, description="Summary of the document")
    Title: str
    Author: str
    DateCreated: str   
    LastModifiedDate: str
    Publisher: str
    Language: str
    PageCount: Union[int, str]  # Can be "Not Available"
    SentimentTone: str
    
class ChangeFormat(BaseModel):
    """
    Represents a change in format for a document.
    """
    Page: str
    Changes: str
    
class SummaryResponse(BaseModel[list[ChangeFormat]]):
    """
    Represents a response containing a list of changes in format.
    """
    pass