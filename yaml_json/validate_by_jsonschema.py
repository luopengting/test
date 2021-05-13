# 导入验证器
from jsonschema import validate

# 编写schema：
my_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "TestInfo",
    "description": "some information about test",
    "type": "object",
    "properties": {
        "name": {
            "description": "Name of the test",
            "type": "string"
        },
        "age": {
            "description": "age of test",
            "type": "integer"
        }
    },
    "required": [
        "name", "age"
    ]
}

# json数据：
json_data = {
    "name": "python",
    "age": 25
}

# 验证：
validate(instance=json_data, schema=my_schema)

from marshmallow import Schema, fields, validates


class UserSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "name字段必须填写"})
    email = fields.Email()
    created_time = fields.DateTime()


user = {"name": "tty", "email": "tty@python"}
schema = UserSchema()
res = schema.load(user)
print(res)
# {'email': ['Not a valid email address.']}

user1 = {"name": "tty", "email": "tty@python.org"}
schema = UserSchema()
res1 = schema.validate(user1)
print(res1)
# {}
