import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # host='0.0.0.0' allows access from other devices on same network
    # Bind port from environment when provided (Render sets $PORT)
    port = int(os.environ.get('PORT', 5000))
    debug = app.config.get('DEBUG', False)
    app.run(host='0.0.0.0', port=port, debug=debug)
