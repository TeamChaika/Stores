from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse

import uvicorn
from scripts import stores, products, products_balance
import json

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/stores/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="stores.html", context={'stores': stores()}
    )


@app.get("/store/{id}", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="store.html", context={'products': stores()}
    )


@app.get("/product/{product_id}/{product_name}", response_class=HTMLResponse)
async def read_item(request: Request, product_id:str, product_name:str):

    return templates.TemplateResponse(
        request=request, name="product.html", context={'pruduct': products_balance(product_id), 'product_name':product_name, 'options': products()}
    )


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="products.html", context={'products': products()}
    )


#if __name__ == "__main__":
#    uvicorn.run(app, port=8011)
