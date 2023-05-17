from pydantic import BaseModel, parse_obj_as


class Category(BaseModel):
    id: int
    title: str
    slug: str


# return_json
# returnJson

