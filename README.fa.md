# 📝 دیاری برنامه‌نویسی

یک برنامه ساده برای **ثبت دستاوردهای روزانه در برنامه‌نویسی** با استفاده از **Python و MySQL**.  
می‌توانید آنچه امروز یاد گرفته‌اید را ثبت کنید، به راحتی گذشته‌ی خود را مشاهده کنید و روند یادگیری خود را دنبال کنید.  

---

## 📌 ویژگی‌ها
- ثبت یادداشت جدید همراه با محتوا و تاریخ  
- مشاهده همه‌ی یادداشت‌های گذشته به ترتیب زمانی  
- ذخیره‌سازی داده‌ها در **پایگاه داده MySQL**  
- رابط کاربری ساده و خط فرمانی (CLI)  

---

## 🗂 ساختار پروژه

    ├── main.py # برنامه اصلی و رابط خط فرمان
    ├── database.py # اتصال و توابع کمکی پایگاه داده
    └── README.md # مستندات پروژه

---

## ▶️ پیش‌نیازها
- Python 3.8 یا بالاتر  
- نصب و اجرای **MySQL Server**  
- بسته پایتون: `mysql-connector-python`

    نصب بسته مورد نیاز:
    ```bash
    pip install mysql-connector-python

---

## 🏁 راه‌اندازی و اجرا

1. مطمئن شوید MySQL در حال اجراست و اطلاعات اتصال در database.py مطابق سرور شماست:
    ```python
   connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="data"
)

2. ایجاد دیتابیس در صورت عدم وجود:
    ```sql
   CREATE DATABASE data;

3. اجرای برنامه:
    ```bash
   python main.py

---

## 🧑‍💻 نمونه استفاده

    welcome to the programming diary!
    
    please select one of the following options:
    1) Add new entry for today
       2) View all entries
       3) Exit.
    
    Your selection: 1
    What have you learned today?: یادگیری کلاس‌ها و OOP در پایتون
    Enter the date: 2025-09-16
    
    please select one of the following options:
    1) Add new entry for today
       2) View all entries
       3) Exit.
    
    Your selection: 2
    2025-09-16
    یادگیری کلاس‌ها و OOP در پایتون

---