from polls.models import Choice, Question
# 위의 내용 동일

# logging 추가
import logging
logger = logging.getLogger(__name__)

# 중간 내용 생략

def vote(request, question_id):
    logger.debug(f"vote().question_id: {question_id}")  # 추가
    question = get_object_or_404(Question, pk=question_id)

# 아래 내용 동일
