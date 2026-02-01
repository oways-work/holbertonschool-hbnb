from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

# Define the review model for output
review_output_model = api.model('ReviewOutput', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user'),
    'place_id': fields.String(description='ID of the place'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'updated_at': fields.DateTime(description='Update timestamp')
})

@api.route('/')
class ReviewList(Resource):
    @api.doc('create_review')
    @api.expect(review_model)
    @api.marshal_with(review_output_model, code=201)
    def post(self):
        """Register a new review"""
        review_data = api.payload
        
        # 1. Verify User exists
        user = facade.get_user(review_data['user_id'])
        if not user:
            api.abort(400, "User not found")
            
        # 2. Verify Place exists
        place = facade.get_place(review_data['place_id'])
        if not place:
            api.abort(400, "Place not found")

        # 3. Create Review
        try:
            new_review = facade.create_review(review_data)
        except ValueError as e:
            # Catch validation errors (like rating > 5)
            api.abort(400, str(e))
            
        return new_review, 201

    @api.doc('list_reviews')
    @api.marshal_list_with(review_output_model)
    def get(self):
        """List all reviews"""
        return facade.get_all_reviews()

@api.route('/<review_id>')
@api.param('review_id', 'The Review identifier')
@api.response(404, 'Review not found')
class ReviewResource(Resource):
    @api.doc('get_review')
    @api.marshal_with(review_output_model)
    def get(self, review_id):
        """Fetch a review given its identifier"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
        return review

    @api.doc('update_review')
    @api.expect(review_model)
    @api.marshal_with(review_output_model)
    def put(self, review_id):
        """Update a review given its identifier"""
        review_data = api.payload
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")

        updated_review = facade.update_review(review_id, review_data)
        return updated_review

    @api.doc('delete_review')
    @api.response(204, 'Review deleted')
    def delete(self, review_id):
        """Delete a review given its identifier"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
            
        facade.delete_review(review_id)
        return '', 204
