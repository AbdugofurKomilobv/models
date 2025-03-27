from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from blog.models import Post
from .models import CustomUserManager, User

def batafsi(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Xato bo‘lsa, 404 qaytaradi
    return render(request, "post_detail.html", {"post": post})

def user_login(request):
    if request.method == "POST":
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]

        user = authenticate(request, phone_number=phone_number, password=password)

        if user is not None:
            login(request, user)

            if user.is_admin:
                return redirect("admin_panel")
            elif user.is_teacher:
                return redirect("teacher_panel")
            elif user.is_student:
                return redirect("student_panel")
        else:
            messages.error(request, "Telefon raqam yoki parol xato!")

    return render(request, "login.html")

def admin_panel(request):
    users = User.objects.all()

    db = {
        'users':users
    }

    return render(request=request,template_name='admin_panel.html',context=db)

def teacher_panel(request):
    return render(request, "teacher_panel.html")

def student_panel(request):
    return render(request, "student_panel.html")



def add_user(request):
    if request.method == "POST":
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]
        name = request.POST["name"]
        role = request.POST["role"]
        password = request.POST["password"]

        user = CustomUserManager.objects.create_user(phone_number=phone_number, email=email, name=name, password=password)

        if role == "teacher":
            user.is_teacher = True
        elif role == "student":
            user.is_student = True

        user.save()
        messages.success(request, f"{name} muvaffaqiyatli qo‘shildi!")
        return redirect("admin_panel")

    return render(request, "add_user.html")

def add_student(request):
    if request.method == "POST":
        print(request.POST)  # Debug uchun
        
        phone_number = request.POST.get("phone")  # HTML dagi input name="phone"

        if not phone_number:
            return HttpResponse("Telefon raqam kiritilmadi!", status=400)

        # Telefon raqami oldin bazada borligini tekshiramiz
        if User.objects.filter(phone_number=phone_number).exists():
            return HttpResponse("Bu telefon raqam allaqachon mavjud!", status=400)

        # Yangi foydalanuvchini yaratamiz
        user = User.objects.create_user(
            phone_number=phone_number,
            email=request.POST.get("email"),
            name=request.POST.get("name"),
            is_student=True,
        )
        return redirect("admin_panel")  # Qo‘shilgandan keyin admin panelga qaytarish

    return render(request, "add_student.html")




def add_teacher(request):
    return render(request, 'add_teacher.html')



def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.save()
        return redirect("admin_panel")

    return render(request, "edit_user.html", {"user": user})
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect("admin_panel")