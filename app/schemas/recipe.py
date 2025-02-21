from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    description: str
    ingredients: str

class RecipeCreate(RecipeBase):
    pass

class RecipeResponse(RecipeBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
