from django.shortcuts import render, redirect
from .models import Post
from .forms import ContactForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Home page
def home(request):
   #Query all post
   all_posts = Post.objects.all()

   context = {
      'posts' : all_posts,
   }
   return render(request, 'blog/home.html', context)


# Post detail page
@login_required(login_url='sign_in')
def post_detail(request, post_id):
   single_post = Post.objects.get(id=post_id)
   return render(request, 'blog/post_detail.html', {'post' : single_post})


# contact page
def contact(request):
   form = ContactForm(request.POST)
   if form.is_valid():
      form.save()       # กด Submit = save
      print("ข้อมูลถูกส่งเรียบร้อย")
      return redirect("home")    # เปลี่ยนเป็นหน้าอื่นหลังจากกด submit ถ้าไม่มีจะค้างที่หน้าเดิม
   else:
      form = ContactForm()
      print("ฟอร์มเปิด")
      print(form)
   return render(request, 'blog/contact.html', {'form' : form})


# Register page
def register(request):
   form = RegisterForm()
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         form.save()
         print("สำเร็จ")
         return redirect("home")
   else:
      form = RegisterForm()
      print("แสดงฟอร์มเรียบร้อย")
   return render(request, 'blog/register.html', {'form' : form})


# Log-in page
def sign_in(request):       ## Login ชื่อซ้ำกับฟังก์ชันสำเร็จรูป เลยต้องใช้ sign_in
   if request.method == 'POST':
      username_form = request.POST["username"]     ## ตัวแปร ["username"] รับค่า username ที่กรอกมาจากตัวแปร name ในหน้า login.html 
      password_form = request.POST["password"]     ## ตัวแปร ["password"] รับค่า username ที่กรอกมาจากตัวแปร name ในหน้า login.html 
      user = authenticate(request, username=username_form, password=password_form)   ## เก็บค่า username, password ในตัวแปร user ตัวเดียว
      if user is not None:
         login(request, user)
         print("success!!")
         return redirect("home")
      else:
         print("log-in not success")
   return render(request, 'blog/login.html')


# Log-out page
def sign_out(request):       
   logout(request)
   return redirect('home')



