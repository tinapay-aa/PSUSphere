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
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_students"] = Student.objects.count()
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()

        today = timezone.now().date()
        count = (
            OrgMember.objects.filter(
                date_joined__year=today.year
            )
            .values("student")
            .distinct()
            .count()
        )

        context["students_joined_this_year"] = count

        return context


class SearchableListView(ListView):
    search_fields = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()

        if query:
            filters = Q()
            for field in self.search_fields:
                filters |= Q(**{f'{field}__icontains': query})
            queryset = queryset.filter(filters)

        return queryset

class OrganizationList(SearchableListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'Org_Templates/org_list.html'
    paginate_by = 5
    ordering = ["college__college_name","name"]
    search_fields = ('name', 'description', 'college__college_name')


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
    template_name = 'Org_Templates/org_del.html'
    success_url = reverse_lazy('organization-list')


class OrgMemberList(SearchableListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'Org_Member_Templates/org_member_list.html'
    paginate_by = 5
    search_fields = (
        'student__student_id',
        'student__firstname',
        'student__lastname',
        'organization__name',
    )

    def get_ordering(self):
        allowed = ('student__firstname', 'student__lastname', 'date_joined')
        sort_by = self.request.GET.get('sort_by')

        if sort_by in allowed:
            return sort_by

        return 'student__lastname'


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


class StudentList(SearchableListView):
    model = Student
    context_object_name = 'student'
    template_name = 'Student_Templates/student_list.html'
    paginate_by = 5
    search_fields = (
        'student_id',
        'firstname',
        'lastname',
        'middlename',
        'program__prog_name',
    )


class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'Student_Templates/student_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"
    template_name = 'Student_Templates/student_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'Student_Templates/student_del.html'
    success_url = reverse_lazy('student-list')


class CollegeList(SearchableListView):
    model = College
    context_object_name = 'college'
    template_name = 'College_Templates/college_list.html'
    paginate_by = 5
    search_fields = ('college_name',)


class CollegeCreateView(CreateView):
    model = College
    fields = "__all__"
    template_name = 'College_Templates/college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeUpdateView(UpdateView):
    model = College
    fields = "__all__"
    template_name = 'College_Templates/college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeDeleteView(DeleteView):
    model = College
    fields = "__all__"
    template_name = 'College_Templates/college_del.html'
    success_url = reverse_lazy('college-list')


class ProgramList(SearchableListView):
    model = Program
    context_object_name = 'program'
    template_name = 'Program_Templates/program_list.html'
    paginate_by = 5
    search_fields = ('prog_name', 'college__college_name')

    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "prog_name"


class ProgramCreateView(CreateView):
    model = Program
    fields = "__all__"
    template_name = 'Program_Templates/program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramUpdateView(UpdateView):
    model = Program
    fields = "__all__"
    template_name = 'Program_Templates/program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramDeleteView(DeleteView):
    model = Program
    fields = "__all__"
    template_name = 'Program_Templates/program_del.html'
    success_url = reverse_lazy('program-list')