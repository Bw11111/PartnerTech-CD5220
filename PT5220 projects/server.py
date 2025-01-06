from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')





@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form['message']
        os.system("C:\\Users\\Minec\\source\\repos\\SendData\\x64\\Debug\\SendData.exe COM3 " + "9"+message)
    
        return redirect(url_for('home'))
    return render_template('contact.html')
@app.route('/banner', methods=['GET', 'POST'])
def banner():
    if request.method == 'POST':
        message = request.form['message']
        os.system("C:\\Users\\Minec\\source\\repos\\SendData\\x64\\Debug\\SendData.exe COM3 " + "6"+message)
    
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/raw', methods=['GET', 'POST'])
def raw():
    if request.method == 'POST':
        message = request.form['message']
        os.system("C:\\Users\\Minec\\source\\repos\\SendData\\x64\\Debug\\SendData.exe COM3 "+message)
    
        return redirect(url_for('home'))
    return render_template('contact.html')   
@app.route("/clr")
def clr():
    os.system("python clr.py")
    return redirect(url_for("home"))
if __name__ == '__main__':
    app.run(debug=True)
