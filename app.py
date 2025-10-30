from flask import Flask, render_template, request # type: ignore
import forms, math # type: ignore

app = Flask(__name__)
#Figuras  - - - - -
@app.route('/figuras', methods=['GET','POST'])
def figuras():
    form = forms.FiguraForm(request.form)
    area = ""
    figura = ""
    if request.method=='POST' and form.validate():
        figura = request.form.get('figura')
        num1 = form.num1.data
        num2 = form.num2.data
        if figura == 'triangulo': area = (num1 * num2) / 2
        elif figura == 'rectangulo': area = num1 * num2
        elif figura == 'circulo': area = math.pi * (num1 ** 2)
        elif figura == 'pentagono': area = (5 * num1 * num2) / 2
    return render_template('figuras.html', form=form, area=area, figura=figura)
@app.route('/')
#HOME - - - - -
def home():
    return "Hello, World!"
#INDICE
@app.route('/index')
def index():
    titulo="IEVN-1003 PWA"
    listado=["opera1", "opera2", "opera3", "opera4"]
    return render_template('index.html', titulo=titulo, listado = listado)
#OPERACIONES
@app.route('/operas', methods=['GET', 'POST'])
def operas():
    if request.method == 'POST':
        x1=request.form.get('n1')
        x2=request.form.get('n2')
        resultado = float(x1)+float(x2)
        return render_template('operas.html', resultado=resultado)
    return render_template('operas.html')
#DISTANCIA
@app.route('/distancia')
def distancia():
    return render_template('distancia.html')
#LAYOUT
@app.route('/layout')
def layout():
    return render_template('layout.html')
#AlUMNOS
@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    alumnos_clase=forms.UserForm(request.form)
    if request.method == 'POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.email.data   
    return render_template('alumnos.html', form= alumnos_clase, mat=mat, nom=nom, ape=ape, em=em) 
        

@app.route('/about')
def about():
    return "This is the about page."
 
@app.route('/user/<string:user>')
def user(user):
    return "Hello"+ user
 
@app.route('/number/<int:num>')
def number(num):
    return "Number: {}".format(num)
 
@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "User ID: {} Name: {}".format(id, username)
 
@app.route('/suma/<float:a>/<float:b>')
def func(a, b):
    return "La suma de {}".format(a + b)
 
@app.route('/prueba')
def prueba():
    return '''
        <h1>Prueba de HTML</h1>
        <p>Esta es una prueba de retorno de HTML en Flask.</p>
        <ul>
            <li>Elemento 1</li>
            <li>Elemento 2</li>
            <li>Elemento 3</li>
        </ul>
    '''
# @app.route('/index')
# def index():
#     return '<h1>Welcome to the index page!</h1>'
if __name__ == '__main__':
    app.run(debug=True)