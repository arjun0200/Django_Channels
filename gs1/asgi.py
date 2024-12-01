import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack  # Import the authentication middleware stack
import app.routing  # Assuming 'app' is your app name containing routing.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs1.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(  # Wrap WebSocket routing with AuthMiddlewareStack
        URLRouter(
            app.routing.websocket_urlpatterns  # WebSocket URL routing
        )
    ),
})


###ws://127.0.0.1:8000/ws/sc/