from django.shortcuts import render
from .models import Subject, Course, School, User
from .forms import SubjectForm
# Create your views here.
def recommend_courses(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject1 = form.cleaned_data['subject1']
            subject2 = form.cleaned_data['subject2']
            subject3 = form.cleaned_data['subject3']
            subject4 = form.cleaned_data['subject4']
            subject5 = form.cleaned_data['subject5']
            subject6 = form.cleaned_data['subject6']

            # Get the subjects chosen by the user
            subjects = [subject1, subject2, subject3, subject4, subject5, subject6]

            # Get the courses related to the subjects
            courses = Course.objects.filter(subject__title__in=subjects).distinct()

            # Get the schools that offer the courses
            schools = School.objects.filter(courses__in=courses)

            # Get the users who have chosen the same subjects
            users = User.objects.filter(subjects__title__in=subjects)

            # Get the subjects that the users have chosen
            user_subjects = Subject.objects.filter(user__in=users)

            # Get the courses related to the user subjects
            user_courses = Course.objects.filter(subject__in=user_subjects)

            # Get the schools that offer the user courses
            user_schools = School.objects.filter(courses__in=user_courses)

            # Combine the schools and user schools
            all_schools = schools | user_schools

            # Remove duplicates
            all_schools = all_schools.distinct()

            # Render the results
            return render(request, 'recommendations.html', {'schools': all_schools, 'courses': courses})

    else:
        form = SubjectForm()

    return render(request, 'home.html', {'form': form})
