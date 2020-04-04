from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dborder


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('main.html')


## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def order_post():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    count = request.form['count']

    order = {
        'name': name,
        'address': address,
        'phone': phone,
        'count': count
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success'})


@app.route('/order', methods=['GET'])
def order_get():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=500, debug=True)
