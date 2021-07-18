from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from voting.models import Feedback
from voting.models import Contact
from voting.models import Registration
from voting.models import Candidate
from voting.models import News

# Create your views here.

def index(request):
     news_data=News.objects.filter()
     return render(request,'index.html',{'news_record':news_data})

def votingregistration(request):
    if request.method == 'POST':
           password=request.POST['password']
           username=request.POST['username']
           first_name='first_name' in request.POST
           last_name='last_name' in request.POST
           email=request.POST['email']
           if User.objects.filter(username=username).exists():
              messages.error(request,"Username Already Exist")
              return redirect('votingregistration')
           elif User.objects.filter(password=password).exists():
              messages.error(request,"Password is invalid")
              return redirect('votingregistration')
           elif User.objects.filter(email=email).exists():
              messages.error(request,"Email Already Exist") 
              return redirect('votingregistration')   
           else :
              user_data=User.objects.create_user(password=password,username=username,first_name=first_name,last_name=last_name,email=email)
              user_data.save()  
              messages.success(request,"You have registered Successfully")
              return redirect('votingregistration') 
    else:     
       return render(request,'votingregistration.html')             
        
def registration(request):
    if request.method=='POST':
           gender=request.POST['gender']
           phone=request.POST['phone']
           voter_id = 'voter_id' in request.POST and request.POST['voter_id']
           address=request.POST['address']
           state=request.POST['state']
           country=request.POST['country']
           copy=request.POST['copy']
           reg_data=Registration(gender=gender,phone=phone,voter_id=voter_id,address=address,state=state,country=country,copy=copy)
           reg_data.save()
           messages.success(request,"You have Send Details Successfully")
           return redirect('registration')
    else:     
        return render(request,'registration.html') 
       
def voting(request):
     v_data=Candidate.objects.all()
     if request.method == 'POST':
        result=Candidate.objects.filter()
        return render(request,'voting.html',{'v_record':v_data,'show_result':result})
     else:
        return render(request,'voting.html',{'v_record':v_data})             
    
def view_result(request): 
     v_data=Candidate.objects.all()
     if request.method == 'POST':
        cast=User.objects.filter().count
        result=Candidate.objects.filter()
        return render(request,'view_result.html',{'v_record':v_data,'show_result':result,'cast':cast})
     else:
        return render(request,'view_result.html',{'v_record':v_data})  

def feedback(request):
    if request.method=='POST':
         feedback_name=request.POST['feedback_name']
         feedback_phone=request.POST['feedback_phone']
         feedback_email=request.POST['feedback_email']
         feedback_address=request.POST['feedback_address']
         feedback_query=request.POST['feedback_query']
         feedback_data=Feedback(feedback_name=feedback_name,feedback_phone=feedback_phone,feedback_email=feedback_email,feedback_address=feedback_address,feedback_query=feedback_query)
         feedback_data.save()
         messages.success(request,"Send Feedback Successfully")
         return redirect('feedback')
    else:    
      return render(request,'feedback.html')     

def contact(request):
    if request.method=='POST':
         contact_name=request.POST['contact_name']
         contact_phone=request.POST['contact_phone']
         contact_email=request.POST['contact_email']
         contact_address=request.POST['contact_address']
         contact_query=request.POST['contact_query']
         contact_data=Contact(contact_name=contact_name,contact_phone=contact_phone,contact_email=contact_email,contact_address=contact_address,contact_query=contact_query)
         contact_data.save()
         messages.success(request,"Send Contact Details Successfully")
         return redirect('contact')
    else:     
       return render(request,'contact.html')  

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user_data = auth.authenticate(username=username,password=password)
        #select * from user where 
        if user_data is not None:
            auth.login(request,user_data)
            return redirect('voting')
        else: 
            messages.error(request,'Invalid username or password')
            return redirect('login') 
    else:            
       return render(request,'login.html')  

def add_candidate(request):
     if request.method=='POST':
         candidate_name=request.POST['candidate_name']
         party=request.POST['party']
         area=request.POST['area']
         candidate_address=request.POST['candidate_address']
         candidate_query=request.POST['candidate_query']
         candidate_photo=request.POST['candidate_photo']
         can_data=Candidate(candidate_name=candidate_name,party=party,area=area,candidate_address=candidate_address,candidate_query=candidate_query,candidate_photo=candidate_photo)
         can_data.save()
         if(can_data):
            messages.success(request,"Candidate Added Successfully")
            return render(request,'add_candidate.html') 
         else:
            messages.danger(request,"Candidate Not Added")
            return render(request,'add_candidate.html')            
     elif request.session._session:  
             return render(request,'add_candidate.html')
     else:
        return render(request,'login.html')        
     
def view_voter(request):
      can_data=Candidate.objects.all()
      if request.session._session:
        return render(request,'view_voter.html',{'can_record':can_data})
      else:
        return redirect(request,'login') 

def delete_voter(request,pk):
    can_data=Candidate.objects.get(id=pk)
    can_data.delete()
    return redirect('view_voter')

def edit_voter(request,pk):
    c_data=Candidate.objects.get(id=pk)
    return render(request,'edit-can.html',{'c_record':c_data})  
    
def update_voter_data(request):
    can_id=request.POST['id']
    can_data=Candidate.objects.get(id=can_id)
    if request.method == 'POST':
       can_data.candidate_name= request.POST['candidate_name']
       can_data.party= request.POST['party']
       can_data.area= request.POST['area']       
       can_data.candidate_address= request.POST['candidate_address']       
       can_data.candidate_query= request.POST['candidate_query']       
       can_data.candidate_photo= request.POST['candidate_photo']       
       can_data.save()
       messages.success(request,"Candidate Updated Successfully")
       return redirect('view_voter')   
           
def verify_voter(request):
      auth_data=User.objects.all()
      if request.session._session:
        return render(request,'verify_voter.html',{'auth_record':auth_data})
      else:
        return redirect(request,'login')  

def delete_user(request,pk):
    user_data=User.objects.get(id=pk)
    user_data.delete()
    return redirect('verify_voter')        

def voter_details(request):
      reg_data=Registration.objects.all()
      if request.session._session:
        return render(request,'voter_details.html',{'reg_record':reg_data})
      else:
        return redirect(request,'login')  

def delete_details(request,pk):
    reg_data=Registration.objects.get(id=pk)
    reg_data.delete()
    return redirect('verify_voter')          

def news_panel(request):
     if request.method=='POST':
         news_link=request.POST['news_link']
         news_text=request.POST['news_text']
         news_data=News(news_link=news_link,news_text=news_text)
         news_data.save()
         if(news_data):
            messages.success(request,"News Added Successfully")
            return render(request,'news_panel.html') 
         else:
            messages.danger(request,"News Not Added")
            return render(request,'news_panel.html')            
     elif request.session._session:  
             return render(request,'news_panel.html')
     else:
        return render(request,'login.html')
        
def logout(request):
     auth.logout(request)
     return redirect('index')     


     