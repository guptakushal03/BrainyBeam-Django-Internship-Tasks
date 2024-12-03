from django.shortcuts import render
from .models import Question, Option
from .forms import QuizForm

def quiz_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            correct = 0
            incorrect = 0
            for question in questions:
                selected_option_ids = form.cleaned_data.get(f'question_{question.id}')
                
                if selected_option_ids:
                    selected_options = Option.objects.filter(id__in=selected_option_ids)

                    correct_options = selected_options.filter(is_correct=True)
                    incorrect_options = selected_options.filter(is_correct=False)

                    correct += correct_options.count()
                    incorrect += incorrect_options.count()

            return render(request, 'Quiz/quiz_result.html', {'correct': correct, 'incorrect': incorrect})
    else:
        form = QuizForm(questions=questions)
    return render(request, 'Quiz/quiz.html', {'form': form})

# Super User: kushalgupta; KG