from fastapi import FastAPI
from fastapi import Request, status
from router import resource_get
from exceptions import BadInputParsed, NoResultsException
from fastapi.responses import  JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Callable
from loguru import logger
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND



app = FastAPI(title="Analiza hijerarhije i slicnosti koncepata iz DBpedia baze")
app.include_router(resource_get.router)



@app.exception_handler(BadInputParsed)
async def bad_input_exception_handler(request: Request, exc: BadInputParsed):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"detail": exc.detail},
    )

@app.exception_handler(NoResultsException)
async def no_results_found_exception_handler(request: Request, exc: NoResultsException):
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content={"detail": exc.detail},
    )

# def create_exception_handler(
#         status_code: int, initial_detail: str
#     ) -> Callable[[Request, StoryException], JSONResponse]:
#     detail = {"message": initial_detail}

#     async def exception_handler(_: Request, exc: StoryException) -> JSONResponse:
#         if exc.message:
#             detail["message"] = exc.message
        
#         if exc.name:
#             detail["message"] = f"{detail['message']} [{exc.name}]"

#         logger.error(exc)
#         return JSONResponse (
#             status_code=status_code, content={"detail": detail["messages"]}
#         )
#     return exception_handler


# app.add_exception_handler(
#     exc_class_or_status_code=TypeError,
#     handler=create_exception_handler(
#         status.HTTP_400_BAD_REQUEST, "Data can't be processed, check the input."
#     )
# )

# @app.middleware('http')
# async def add_middleware(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     duration = time.time() - start_time
    
#     response.headers['duration'] = str(duration) #dodajem headers samom responsu
#     return response


# hosts = ['http://localhost:3000']

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = hosts,
#     allow_credentials = True,
#     allow_methods = ["*"],
#     allow_headers = ["*"]
# )

# url = "https://dbpedia.org/sparql"

# @app.get("/")
# async def root():
#     page = requests.get(url)
#     return {"page", page.status_code}