from typing import List, Optional
from pydantic import BaseModel


class PostSubmission(BaseModel):
    id:int
    epoch_second:int
    problem_id:str
    contest_id:str
    user_id:str
    language:str
    point:str
    length:int
    result:str
    execution_time:int