from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('home.html', title='Home', h1='Home')

@app.route('/lista')
def lista():
    lista = ['Bibliotecas Python', 'Tópicos Especiais em Gestão', 'Inicio do tema(liderança)']
    return render_template('list.html',
                           title='8459210',
                           h1='Desenvolvimento de Sistemas com Python',
                           lista=lista)


if __name__ == '__main__':
    app.run(debug=True)