# import django.http
import django.shortcuts
# from django.template import loader, Context
# from django import forms
# from User.models import User
#
# class UserForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     #headImg = forms.FileField()
#
# # Create your views here.
def index(req): #(id,params)
    #return HttpResponse("<p>hello</p>")
    #id will be assign from urls
    #params are parameters without names
    user = "zihan"
    #user = req.COOKIE.get('username','')
    #username = req.session.get('username','anybody')
    book_list = ['python', 'java', 'php', 'web']

    return django.shortcuts.render_to_response('pages/index.html', {'title':'my page','book_lists':book_list,'user':user})

# def template(req):
#     t = loader.get_template("pages/template.html")
#     c = Context({})
#
#     return django.http.HttpResponse(t.render(c));
#
# def register(req):
#     if req.method == 'POST':
#         form = UserForm(req.POST)#, req.FILES)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             User.objects.create(username = username, password = password)
#             #objects.filter is to confirm if the user is existed
#             print (form.cleaned_data)
#             #form.cleaned_data['headImg'].name
#             '''
#             fp = file('/upload/'+uf.cleaned_data['headImg'].name, 'wb')
#             s = uf.cleaned_data['headImg'].read()
#             fp.write(s)
#             fp.close()
#             '''
#             return django.http.HttpResponse('ok')
#     else:
#         form = UserForm()
#     return django.shortcuts.render_to_response('pages/register.html', {'form':form})
#
# def login(req):
#     if req.method == 'POST':
#         form = UserForm(req.POST)#, req.FILES)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             users = User.objects.filter(username = username, password = password) #or username_exact
#             #objects.filter is to confirm if the user is existed
#             #print (form.cleaned_data)
#             #form.cleaned_data['headImg'].name
#             '''
#             fp = file('/upload/'+uf.cleaned_data['headImg'].name, 'wb')
#             s = uf.cleaned_data['headImg'].read()
#             fp.write(s)
#             fp.close()
#             '''
#             if users:
#                 response = django.http.HttpResponseRedirect('/career_refer/index/')
#                 response.set_cookie('username', username, 3600)
#                 #req.session['username'] = username
#                 return response
#             else:
#                 return django.http.HttpResponseRedirect('/career_refer/login')
#     else:
#         form = UserForm()
#     return django.shortcuts.render_to_response('pages/login.html', {'form':form})
#
# def logout(req):
#     response =  django.http.HttpResponse('/career_refer/logout')
#     response.delete_cookie('username')
#     #del req.session['username']
#     return response('logut ok')