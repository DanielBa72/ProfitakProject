from workproject import app
from workproject import db


with app.app_context(): 
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)