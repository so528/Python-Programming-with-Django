Microsoft Windows [Version 10.0.19045.4529]
(c) Microsoft Corporation. All rights reserved.

C:\Users\소현우>cd C:\Users\소현우\Desktop\

C:\Users\소현우\Desktop>
C:\Users\소현우\Desktop>cd project\project

C:\Users\소현우\Desktop\project\project>python manage.py shell
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls .models import Question, Choice
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What is your hobby?>]>
>>> Question.objects.filter(question_text__startswith = 'What')
<QuerySet [<Question: What is your hobby?>, <Question: What's up?>]>

>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.filter(pub_date__year = current_year)
<QuerySet [<Question: What is your hobby?>, <Question: Who do you like best?>, <Question: Where do you live?>, <Question: What's up?>]>

>>> Question.objects.filter(pk=1)
<QuerySet [<Question: What is your hobby?>]>

           
>>> q = Question.objects.get(pk=2)
>>> q.choice_set.all()
<QuerySet []>

q.choice_set.create(choice_text = 'King sejong', votes = 0)
<Choice: King sejong>

 q.choice_set.create(choice_text = 'President Lincoln', votes = 0)
<Choice: President Lincoln>

>>> c = q.choice_set.create(choice_text = 'my mother', votes = 0)
>>> c.question
<Question: Who do you like best?>

q.choice_set.all()
<QuerySet [<Choice: King sejong>, <Choice: President Lincoln>, <Choice: my mother>]>


>>> q.choice_set.count()
3

>>> Choice.objects.filter(question__pub_date__year = current_year)
<QuerySet [<Choice: Reading>, <Choice: Soccer>, <Choice: Climbing>, <Choice: Seoul>, <Choice: Daejeon>, <Choice: Jeju>, <Choice: King sejong>, <Choice: President Lincoln>, <Choice: my mother>]>


>>> c = q.choice_set.filter(choice_text__startswith='Sleeping')
>>> c.delete()
(0, {})
