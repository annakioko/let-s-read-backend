from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from dotenv import load_dotenv
import os

from models import db, Product, Category, User, Order, OrderItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
load_dotenv()
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')


migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})


#class LogIn(Resource):
   # def post(self):
      #  data = request.get_json()
       # if not data:
        #    return {"error": "Missing data in request"}, 400

       # username = data.get('username')
       # password = data.get('password')
        
      #  user = User.query.filter_by(username=username).first()
        
       # if not user:
        #  return {"error": "User does not exist"}, 401
      #  if not bcrypt.check_password_hash(user.password, password):
       #    return {"error": "Incorrect password"}, 401
        
      #  access_token = create_access_token(identity={'id': username.id, 'role': username.role})
       # refresh_token = create_refresh_token(identity={'id': username.id, 'role': username.role})
      #  return {"access_token": access_token, "refresh_token": refresh_token}, 200

#api.add_resource(LogIn, '/login')

#class TokenRefresh(Resource):
   # @jwt_required(refresh=True)
   # def post(self):
       # try:
      #      current_user = get_jwt_identity()
       #     access_token = create_access_token(identity=current_user)
        #    return {'access_token': access_token}, 200
        #except Exception as e:
          #  return jsonify(error=str(e)), 500

#api.add_resource(TokenRefresh, '/refresh-token')

#User routes
class UserResource(Resource):
    def get(self):
       users = [user.serialize() for user in User.query.all()]
       return make_response(users, 200)
    
    #def patch they should be able to edit their passwords and addresses and emails
    
api.add_resource(UserResource, '/user')



#Product Routes
#post route should be added but this is after the Jwt is added
class ProductResource(Resource):
    def get(self):
        products = [product.serialize() for product in Product.query.all()]
        return make_response(products, 200)
    
api.add_resource(ProductResource, '/product')

#Product by name
class ProductByName(Resource):
    def get(self, name):
        product = Product.query.filter_by(name=name).first()
        if product is None:
            return{"error": "Product not found"}, 404
        response_dict = product.serialize()
        return make_response(response_dict, 200)
    
api.add_resource(ProductByName, '/product/<string:name>')



#product by category
class ProductByCategory(Resource):
    def get(self, category):
        product = Product.query.filter_by(category_name=category).all()
        if product is None:
            return{"error": "Product not found"}, 404
        response_dict = product.serialize()
        return make_response(response_dict, 200)
    
api.add_resource(ProductByCategory, '/product/<string:category>')
    
    

#product by id will mostly be used by the admin
#patch a 
class ProductById(Resource):
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if product is None:
            return{"error": "Product not found"}, 404
        response_dict = product.serialize()
        return make_response(response_dict, 200)
    
  
    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        if product is None:
            return{"error": "Product not found"}, 404
        
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product delete successfully'})
    

     

    
api.add_resource(ProductById, '/products/<int:id>')


#Category routes
class CategoryResource(Resource):
    def get(self):
        categories = [category.serialize() for category in Category.query.all()]
        return make_response(categories, 200)
    
    
    
api.add_resource(CategoryResource, '/category')
    

#category by name
class CategoryByName(Resource):
    def get(self, name):
        category = Category.query.filter_by(name=name).first()
        if category is None:
            return{"error": "Product not found"}, 404
        response_dict = category.serialize()
        return make_response(response_dict, 200)
        
    
api.add_resource(CategoryByName, '/categories/<string:name>')


class OrderResource(Resource):
    def get(self):
        orders = [order.serialize() for order in Order.query.all()]
        return make_response(orders, 200)
    
api.add_resource(OrderResource, '/orders')


class OrderById(Resource):
    def get(self, id):
        order = Order.query.filter_by(id=id).first()
        if order is None:
            return{"error": "order not found"}, 404
        response_dict = order.serialize()
        return make_response(response_dict, 200)
    
api.add_resource(OrderById, '/order/<int:id>')

# this is for the add to cart
class OrderItem(Resource):
    def post(self):
        pass


api.add_resource(OrderItem, '/orderitem')


#put route by id is for increasing and decreasing quantity
class OrderItemById(Resource):
    def patch(self, id):
        pass



    #delete is the remove from cart
    def delete(self, id):
        pass


api.add_resource(OrderItemById, '/orderitem/<int:id>')


