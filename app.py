
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

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f' there is error need to be fixed {e}')
        return redirect('/')

    return f'item deleeted is {id}  task is {task_to_delete.content}'

@app.route('/Update/<int:id>',methods=['POST'  ,'GET'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_update.content = request.form['content']
        db.session.commit()
        return redirect('/')
    else :
       
        return render_template('update.html' , task = task_to_update)









if (__name__ == "__main__"):
    app.run( port=5500, debug=True)