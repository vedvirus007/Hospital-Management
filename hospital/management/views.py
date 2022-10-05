from django.shortcuts import render,HttpResponse
from .models import billing, hospital,doctor,patient,comment
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
User = get_user_model()
# Create your views here.




def signup(request):
    return render(request, 'signup.html')

def signup_admin(request):
   
    context={'success':'not submitted'}
    if request.method=="POST":
        hosp_name=request.POST['hospitalname']
        admin_name=request.POST['adminname']
        address=request.POST['address']
        passw=request.POST['Password']
        repassw=request.POST['ConfirmPassword']
        # print(hosp_name , admin_name ,address)
        ins=hospital(hospital_name=hosp_name,admin_name=admin_name,hospital_address=address)
        if passw==repassw:
            ins.save()
            myuser=User.objects.create_user(username=admin_name,password=passw,type_user='admins')
            myuser.save()
    return render(request, 'admin_signup_form.html',context)

def signup_doc(request):

    if request.method=="POST":
        doc_name=request.POST['username']
        qual=request.POST['qualification']
        hosp_name=request.POST['hospname']
        passw=request.POST['Password']
        repassw=request.POST['ConfirmPassword']
        # print(hosp_name , admin_name ,address)
        ins=doctor(doctor_name=doc_name,qualification=qual,hospital_name=hosp_name)
        if passw==repassw:
            ins.save()
            myuser=User.objects.create_user(username=doc_name,password=passw,type_user='doctor')
            myuser.save()
    return render(request, 'doctor_signup_form.html')

def signup_patient(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        # f=request.POST['adminname']
        # address=request.POST['address']
        passw=request.POST['Password']
        repassw=request.POST['ConfirmPassword']
        # user_type=patient
        # print(hosp_name , admin_name ,address)
        if passw==repassw:
            myuser=User.objects.create_user(username,email,passw,type_user='user')
            myuser.save()
    return render(request, 'patient_signup_form.html')

def patient_admission(request):
    context={'doc':doctor.objects.all()}
    if request.method=="POST":
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        illness=request.POST['Illness']
        doctor_select=request.POST['select_doctor']
        # print(hosp_name , admin_name ,address)
        ins=patient(patient_name=f_name,illness=illness,doctor_select=doctor_select)
        ins.save()
        myuser=User.objects.create_user(username=f_name,password='admit',type_user='patient')
        myuser.save()
        context={'doc':doctor.objects.all()}
    return render(request, 'patient_submit_form.html',context)

def say_doc(request):
    alldoctors=doctor.objects.all()
    context={'doc':alldoctors}
    return render(request, 'doctor_table.html',context)

def doc_profile(request, id):
    doc_obj = doctor.objects.get(id=id)
    context = {
        'doc' : doc_obj
    }
    return render(request, 'doctor_profile.html',context)

def say_pat(request):
    allpatients=patient.objects.all()
    context={'pat':allpatients}
    return render(request, 'patient_table.html',context)

def pat_profile(request, id):
    pat_obj = patient.objects.get(id=id)
    context = {
        'pat' : pat_obj
    }
    return render(request, 'patient_profile.html',context)

def say_admin(request):
   allhospitals=hospital.objects.all()
   context={'hosp':allhospitals}
   return render(request, 'admin_table.html',context)

def admin_profile(request, id):
    admin_obj = hospital.objects.get(id=id)
    context = {
        'adm' : admin_obj
    }
    return render(request, 'admin_profile.html',context)

def say_home(request):
    allcomments=comment.objects.all()
    context={'comm':allcomments}
    for i in allcomments:
        print(i.comment)
    return render(request, 'home.html',context)

    
def contact(request):
    return render(request, 'contact.html')


def userlogin(request):
    
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        pass1=request.POST['pass1']
        user=authenticate(username=loginusername,password=pass1)
        
        if user is not None:
            login(request,user)
            
    return render(request, 'login.html')


# def handlelogin(request):
#     context={'success':'not valid'}
#     if request.method=="POST":
#         loginusername=request.POST['loginusername']
#         pass1=request.POST['pass1']
#         user=authenticate(username=loginusername,password=pass1)
        
#         if user is not None:
#             login(request,user)
#             context={'success':' valid'}
#     return render(request,'userlogin.html',context)


def handlecomment(request):
    
    if request.method=="POST":
        u_name=request.POST['u_name']
        u_comment=request.POST['user_comment']
        ins=comment(user_name=u_name,comment=u_comment)
        ins.save()
    return render(request, 'home.html')     



def handlelogout(request):
    logout(request)
    return render(request, 'logout_user.html') 

def billGenerator(request):
    return render(request, 'invoice_generator.html')
        
def invoice(request):
    if request.method=="POST":
        f_name = request.POST['name']
        h_name = request.POST['hospitalname']
        med_cost = request.POST['medicine']
        checks = request.POST.getlist('checks[]')
        print(checks)
        cost = 0
        for i in checks:
            cost+=int(i)*500
        cost+=int(med_cost)    
        ins = billing(patient_name = f_name,hos_name = h_name, cost = cost)    
        ins.save()
        print(cost, f_name, h_name)

        context = {
            'bills' : checks, 
            'total' : cost,
            'insta' : h_name,
            'med':med_cost,
            'discount':0.1*int(cost),
            'discount_amount':0.9*int(cost)
        }

    return render(request, 'invoice.html', context)

def NewInvoice(request):
    if request.method=="POST":
    #    ins = billing(paid_cost=True)
    #    ins.save()
    #    print(billing.paid_cost)
    #    context = {
    #         'bills' : checks, 
    #         'total' : cost,
    #         'insta' : h_name
    #     }
         return render(request, 'new_invoice.html') 