import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# 連線資訊: host='localhost
# 資料庫: pydb
# 使用者: root
# 密碼: Dev127336
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Dev127336@localhost/pydb'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), unique=True)
    UC = db.Column(db.String(120))
    UN = db.Column(db.String(120))
    FC = db.Column(db.String(120))

    def __init__(self, id, password, UC, UN, FC):
        self.id = id
        self.password = password
        self.UC = UC
        self.UN = UN
        self.FC = FC

class testSchema(ma.Schema):
    class Meta:
        fields = ('id', 'password', 'UC', 'UN', 'FC')

test_schema = testSchema()
tests_schema = testSchema(many=True)

@app.route('/test', methods=['POST'])
def add_test():
    id = request.json['id']
    password = request.json['password']
    UC = request.json['UC']
    UN = request.json['UN']
    FC = request.json['FC']

    new_test = test(id, password, UC, UN, FC)

    db.session.add(new_test)
    db.session.commit()

    return test_schema.jsonify(new_test)

@app.route('/test', methods=['GET'])
def get_tests():
    all_tests = test.query.all()
    result = tests_schema.dump(all_tests)
    return jsonify(result)

@app.route('/test/<id>', methods=['GET'])
def get_test(id):
    test = test.query.get(id)
    return test_schema.jsonify(test)

@app.route('/test/<id>', methods=['PUT'])
def update_test(id):
    test = test.query.get(id)

    id = request.json['id']
    password = request.json['password']
    UC = request.json['UC']
    UN = request.json['UN']
    FC = request.json['FC']

    test.id = id
    test.password = password
    test.UC = UC
    test.UN = UN
    test.FC = FC

    db.session.commit()

    return test_schema.jsonify(test)

@app.route('/test/<id>', methods=['DELETE'])
def delete_test(id):
    test = test.query.get(id)
    db.session.delete(test)
    db.session.commit()

    return test_schema.jsonify(test)

if __name__ == '__main__':
    app.run(debug=True)

