from fastapi import FastAPI
from typing import List
from fastapi_pagination import Page, paginate,limit_offset,set_page

app = FastApi()

l= [{"id":1 "name":f"item{i}"} for i in range(1,101)]

@app.get("/item",response_model=list[dict])
async def get_items(limit_offset:)


