from pydantic import BaseModel ,Field
from typing import Optional , Annotated 
from datetime import date


class taskSchema(BaseModel):
    id : Annotated[Optional[int],Field(description='Id of the Task',examples=[1,2,3],default=None)]
    name : Annotated[str,Field(description='name of the Task',examples=['Cook Food'])]
    description : Annotated[str,Field(description='description of the Task',examples=['Cook Food for the dinner tonight'])]
    isDone : Annotated[Optional[bool],Field(description='Is task completed',examples=['Cook Food'],default=False)]
    date: Annotated[Optional[date], Field(description="Date of the Task", examples=["2025-10-23"], default_factory=date.today)]
    
    model_config = {
        "from_attributes": True 
    }
    



class UpdateTaskSchema(BaseModel):
    name : Annotated[Optional[str],Field(description='name of the Task',examples=['Cook Food'],default=None)]
    description : Annotated[Optional[str],Field(description='description of the Task',examples=['Cook Food for the dinner tonight'],default=None)]
    isDone : Annotated[Optional[bool],Field(description='Is task completed',examples=['Cook Food'],default=False)]
    date: Annotated[Optional[date], Field(description="Date of the Task", examples=["2025-10-23"], default_factory=date.today)]

    class Config:
        model_config = {
        "from_attributes": True  
    }
        

