from flask import Flask, request, render_template,jsonify
import numpy as np

app = Flask(__name__)
# def string_join(text1,text2):
#    text1 = text1.upper()
#    text2 = text2.upper()
#    combine = text1 +text2
#    return combine

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/join', methods=['GET','POST'])
# def my_form_post():
#     text1 = request.form['text1']
#     word = request.args.get('text1')
#     text2 = request.form['text2']
#     combine = string_join(text1,text2)
#     result = {
#         "output": combine
#     }
#     result = {str(key): value for key, value in result.items()}
#     return jsonify(result=result)


@app.route('/')
def matrix():
    return render_template('inv.html')

@app.route('/', methods = ['POST'])
def matrix_inverse():
    text = request.form['mat']
    list = text.split()
    sz = int(np.sqrt(len(list)))
    
    b = [int(z) for z in list]
    a = np.reshape(np.array(b), (sz, sz))

    inva = np.linalg.inv(a)
    # print(inva)

    processed_text = ''

    for x in inva:
        processed_text += str(x)
        processed_text += ' '

    return processed_text
    


if __name__ == '__main__':
    app.run()