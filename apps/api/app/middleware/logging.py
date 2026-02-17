import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = str(uuid.uuid4())
        start = time.perf_counter()
        response = await call_next(request)
        response.headers['X-Request-ID'] = request_id
        response.headers['X-Latency-MS'] = f"{(time.perf_counter() - start)*1000:.2f}"
        return response
