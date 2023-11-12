from app import create_app
from src.sockets.user.socketio_events import socketio


from src.database.db_pg import db
from src.models.seeds import create_seed

app = create_app()

with app.app_context():
    db.create_all()
    create_seed()

print("Server running on port 5000")

if __name__ == "__main__":
    # app.run(debug=False, port=5000, host="0.0.0.0")
    socketio.init_app(app)
    socketio.run(app, debug=True, port=5000, host="0.0.0.0")
