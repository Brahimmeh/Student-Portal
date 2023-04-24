
from urllib.request import Request
from django.contrib import messages
from site import USER_BASE
from django.shortcuts import render
from Portal_Account.Email_BE import email_BE
from django.contrib.auth import login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from Portal_Account.models import MasterU,CustomUser,Staff, Teacher,Students,Courses,Subjects,Attendance_Teacher,Attendance_Student,Note_Student,Compliant_Teacher,Compliant_Student,Mark
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

#global
#username="name"

#Homepage
def showhomepage (request):
    return render(request,"HomePage.html")

# ADMIN
@login_required(login_url='/admin/')
def showAdminPage(request):
    us=request.user
    c1=MasterU.objects.count
    c2=Staff.objects.count
    c3=Teacher.objects.count
    c4=Students.objects.count
    return render(request,"admin_pa.html",{"user":us,"c1":c1,"c2":c2,"c3":c3,"c4":c4})

@login_required(login_url='/admin/')
def ShowAddStaff(request):
    us=request.user
    return render(request,"Add_Staff.html",{"user" :us})

@login_required(login_url='/admin/')
def ShowAddTeacher(request):
    us=request.user
    return render(request,"Add_Teacher.html",{"user" :us})

@login_required(login_url='/admin/')
def ShowAddStudent(request):
    us=request.user
    courses_su=Courses.objects.all
    return render(request,"Add_Student.html",{"courses" :courses_su})

@login_required(login_url='/admin/')
def ShowAddCourse(request):
    us=request.user
    return render(request,"Add_Course.html",{"user" :us})

@login_required(login_url='/admin/')
def ShowManageStaff(request):
    us=request.user
    staff_l=Staff.objects.all
    return render(request,"Manage_Staff.html",{"staffs" :staff_l,"user" :us})

@login_required(login_url='/admin/')
def ShowManageTeacher(request):
    us=request.user
    teacher=Teacher.objects.all
    return render(request,"Manage_Teacher.html",{"teachers" :teacher,"user" :us})

@login_required(login_url='/admin/')
def ShowManageStudent(request):
    us=request.user
    student=Students.objects.all
    course=Courses.objects.all
    return render(request,"Manage_Student.html",{"courses" :course, "students":student,"user" :us})

@login_required(login_url='/admin/')
def ShowManageCourse(request):
    us=request.user
    course=Courses.objects.all
    return render(request,"Manage_Course.html",{"courses":course,"user" :us})

@login_required(login_url='/admin/')
def showListAdmin(request):
    us=request.user
    Staff_list=Staff.objects.all
    Teacher_list=Teacher.objects.all
    Student_list=Students.objects.all
    courses_su=Courses.objects.all
    return render(request,"Show_List_Admin.html",{"user" :us,"staffs" :Staff_list,"teachers" :Teacher_list,"students" :Student_list,"courses" :courses_su,"username" :"braim"})

#STAFF
@login_required(login_url='/Staff_log/')
def showStaffPage(request):
    us=request.user
    return render(request,"staff_pa.html",{"user" :us})

@login_required(login_url='/Staff_log/')
def showAddAttTeacher(request):
    us=request.user
    subject=Subjects.objects.all
    Teacher_list=Teacher.objects.all
    return render(request,"Add_Att_Teach.html",{"user" :us,"teachers" :Teacher_list,"Subjects":subject})

@login_required(login_url='/Staff_log/')
def showAddAttStudent(request):
    us=request.user
    subject=Subjects.objects.all
    Teacher_list=Teacher.objects.all
    student=Students.objects.all
    return render(request,"Add_Att_Student.html",{"user" :us,"teachers" :Teacher_list,"Subjects":subject,"Students":student})

@login_required(login_url='/Staff_log/')
def showAddSubject(request):
    us=request.user
    Teacher_list=Teacher.objects.all
    courses_su=Courses.objects.all
    return render(request,"Add_Subject.html",{"user" :us,"teachers" :Teacher_list,"courses" :courses_su})

@login_required(login_url='/Staff_log/')
def showEditSubject(request):
    us=request.user
    subject=Subjects.objects.all
    Teacher_list=Teacher.objects.all
    courses_su=Courses.objects.all
    return render(request,"Edit_Subject.html",{"user" :us,"teachers" :Teacher_list,"courses" :courses_su,"Subjects":subject})   

@login_required(login_url='/Staff_log/')
def showAddNote(request):
    us=request.user
    courses_su=Courses.objects.all
    return render(request,"Add_Student_Note.html",{"user" :us,"courses" :courses_su})

@login_required(login_url='/Staff_log/')
def showNote(request):
    us=request.user
    note=Note_Student.objects.all
    return render(request,"Show_Note_Staff.html",{"user" :us,"notes" :note})

@login_required(login_url='/Staff_log/')
def showCompTeach(request):
    us=request.user
    comp=Compliant_Teacher.objects.all
    return render(request,"Show_Com_Teach.html",{"user" :us,"complaints_t" :comp})

@login_required(login_url='/Staff_log/')
def showCompStud(request):
    us=request.user
    comp=Compliant_Student.objects.all
    return render(request,"Show_Comp_Stud.html",{"user" :us,"complaints_s" :comp})

@login_required(login_url='/Staff_log/')
def showListStaff(request):
    us=request.user
    Teacher_list=Teacher.objects.all
    Student_list=Students.objects.all
    courses_su=Courses.objects.all
    sub=Subjects.objects.all
    att_t=Attendance_Teacher.objects.all
    att_s=Attendance_Student.objects.all
    return render(request,"list_staff.html",{"user" :us,"attendances_s":att_s,"attendances_t":att_t,"subjects":sub,"teachers" :Teacher_list,"students" :Student_list,"courses" :courses_su,"username" :"braim"})

#Teacher
@login_required(login_url='/Teacher_log/')
def showTeacherPage(request):
    us=request.user
    return render(request,"teacher_pa.html",{"user" :us})

@login_required(login_url='/Teacher_log/')
def showAddMark(request):
    us=request.user
    stud=Students.objects.all
    teach=Teacher.objects.get(admin=us)
    sub=Subjects.objects.all().filter(teacher_id=teach)
    return render(request,"add_mark.html",{"user" :us,"Students":stud,"Subjects":sub})

@login_required(login_url='/Teacher_log/')
def showEditMark(request):
    us=request.user
    teach=Teacher.objects.get(admin=us)
    stud=Students.objects.all
    sub=Subjects.objects.all().filter(teacher_id=teach)
    return render(request,"Edit_Mark.html",{"user" :us,"Students":stud,"Subjects":sub})

@login_required(login_url='/Teacher_log/')
def showAddComp(request):
    us=request.user
    return render(request,"Add_compl_teach.html",{"user" :us})

@login_required(login_url='/Teacher_log/')
def showComplaintTeach(request):
    us=request.user
    teach=Teacher.objects.get(admin=us)
    comp=Compliant_Teacher.objects.all().filter(teacher_id=teach)
    return render(request,"list_comp_teach.html",{"user" :us,"complaints_t" :comp})

@login_required(login_url='/Teacher_log/')
def showlistsub(request):
    us=request.user
    teach=Teacher.objects.get(admin=us)
    sub=Subjects.objects.all().filter(teacher_id=teach)
    return render(request,"list_sub_teach.html",{"user" :us,"subjects":sub})

@login_required(login_url='/Teacher_log/')
def showliststud(request):
    us=request.user
    teach=Teacher.objects.get(admin=us)
    sub=Subjects.objects.all().filter(teacher_id=teach)
    stud=Students.objects.all
    return render(request,"student_list_teach.html",{"user" :us,"students":stud,"subjects":sub})

@login_required(login_url='/Teacher_log/')
def showlistmark(request):
    us=request.user
    teach=Teacher.objects.get(admin=us)
    sub=Subjects.objects.all().filter(teacher_id=teach)
    ma=Mark.objects.all().filter(teacher_id=teach)
    return render(request,"mark_list.html",{"user" :us,"marks":ma,"subjects":sub})

@login_required(login_url='/Teacher_log/')
def show_att_list_teach(request):
    us=request.user
    teach=Teacher.objects.get(admin=us)
    att=Attendance_Teacher.objects.all().filter(teacher_id=teach)
    return render(request,"list_att_teach.html",{"user" :us,"attendances_t":att})
    

#Student
@login_required(login_url='/Student_log/')
def showstudentpage(request):
    us=request.user
    return render(request,"student_pa.html",{"user" :us})

@login_required(login_url='/Student_log/')
def showenrolledcour(request):
    us=request.user
    stud=Students.objects.get(admin=us)
    cou=Courses.objects.all
    return render(request,"Enrolled_cour.html",{"user" :us,"courses":cou,"stud_id":stud})

@login_required(login_url='/Student_log/')
def showsubliststud(request):
    us=request.user
    stud=Students.objects.get(admin=us)
    cou=Courses.objects.all
    sub=Subjects.objects.all
    return render(request,"Sub_list_stu.html",{"user" :us,"courses":cou,"stud_id":stud, "subjects":sub})

@login_required(login_url='/Student_log/')
def showComplaintStud(request):
    us=request.user
    stud=Students.objects.get(admin=us)
    comp=Compliant_Student.objects.all().filter(student_id=stud)
    return render(request,"list_comp_stud.html",{"user" :us,"complaints":comp})

@login_required(login_url='/Student_log/')
def AddCompStudent(request):
    us=request.user
    stud=Students.objects.get(admin=us)
    cou=Courses.objects.all
    sub=Subjects.objects.all
    return render(request,"Add_comp_stud.html",{"user" :us,"courses":cou,"stud_id":stud, "subjects":sub})

@login_required(login_url='/Student_log/')
def showlistmarkstud(request):
    us=request.user
    stud=Students.objects.get(admin=us)
    sub=Subjects.objects.all().filter(course_id=stud.course_id)
    ma=Mark.objects.all().filter(student_id=stud)
    return render(request,"mark_list_stud.html",{"user" :us,"marks":ma,"subjects":sub})

@login_required(login_url='/Student_log/')
def showattliststud(request):
    us=request.user
    stud=Students.objects.get(admin=us)
    att=Attendance_Student.objects.all().filter(student_id=stud)
    return render(request,"list_att_stud.html",{"user" :us,"attendances":att})

@login_required(login_url='/Student_log/')
def showanotestud(request):
    us=request.user
    stud=Students.objects.get(admin=us)
    notes=Note_Student.objects.all().filter(course_id=stud.course_id)
    return render(request,"list_note_stud.html",{"user" :us,"notes":notes})

#log
def ShowAdminLog(request):
    return render(request,"Admin_Log.html")
    
def showStudentLog(request):
    return render(request,"Student_log.html")

def showStaffLog(request):
    return render(request,"Staff_log.html")

def showTeacherLog(request):
    return render(request,"Teacher_Log.html")

#Commun
#Login for all Users

def dologin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Error</h2>")
    else:
        a=request.POST.get("email")
        b= request.POST.get("pass")
        user=email_BE.authenticate(request,username=a,password=b)
        if user!=None:
            login(request,user)
            if(user.user_type=="1"):
                return HttpResponseRedirect("/admin/HomeP")
            elif(user.user_type=="2"):
                return HttpResponseRedirect("/Staff_log/HomeP")
            elif(user.user_type=="3"):
                return HttpResponseRedirect("/Teacher_log/HomP")
            else:
                return HttpResponseRedirect("/Student_log/HomP")       
        else:
            user=email_BE.authenticate_p(request,username=a,password=b)
            #Add different log page inv
            if(user==None):
                if(request.path =="/admin/doLogin"):
                    messages.error(request,"This Account Does Not Exsit In The System, Check Your Informations and Try-Again")
                    return HttpResponseRedirect("/admin/")
                elif(request.path =="/Staff_log/doLogin"):
                    messages.error(request,"This Account Does Not Exsit In The System, Check Your Informations and Try-Again")
                    return HttpResponseRedirect("/Staff_log/")
                elif(request.path =="/Teacher_log/doLogin"):
                    messages.error(request,"This Account Does Not Exsit In The System, Check Your Informations and Try-Again")
                    return HttpResponseRedirect("/Teacher_log/")
                else:
                    messages.error(request,"This Account Does Not Exsit In The System, Check Your Informations and Try-Again")
                    return HttpResponseRedirect("/Student_log/")
            elif(user.user_type=="1"):
                messages.error(request,"The Username or The password entred are invalide, Check Your Informations and Try-Again" )
                return HttpResponseRedirect("/admin/")
            elif(user.user_type=="2"):
                messages.error(request,"The Username or The password entred are invalide, Check Your Informations and Try-Again")
                return HttpResponseRedirect("/Staff_log/")    
            elif(user.user_type=="3"):
                messages.error(request,"The Username or The password entred are invalide, Check Your Informations and Try-Again")
                return HttpResponseRedirect("/Teacher_log/")  
            elif(user.user_type=="4"):
                messages.error(request,"The Username or The password entred are invalide, Check Your Informations and Try-Again")
                return HttpResponseRedirect("/Student_log/")    

def GetUserDt(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def loGout(request):
    logout(request)
    #home
    return HttpResponseRedirect("/")   

#Manage Admin Tasks
@csrf_exempt
def save_staff(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=make_password(request.POST.get("pass")) 
        adr=request.POST.get("adress")
        occ=request.POST.get("rol")
        try:
            user=CustomUser()
            user.user_type="2"
            user.first_name=first_name
            user.last_name=last_name
            user.email="Sta_" + email
            user.password=password
            user.username="Sta_" + email
            user.save()
            user.save_base()

            user1=Staff()
            user1.admin=user
            user1.address=adr
            user1.role=occ
            user1.save()
            user1.save_base()
            messages.success(request,"Staff Member Added Successfuly")
            return HttpResponseRedirect("admin/Add_staff")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/Add_staff")
        

@csrf_exempt
def save_teacher(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=make_password(request.POST.get("pass")) 
        adr=request.POST.get("adress")
        try:
            user=CustomUser()
            user.user_type="3"
            user.first_name=first_name
            user.last_name=last_name
            user.email="Te_" + email
            user.password=password
            user.username="Te_" + email
            user.save()
            user.save_base()

            user1=Teacher()
            user1.admin=user
            user1.address=adr
            user1.save()
            user1.save_base()
            messages.success(request,"Teacher Added Successfuly")
            return HttpResponseRedirect("admin/Add_teacher")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/Add_teacher")

@csrf_exempt
def save_course(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        name=request.POST.get("name")
        dur=request.POST.get("dur")
        try:
            user1=Courses()
            user1.course_name=name
            user1.duration=dur
            user1.save()
            user1.save_base()
            messages.success(request,"Course Added Successfuly")
            return HttpResponseRedirect("admin/Add_course")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/Add_course")


@csrf_exempt
def save_student(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        gender=request.POST.get("gender")
        email=request.POST.get("email")
        password=make_password(request.POST.get("pass")) 
        course_id=request.POST.get("course")
        Starty=request.POST.get("startY")
        endy=request.POST.get("endY")
        adr=request.POST.get("adress")
        try:
            user=CustomUser()
            user.user_type="4"
            user.first_name=first_name
            user.last_name=last_name
            user.email="Etu_" + email
            user.password=password
            user.username="Etu_" + email
            user.save()
            user.save_base()
            course_objct=Courses.objects.get(id=course_id)
            user1=Students()
            user1.admin=user
            user1.course_id=course_objct
            user1.gender=gender
            user1.address=adr
            user1.session_start_year=Starty
            user1.session_end_year=endy
            user1.save()
            user1.save_base()
            messages.success(request,"Student Added Successfuly")
            return HttpResponseRedirect("admin/Add_student")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/Add_student")
@csrf_exempt
def manage_course(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course")
        name=request.POST.get("name")
        dur=request.POST.get("dur")
        try:
            course_objct=Courses.objects.all().filter(id=course_id)
            course_objct.update(course_name=str(name),duration=dur)
            messages.success(request,"Course Edited Successfuly")
            return HttpResponseRedirect("admin/manage_course")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/manage_course")


@csrf_exempt
def manage_staff(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        admin_id=request.POST.get("admin_id")
        password=make_password(request.POST.get("pass")) 
        adr=request.POST.get("adress")
        occ=request.POST.get("rol")
        try:
            user=CustomUser.objects.all().filter(id=admin_id)
            user.update(first_name=str(first_name),last_name=str(last_name),password=password)
            user1=Staff.objects.all().filter(admin=admin_id)
            user1.update(role=str(occ),address=str(adr))
            messages.success(request,"Staff Member Edited Successfuly")
            return HttpResponseRedirect("admin/manage_staff")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/manage_staff")


@csrf_exempt
def manage_teacher(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        admin_id=request.POST.get("admin_id")
        password=make_password(request.POST.get("pass")) 
        adr=request.POST.get("adress")
        try:
            user=CustomUser.objects.all().filter(id=admin_id)
            user.update(first_name=str(first_name),last_name=str(last_name),password=password)
            user1=Teacher.objects.all().filter(admin=admin_id)
            user1.update(address=str(adr))
            messages.success(request,"Teacher Edited Successfuly")
            return HttpResponseRedirect("admin/manage_teacher")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/manage_teacher")


@csrf_exempt
def manage_student(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        gender=request.POST.get("gender")
        admin_id=request.POST.get("admin_id")
        password=make_password(request.POST.get("pass")) 
        course=request.POST.get("course")
        Starty=request.POST.get("startY")
        endy=request.POST.get("endY")
        adr=request.POST.get("adress")
        try:
            user=CustomUser.objects.all().filter(id=admin_id)
            user.update(first_name=str(first_name),last_name=str(last_name),password=password)
            user1=Students.objects.all().filter(admin=admin_id)
            user1.update(address=str(adr),gender=str(gender),course_id=course,session_start_year=Starty,session_end_year=endy)
            messages.success(request,"Student Edited Successfuly")
            return HttpResponseRedirect("admin/manage_student")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again (Email Adress Must Be Unique)")
            return HttpResponseRedirect("admin/manage_student")

#Manage Staff Tasks
@csrf_exempt
def save_subject(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        sub_name=request.POST.get("name")
        course_id=request.POST.get("course")
        teacher_id=request.POST.get("teacher")
        
        try:
            sub=Subjects()
            sub.subject_name=sub_name
            course_objct=Courses.objects.get(id=course_id)
            teacher_objct=Teacher.objects.get(id=teacher_id)
            sub.teacher_id=teacher_objct
            sub.course_id=course_objct
            sub.save()
            sub.save_base()
            messages.success(request,"Subject Added Successfuly")
            return HttpResponseRedirect("Staff_log/Add_subject")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Staff_log/Add_subject")

@csrf_exempt
def edit_subject(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        sub_name=request.POST.get("name")
        sub_id=request.POST.get("subject")
        course_id=request.POST.get("course")
        teacher_id=request.POST.get("teacher")
        
        try:
            sub=Subjects.objects.all().filter(id=sub_id)
            sub.update(subject_name=str(sub_name),course_id=course_id,teacher_id=teacher_id)
            messages.success(request,"Subject Edited Successfuly")
            return HttpResponseRedirect("Staff_log/Edit_subject")
        except:
            messages.error(request,"An Error Occuried While Editing, Try Again")
            return HttpResponseRedirect("Staff_log/Edit_subject")

@csrf_exempt
def save_att_teacher(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        sub_id=request.POST.get("subject")
        d=request.POST.get("day")
        stat=request.POST.get("status")
        teacher_id=request.POST.get("teacher")
        
        try:
            att=Attendance_Teacher()
            att.attendance_date=d
            sub=Subjects.objects.get(id=sub_id)
            teach=Teacher.objects.get(id=teacher_id)
            att.subject_id=sub
            att.status=stat
            att.teacher_id=teach
            att.save()
            att.save_base()
            messages.success(request,"Attendance Added Successfuly")
            return HttpResponseRedirect("Staff_log/Add_att_teacher")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Staff_log/Add_att_teacher")

@csrf_exempt
def save_att_student(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        sub_id=request.POST.get("subject")
        day=request.POST.get("day")
        stat=request.POST.get("status")
        student_id=request.POST.get("Student")
        
        try:
            att=Attendance_Student()
            att.attendance_date=day
            sub=Subjects.objects.get(id=sub_id)
            stud=Students.objects.get(id=student_id)
            att.subject_id=sub
            att.status=stat
            att.student_id=stud
            att.save()
            att.save_base()
            messages.success(request,"Attendance Added Successfuly")
            return HttpResponseRedirect("Staff_log/Add_att_student")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Staff_log/Add_att_student")

@csrf_exempt
def save_note(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        us=request.user
        msg=request.POST.get("note")
        course_id=request.POST.get("course")
        
        
        try:
            note=Note_Student()
            staf=Staff.objects.get(admin=us)
            note.Note=msg
            course_objct=Courses.objects.get(id=course_id)
            note.course_id=course_objct
            note.staff_id=staf
            note.save()
            note.save_base()
            messages.success(request,"Note Added Successfuly")
            return HttpResponseRedirect("Staff_log/Add_Student_Note")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Staff_log/Add_Student_Note")

#Teacher
@csrf_exempt
def save_mark(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        sub_id=request.POST.get("subject")
        stud_id=request.POST.get("Student")
        val=request.POST.get("value")
        us=request.user
        
        try:
            m=Mark()
            sub=Subjects.objects.get(id=sub_id)
            stud=Students.objects.get(id=stud_id)
            teach=Teacher.objects.get(admin=us)
            m.subject_id=sub
            m.student_id=stud
            m.teacher_id=teach
            m.value=val
            m.save()
            m.save_base()
            messages.success(request,"Mark Added Successfuly")
            return HttpResponseRedirect("Teacher_log/Add_mark")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Teacher_log/Add_mark")

@csrf_exempt
def edit_mark(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        sub_id=request.POST.get("subject")
        stud_id=request.POST.get("Student")
        val=request.POST.get("value")
        us=request.user
        
        try:
            teach=Teacher.objects.get(admin=us)
            m=Mark.objects.all().filter(subject_id=sub_id,student_id=stud_id,teacher_id=teach)
            m.update(value=val)
            messages.success(request,"Mark Edited Successfuly")
            return HttpResponseRedirect("Teacher_log/edit_mark")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Teacher_log/edit_mark")

@csrf_exempt
def save_comp_teach(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        clas=request.POST.get("class_s")
        stud=request.POST.get("name_s")
        cours=request.POST.get("course_s")
        compl=request.POST.get("comp")
        us=request.user
        
        try:
            com=Compliant_Teacher()
            teach=Teacher.objects.get(admin=us)
            com.teacher_id=teach
            com.Student_name=stud
            com.Student_course=cours
            com.Student_class=clas
            com.complaint=compl
            com.save()
            com.save_base()
            messages.success(request,"Complaint Sent Successfuly")
            return HttpResponseRedirect("Teacher_log/Add_complaint_teach")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Teacher_log/Add_complaint_teach")

#Student
@csrf_exempt
def save_comp_stud(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        teach=request.POST.get("name")
        sub=request.POST.get("subject")
        compl=request.POST.get("comp")
        us=request.user
        
        try:
            com=Compliant_Student()
            stud=Students.objects.get(admin=us)
            com.student_id=stud
            com.teacher_name=teach
            com.Subject_name=sub
            com.complaint=compl
            com.save()
            com.save_base()
            messages.success(request,"Complaint Sent Successfuly")
            return HttpResponseRedirect("Student_log/Add_complaint_stud")
        except:
            messages.error(request,"An Error Occuried While Adding, Try Again")
            return HttpResponseRedirect("Student_log/Add_complaint_stud")