import time
from datetime import datetime
from fastapi import Request


async def log_request_middleware(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(
        f"{timestamp} - retail_api - INFO - "
        f"{request.method} {request.url.path} "
        f"{response.status_code} - {process_time:.4f}s",
        flush=True
    )

    return response