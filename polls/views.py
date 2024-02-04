from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, timedelta
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
from bson import ObjectId


# Create your views here.
# views = routes
def index(request):


    
# client = MongoClient(os.getenv('MONGO_URI'))
# db = client['mysite']
# question = db.polls_question
# print('all collections', db.list_collection_names())
# # db.polls_question.insert_one({
# #     'question_text': 'What is your favorite color?',
# #     'pub_date': datetime.now()
# # })
# print('----Availiable Questions----')
# all_questions = db.polls_question.find()
# q_num = 1
# for q in all_questions:
#     print('Question number '+str(q_num)+': '+q['question_text']+' (Published on: '+str(q['pub_date'])+')')
#     q_num += 1
# print('')

# new_q = {"question_text": "What's new?", "pub_date": datetime.now()}

# does_new_q_exist_in_db = False

# for q in db.polls_question.find():
#     if q['question_text'] == new_q['question_text']:
#         does_new_q_exist_in_db = True
#         break
# if not does_new_q_exist_in_db:
#     db.polls_question.insert_one(new_q)
#     print('New question added to the database!')
# else:
#     print('Question already exists in the database!')
# print('')

# # TODO search by question_text
# qtext_s = question.find_one({ 'question_text' : "What's new?" })
# print('Search by question_text= '+ qtext_s['question_text']+ '(published on: ' +str(qtext_s['pub_date'])+ ')' )
# # TODO Search a question by a certain text
# specific_question = (
#     db.polls_question.find_one({"question_text": {"$regex": "what", "$options": "i"}}),
# )
# print('specific search'+ specific_question[0]['question_text']+ 'published: '+  specific_question[0]['pub_date'])
# # TODO Search all questions by one date
# target_date = datetime(2024, 2, 3)
# found_questions = question.find(
#     {"pub_date": {"$gte": target_date, "$lt": target_date + timedelta(days=1)}}
# )

# # Print or iterate over the found questions
# print("----Find questions with the specified date-----")
# for question in found_questions:
#     print(question)
# # search_date = { 'pub_date': datetime.now() }
# # result = question.find(search_date).sort("pub_date", -1) # sort by pub_date in descending order
# # for q in result:
# #     print('date result', q['question_text'], 'published: ', str(q['pub_date']))
# # TODO Update a question (pub_date -> needs to be set to current date)
# update_data = {
#     "$set": {
#         "question_text": "How are you today?",
#         "pub_date": datetime.now()
#         }
# }
# update_s_data = { '_id':ObjectId('65bea3a2d2cecb793c0a1b0e') }
# db.polls_question.find_one_and_update(update_s_data, update_data)
# update_result = db.polls_question.find_one(update_s_data)
# print('Updated Question= '+ update_result['question_text']+ '(updated on: ' +str(update_result['pub_date'])+ ')' )

# # TODO Delete a question
# # 

    return HttpResponse("Hello, world. You're at the polls index.")