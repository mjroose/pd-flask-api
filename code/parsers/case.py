from flask_restful import reqparse

case_parser = reqparse.RequestParser()
case_parser.add_argument('number',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
case_parser.add_argument('client_id',
    type=int,
    required=True,
    help="Fields cannot be left blank!"
)
case_parser.add_argument('attorney_ids',
    type=int,
    action='append',
    required=True,
    help="A case must be assigned to an attorney."
)
