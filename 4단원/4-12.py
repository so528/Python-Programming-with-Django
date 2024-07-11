from polls.models import Question, Choice

Question.objects.all()

[<Question: What is your hobby?>, <Question: Who do you like best?>, <Question: Where do you live?>

Choice.objects.all()

 <QuerySet [<Choice: Reading>, <Choice: Soccer>, <Choice: Climbing>, <Choice: Seoul>, <Choice: Daejeon>, <Choice: Jeju>]>

 from django.utils import timezone

 q = Question(question_text = "What's up?", pub_date = timezone.now())
>>> q.save()
>>> q.id

 q.question_text
"What's up?"
>>> q.pub_date
datetime.datetime(2024, 7, 11, 7, 38, 14, 125213, tzinfo=datetime.timezone.utc)
>>> Question.objects.all()
<QuerySet [<Question: What is your hobby?>, <Question: Who do you like best?>, <Question: Where do you live?>, <Question: What's up?>]>
>>> exit()
