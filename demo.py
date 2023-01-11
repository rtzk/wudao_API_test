from flask import Flask, render_template, request
from  wudo import Submitwudao

app = Flask(__name__)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        prompt=request.form['prompt']
        print({"prompt:",prompt})
        if prompt is not "":
            outputText=Submitwudao(prompt)
            values={"textarea":outputText,"prompt":prompt}
            return render_template('index.html',**values)
    return render_template('index.html')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         question = request.form.get('prompt')
#         print(question)

#         return '执行成功'
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080)