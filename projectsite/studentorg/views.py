from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization
from studentorg.forms import OrganizationForm
from studentorg.models import (
    OrgMember,
    Student,
    College,
    Program
)
from django.urls import reverse_lazy

class HomePageView(ListView):
 model = Organization
 context_object_name = 'home'
 template_name = "home.html"

# Organization Views
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'Org_Templates/org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'Org_Templates/org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'Org_Templates/org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'del.html'
    success_url = reverse_lazy('organization-list')

# Org Member Views
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'Org_Member_Templates/org_member_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = "__all__"
    template_name = 'Org_Member_Templates/org_member_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = "__all__"
    template_name = 'Org_Member_Templates/org_member_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'Org_Member_Templates/org_member_del.html'
    success_url = reverse_lazy('orgmember-list')

# Student Views
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5


class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

# College Views
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5


class CollegeCreateView(CreateView):
    model = College
    fields = "__all__"
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeUpdateView(UpdateView):
    model = College
    fields = "__all__"
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

# Program views
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5


class ProgramCreateView(CreateView):
    model = Program
    fields = "__all__"
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramUpdateView(UpdateView):
    model = Program
    fields = "__all__"
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')