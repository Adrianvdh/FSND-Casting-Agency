from .app import create_app
from .models import db

app = create_app()


# Default port:
if __name__ == '__main__':
    app.run()
