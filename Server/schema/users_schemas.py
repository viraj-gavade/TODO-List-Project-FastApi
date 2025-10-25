from pydantic import BaseModel ,Field ,EmailStr
from typing import Annotated ,List,Optional
from schema.tasks_shemas import taskSchema


class UserSchema(BaseModel):
    id: Annotated[

        Optional
        [int],
        Field(description="ID of the user", examples=[1, 2, 3, 4, 5],default=None)
    ]

    username: Annotated[
        str,
        Field(
            description="Username of the user",
            max_length=24,
            min_length=4,
            pattern=r'^[a-zA-Z0-9_]+$',
            examples=["viraj_gavade"]
        )
    ]

    password: Annotated[
        str,
        Field(
            description="Password of the user",
            max_length=24,
            min_length=8,
            pattern=r"^[A-Za-z0-9]{8,}$",
            examples=["Viraj123"]
        )
    ]

    email: Annotated[
        EmailStr,
        Field(description="Email of the user", examples=["demouser@gmail.com"])
    ]

    tasks: List[taskSchema] = Field(default_factory=list, description="List of tasks created by the user")

    model_config = {
        "from_attributes": True
    }



class SinUpSchema(BaseModel):

    id: Annotated[Optional
        [int],
        Field(description="ID of the user", examples=[1, 2, 3, 4, 5],default=None)
    ]

    username: Annotated[
        str,
        Field(
            description="Username of the user",
            max_length=24,
            min_length=4,
            pattern=r'^[a-zA-Z0-9_]+$',
            examples=["viraj_gavade"]
        )
    ]

    password: Annotated[
        str,
        Field(
            description="Password of the user",
            max_length=24,
            min_length=8,
            pattern=r"^[A-Za-z0-9]{8,}$",
            examples=["Viraj123"]
        )
    ]

    email: Annotated[
        EmailStr,
        Field(description="Email of the user", examples=["demouser@gmail.com"])
    ]

    model_config = {
        "from_attributes": True
    }



class SingInSchema(BaseModel):

    id: Annotated[Optional
        [int],
        Field(description="ID of the user", examples=[1, 2, 3, 4, 5],default=None)
    ]

    username: Annotated[
        str,
        Field(
            description="Username of the user",
            max_length=24,
            min_length=4,
            pattern=r'^[a-zA-Z0-9_]+$',
            examples=["viraj_gavade"]
        )
    ]

    password: Annotated[
        str,
        Field(
            description="Password of the user",
            max_length=24,
            min_length=8,
            pattern=r"^[A-Za-z0-9]{8,}$",
            examples=["Viraj123"]
        )
    ]


    model_config = {
        "from_attributes": True
    }

