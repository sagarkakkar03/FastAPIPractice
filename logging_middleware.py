from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        end = time.time()
        print('time',round(end-start))
        print(request.method)
        print(response.status_code)
        return response

app.add_middleware(LogMiddleware)

@app.get('/')
def simple_app():
    return {'message': 'Working'}