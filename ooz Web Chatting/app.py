from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = '123'

#chat server
socketio = SocketIO(app)
@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    #send message to everyone in server
    send(msg, broadcast=True)

@app.route('/chat')
def chat():
    return render_template('chatroom.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # add to the db when there's input in the fields and the passwords match 
        # when conditions are not met, stay on the signin page
        if (password == "TVTVX" and username == "oozAdmin"):
            return render_template("chatroom.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    
if __name__ == "__main__":
    socketio.run(app)