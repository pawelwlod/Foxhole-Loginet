# middleware.py
'''Middleware Manager for Loginet'''

import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.logger = logging.getLogger("http_middleware")
    
    async def dispatch(self, request, call_next):
        start = time.time()
        self.logger.info(f"HTTP {request.method} {request.url.path} - started")

        try:
            response = await call_next(request)
        except Exception as exc:
            self.logger.exception(f"Unhandled error during request: {exc}")
            raise

        duration = (time.time() - start) * 1000
        self.logger.info(
            f"HTTP {request.method} {request.url.path} "
            f"completed with {response.status_code} in {duration:.2f}ms"
        )

        return response


class WebSocketLoggingMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app
        self.logger = logging.getLogger("middleware.websocket")

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "websocket":
            return await self.app(scope, receive, send)

        path = scope.get("path")
        self.logger.info(f"WebSocket connect: {path}")

        try:
            await self.app(scope, receive, send)
        except Exception as exc:
            self.logger.exception(f"WebSocket error on {path}: {exc}")
            raise
        finally:
            self.logger.info(f"WebSocket disconnect: {path}")
