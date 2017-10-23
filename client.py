from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from clientModel import clientModel

class GetClient(Resource):

    def get(self,id):

        client = clientModel.find_by_id(id)
        if client:
            return client.json()
        return {'message': 'Client does not exist.'}, 404


class ModifyClient(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True)
    parser.add_argument('name', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('phone', type=str)
    parser.add_argument('address', type=str)
    parser.add_argument('city', type=str)
    parser.add_argument('postalcode', type=str)
    parser.add_argument('country', type=str)

    # have to authenticate before calling POST
    @jwt_required()
    def post(self):

        data = ModifyClient.parser.parse_args()

        if clientModel.find_by_id(data['id']):
            return {'message': "A client with id '{}' already exists.".format(data['id'])}, 400


        client= clientModel(data['id'], data['name'], data['email'],  data['phone'], \
                data['address'],  data['city'],  data['postalcode'],  data['country'])

        try:
            client.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return clientModel.json(), 201

    # have to authenticate before calling DELETE
    @jwt_required()
    def delete(self):

        data = ModifyClient.parser.parse_args()

        client = clientModel.find_by_id(data['id'])
        if client:
            client.delete_from_db()

        return {'message': 'Client has been deleted successfully!'}

    # have to authenticate before calling PUT
    @jwt_required()
    def put(self):

        data = ModifyClient.parser.parse_args()
        client = clientModel.find_by_id(data['id'])
        if client:
            client.name = data['name']
            client.phone = data['phone']
            client.email = data['email']
            client.address = data['address']
            client.city = data['city']
            client.postalcode = data['postalcode']
            client.country = data['country']
        else:
            client = clientModel(data['id'], data['name'], data['email'], data['phone'], data['address'], \
                                 data['city'], data['postalcode'], data['country'])

        client.save_to_db()
        return client.json()


class ClientList(Resource):

    def get(self):
        # apply this lambda function to rach element in the query result list
        return {'clients': list(map(lambda x: x.json(), clientModel.query.all()))}
