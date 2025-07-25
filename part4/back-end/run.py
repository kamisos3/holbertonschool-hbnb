from app import create_app

app = create_app()

with app.app_context():
    from app import db
    db.drop_all()
    db.create_all()
    print("Database tables recreated successfully!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
