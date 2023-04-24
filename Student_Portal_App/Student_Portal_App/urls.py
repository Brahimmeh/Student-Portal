"""Student_Portal_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Student_Portal_App.settings import MEDIA_URL,MEDIA_ROOT,STATIC_ROOT,STATIC_URL
from Portal_Account import views

urlpatterns = [
    path('', views.showhomepage),
    path('admin/', views.ShowAdminLog),
    path('admin/doLogin',views.dologin),
    path('admin/HomeP', views.showAdminPage),
    path('admin/Add_staff', views.ShowAddStaff),
    path('admin/Add_teacher', views.ShowAddTeacher),
    path('admin/Add_student', views.ShowAddStudent),
    path('admin/Add_course', views.ShowAddCourse),
    path('admin/manage_staff', views.ShowManageStaff),
    path('admin/manage_teacher', views.ShowManageTeacher),
    path('admin/manage_student', views.ShowManageStudent),
    path('admin/manage_course', views.ShowManageCourse),
    path('admin/show_list_admin', views.showListAdmin),
    path('save_staff',views.save_staff),
    path('save_teacher',views.save_teacher),
    path('save_student',views.save_student),
    path('save_course',views.save_course),
    path('manage_course',views.manage_course),
    path('manage_staff',views.manage_staff),
    path('manage_teacher',views.manage_teacher),
    path('manage_student',views.manage_student),
    #staff
    path('Staff_log/', views.showStaffLog),
    path('Staff_log/doLogin',views.dologin),
    path('Staff_log/HomeP', views.showStaffPage),
    path('Staff_log/Add_att_teacher', views.showAddAttTeacher),
    path('Staff_log/Add_att_student', views.showAddAttStudent),
    path('Staff_log/Add_subject', views.showAddSubject),
    path('Staff_log/Edit_subject', views.showEditSubject),
    path('Staff_log/Add_Student_Note', views.showAddNote),
    path('Staff_log/Show_Student_Note', views.showNote),
    path('Staff_log/show_list_staff', views.showListStaff),
    path('Staff_log/complaint_teach', views.showCompTeach),
    path('Staff_log/complaint_stud', views.showCompStud),
    path('save_subject', views.save_subject),
    path('edit_subject',views.edit_subject),
    path('save_att_teacher',views.save_att_teacher),
    path('save_att_student',views.save_att_student),
    path('save_note',views.save_note),
    #Teacher
    path('Teacher_log/', views.showTeacherLog),
    path('Teacher_log/doLogin',views.dologin),
    path('Teacher_log/HomP', views.showTeacherPage),
    path('Teacher_log/Add_mark', views.showAddMark),
    path('Teacher_log/edit_mark', views.showEditMark),
    path('Teacher_log/Add_complaint_teach', views.showAddComp),
    path('Teacher_log/list_com_teach', views.showComplaintTeach),
    path('Teacher_log/list_sub_teach', views.showlistsub),
    path('Teacher_log/show_list_student', views.showliststud),
    path('Teacher_log/show_mark_list', views.showlistmark),
    path('Teacher_log/show_att_list_teach', views.show_att_list_teach),
    path('save_mark', views.save_mark),
    path('edit_mark', views.edit_mark),
    path('add_comp', views.save_comp_teach),
    #Sudent
    path('Student_log/', views.showStudentLog),
    path('Student_log/doLogin',views.dologin),
    path('Student_log/HomP', views.showstudentpage),
    path('Student_log/see_enrolled_course', views.showenrolledcour),
    path('Student_log/see_sub_stud', views.showsubliststud),
    path('Student_log/Add_complaint_stud', views.AddCompStudent),
    path('Student_log/list_com_stud', views.showComplaintStud),
    path('Student_log/show_mark_list_stud', views.showlistmarkstud),
    path('Student_log/show_att_list_stud', views.showattliststud),
    path('Student_log/show_note_stud', views.showanotestud),
    path('add_comp_stud', views.save_comp_stud),
    


    path('getUserDet',views.GetUserDt),
    path('logout',views.loGout),
    
    
    #path('admin/', admin.site.urls),
]+static(MEDIA_URL,document_root=MEDIA_ROOT)+static(STATIC_URL,document_root=STATIC_ROOT)
