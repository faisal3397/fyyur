import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    response_data = {}

    for category in categories:
      response_data[category.format()["id"]] = category.format()["type"]

    return jsonify({'categories': response_data})
  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def get_questions():
    questions = Question.query.all()
    categories = Category.query.all()
    result_questions = []
    result_categories = {}
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    for category in categories:
      result_categories[category.format()["id"]] = category.format()["type"]

    for question in questions:
      result_questions.append(question.format())

    result_current_category = {}
    current_category = categories[random.randrange(0,6)].format()
    result_current_category[current_category["id"]] = current_category["type"]

    return jsonify({
      'questions': result_questions[start:end],
      'total_questions': len(result_questions),
      'categories': result_categories,
      'current_category': result_current_category
    })
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.get(question_id)
    question.delete()
    return jsonify({'message': 'Question Deleted'})
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():
    question = request.json["question"]
    answer = request.json["answer"]
    category = request.json["category"]# request.json["category"] will be an integer which is the category id 
    difficulty = request.json["difficulty"]

    question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
    question.insert()
    return jsonify({'message': 'Question Created'}), 201
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    result_questions = []
    search_term=request.json["searchTerm"]
    # add %% before and after search term to get all the results that has the search term in their names
    search = "%{}%".format(search_term)
    questions = Question.query.filter(Question.question.ilike(search)).all()
    for question in questions:
      result_questions.append(question.format())

    result_current_category = {}
    categories = Category.query.all()
    current_category = categories[random.randrange(0,6)].format()
    result_current_category[current_category["id"]] = current_category["type"]

    return jsonify({
      "questions": result_questions,
      "totalQuestions": len(result_questions),
      "currentCategory": result_current_category
    })
  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<category_id>/questions')
  def get_questions_by_category(category_id):
    category = Category.query.get(category_id).format()
    questions = Question.query.filter_by(category = category["id"])
    formatted_questions = [question.format() for question in questions]

    return jsonify({
      "questions": formatted_questions,
      "totalQuestions": len(formatted_questions),
      "currentCategory": category["type"]
    })

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    previous_questions = request.json["previous_questions"]
    quiz_category = request.json["quiz_category"]
    print(request.json)

    category = Category.query.get(quiz_category["id"]).format()
    questions = Question.query.filter_by(category = category["id"])
    formatted_questions = [question.format() for question in questions]
    random_question = {}

    for question in formatted_questions:
      if question["id"] not in previous_questions:
        random_question = question


    return jsonify({
      "question": random_question
    })
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    