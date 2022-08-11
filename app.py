
from asyncio import tasks
from datetime import datetime

from flask import Flask ,render_template ,request,redirect
from flask_sqlalchemy import SQLAlchemy


app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complate = db.Column(db.String(200))
    # date_created = db.Column(db.DateTime, defualt=datetime.utcnow)


    def __repr__(self) -> str:
        return '<Task %r' %self.id


@app.route('/',methods=['POST'  ,'GET'])
def index():
    if request.method == 'POST':
        new_task =request.form['content']
        new_task_inatsnce = Todo(content = new_task)
        try:
            db.session.add(new_task_inatsnce)
            db.session.commit()
            return redirect('/')
        except:
            print("somting wronge")
        print((f"all reserverd {new_task}"))
        return(f"all reserverd {new_task}")
    else:
        tasks = Todo.query.all()
        # print(tasks)      
        return  render_template('index.html' , tasks =tasks)





if (__name__ == "__main__"):
    app.run( port=5500, debug=True)