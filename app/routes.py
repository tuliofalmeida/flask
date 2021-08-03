import numpy as np
from app import app
from flask.templating import render_template
from app.forms import LoginForm
# from bokeh.plotting import figure
# from bokeh.resources import CDN
# from bokeh.embed import file_html,components

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Túlio'}
    data = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
    post = [
        {
            'author': {'username':'Tião'},
            'body': 'Belo dia em Macaíba.'
        },
        {
            'author': {'username':'Tia do pastel'},
            'body': 'Macaíba é bom demais.'
        },
        {
            'author': {'username':'Mito'},
            'body': 'Gosto demais de Macaíba.'
        }
    ]
    
    # plot = figure(title='Teste')
    # tempo = np.arange(0, 10, 0.1)
    # sinal = np.sin(tempo)
    # plot.line(tempo, sinal)
    # html = file_html(plot, CDN, "my plot")
    # div = components(plot)
    
    return render_template('pagina.html', title='Home',post=post,
                           data=data,user=user)
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)
    
