from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Choice, Question
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import os
from dotenv import load_dotenv
load_dotenv()


# imports for authentication
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import  User
from django.contrib.auth import  login , logout, authenticate
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import  method_decorator

recipientAddress = os.getenv('SMTP_EMAIL')
# Create your views here.
# views = routes
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = { "latest_question_list": latest_question_list }
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
def send_message(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"{form.cleaned_data['name']} sent you a message!"
            message = f"Name: {form.cleaned_data['name']}\n\nSubject: {form.cleaned_data['subject']}\n\nSender: {form.cleaned_data['sender']}\n\nMessage:\n{form.cleaned_data['message']}"
            sender = form.cleaned_data['sender']
            send_mail(
                subject, #title
                message,
                sender,
                [recipientAddress],
                fail_silently=False,
            )
            form = ContactForm()
            return HttpResponseRedirect('/polls')
        else:
            form = ContactForm()
            return render(request, "polls/contact.html", { 'form': form })
    else:
        form = ContactForm()
        return render(request, "polls/contact.html", {"form" : form }) 
        #create a form instance and populate it with the data from the request:
        # form = ContactForm(request.post)
    #     if form.is_valid():
    #         #process the data in the form.cleaned_data as required
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         sender = form.cleaned_data['sender']
    #         cc_myself = form.cleaned_data['cc_myself']

    #         recipients = [recipientAddress]
    #         if cc_myself:
    #             recipients.append(sender)
            
    #         send_mail(subject, message, sender, recipients)
    #         # redirect to a new url
    #         return HttpResponseRedirect('/thanks/')
    # else:
    #     form = ContactForm()

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv
# load_dotenv()
# from bson import ObjectId

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

