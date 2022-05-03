from django.http.response import JsonResponse
from django.urls.conf import path
from .models import *
from Chairman.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.conf import  settings
import datetime
from django.core.mail import send_mail


# Create your views here.

def m_all_members(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "member" or "Member":
            mid = Member.objects.get(user_id = uid)
            m_all = Member.objects.exclude(user_id =uid)
            context = {
                'uid':uid,
                'mid':mid,
                'm_all':m_all
            }
            return render(request,"MemberApp/m_all_members.html",{'context':context})

def m_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        # mid = Member.objects.get(user_id = uid)
                

        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']

            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                # context = {
                    # 'uid':uid,
                    # 'mid':mid,
                # 0}

                return redirect('m-profile')
        else:
            if uid.role == "member" or "Member":
                mid = Member.objects.get(user_id = uid)
                context = {
                    'uid':uid,
                    'mid':mid,
                }
                return render(request,"MemberApp/m_profile.html",{'context':context})
            # else:
            #     pass
    else:
        return redirect('login')

def m_add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "member":
            mid = Member.objects.get(user_id = uid)
            m_all = Member.objects.exclude(user_id =uid)
            context = {
                'uid':uid,
                'mid':mid,
                'm_all':m_all
            }
            return render(request,"MemberApp/m_add_member.html",{'context':context})


def m_all_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Member.objects.get(user_id = uid)
        n_all = Notice.objects.all().order_by('created_at').reverse()
        context = {
            'uid':uid,
            'mid':mid,
            'n_all':n_all
        }

        return render(request,"MemberApp/m-all-notice.html",{'context':context})
    else:
        return redirect('login')

def m_all_notice_details(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Member.objects.get(user_id = uid)
        nid = Notice.objects.get(id = pk)

        nall = NoticeView.objects.filter(member_id = mid, notice_id = nid)

        if nall:
            print('Alraeady notice read')
        else:
            nvid = NoticeView.objects.create(notice_id = nid, member_id = mid)

        context = {
            'uid':uid,
            'mid':mid,
            'nid':nid
        }

        return render(request,"MemberApp/m-all-notice-details.html",{'context':context})
    else:
        return redirect('login')




def m_all_event(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Member.objects.get(user_id = uid)

        e_all = Event.objects.all().order_by('created_at').reverse()
        context = {
            'uid':uid,
            'mid':mid,
            'e_all':e_all
        }

        return render(request,"MemberApp/m-all-event.html",{'context':context})
    else:
        return redirect('login')

def m_all_event_details(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Member.objects.get(user_id = uid)
        eid = Event.objects.get(id = pk)

        eall = EventView.objects.filter(member_id = mid, event_id = eid)

        if eall:
            print("Already Read")
        else:
            evid = EventView.objects.create(event_id = eid, member_id = mid)

        context={
            'uid':uid,
            'mid':mid,
            'eid':eid
        }
        return render(request,"MemberApp/m-all-event-details.html",{'context':context})
    else:
        return redirect('login')
  
def m_add_event(request):
    if "email" in request.session:
        if request.POST:
            if "pic" in request.FILES and "video" not in request.FILES:
                eid = Event.objects.create(
                    title = request.POST['title'],
                    description = request.POST['description'],
                    pic = request.FILES['pic']
                )

            elif "video" in request.FILES and "pic" not in request.FILES:
                eid = Event.objects.create(
                    title = request.POST['title'],
                    description = request.POST['description'],
                    videofile = request.FILES['video']
                ) 
            elif "video" in request.FILES and "pic" in request.FILES:
                eid = Event.objects.create(
                    title = request.POST['title'],
                    description = request.POST['description'],
                    pic = request.FILES['pic'],
                    videofile = request.FILES['video']
                )
            else:
                eid = Event.objects.create(
                    title = request.POST['title'],
                    description = request.POST['description'],
                )
            return redirect('m-add-event')
        else:
            uid = User.objects.get(email = request.session['email'])
            # uid = User.objects.all()
            mid = Member.objects.get(user_id = uid)
            context = {
                'uid':uid,
                'mid':mid,
            }
            return render(request,"MemberAPP/m-add-event.html",{'context':context})
    else:
        return redirect('login')
