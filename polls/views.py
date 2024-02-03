from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
from bson import ObjectId

client = MongoClient(os.getenv('MONGO_URI'))
db = client['mysite']
question = db.polls_question
print('all collections', db.list_collection_names())
# db.polls_question.insert_one({
#     'question_text': 'What is your favorite color?',
#     'pub_date': datetime.now()
# })
print('----Availiable Questions----')
all_questions = db.polls_question.find()
q_num = 1
for q in all_questions:
    print('Question number '+str(q_num)+': '+q['question_text']+' (Published on: '+str(q['pub_date'])+')')
    q_num += 1
print('')

new_q = {"question_text": "What's new?", "pub_date": datetime.now()}

does_new_q_exist_in_db = False

for q in db.polls_question.find():
    if q['question_text'] == new_q['question_text']:
        does_new_q_exist_in_db = True
        break
if not does_new_q_exist_in_db:
    db.polls_question.insert_one(new_q)
    print('New question added to the database!')
else:
    print('Question already exists in the database!')
print('')

# Create your views here.
# views = routes
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")