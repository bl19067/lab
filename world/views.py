from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
# Create your views here.
def index(request):
	params={
		'title':'ctf_b',
		'msg':'sign in or sign up to regist.',
		'sign_up':'sign_up',
		'login':'login',
	}
	return render(request,'hello/index.html', params)
#入力した場合に結果を返す関数
def form(request):
	msg=request.POST['msg']
	params={
		'title':'form',
		'msg':'Thank you for registing.Hello! '+msg+'.',
	}
	return render(request,'hello/registed.html',params)

def next(request):
	params={
		'title':'Welcome!',
		'msg':'please your information',
		
		
	}
	return render(request,'hello/sign_up.html',params)


def login(request):
	params={
		'title':'login user',
		'msg':'your data',
		'form':HelloForm()
		
	}
	if (request.method=='POST'):
		params['message']='name:'+request.POST['name']+'<br>mail:'+request.POST['mail']+'<br>age:'+request.POST['age']
		params['form']=HelloForm(request.POST)
	return render(request,'hello/login.html',params)