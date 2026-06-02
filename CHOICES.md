# Design Choices & Trade-offs

1. **FastAPI over Flask:** Chosen for its native asynchronous capabilities and automatic Swagger UI generation, which simplifies API testing.

2. **Middleware Logging:** Implemented a custom log_request_middleware to ensure detailed request tracking (latency, status, path) without external heavy dependencies.

3. **SQLite:** Chosen for the prototype phase due to zero-configuration requirements, making it portable and easy to verify for judges.
