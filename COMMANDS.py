# Windows PowerShell
# (C) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.
#
# Попробуйте новую кроссплатформенную оболочку PowerShell (https://aka.ms/pscore6)
#
# PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4> python -m venv venv
# PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4> venv\scripts\activate
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4> pip install Django
# Collecting Django
#   Using cached Django-4.0.3-py3-none-any.whl (8.0 MB)
# Collecting backports.zoneinfo
#   Using cached backports.zoneinfo-0.2.1-cp38-cp38-win_amd64.whl (38 kB)
#   Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)
# Installing collected packages: tzdata, sqlparse, backports.zoneinfo, asgiref, Django
# Successfully installed Django-4.0.3 asgiref-3.5.0 backports.zoneinfo-0.2.1 sqlparse-0.4.2 tzdata-2022.1
# WARNING: You are using pip version 21.1.1; however, version 22.0.4 is available.
# You should consider upgrading via the 'c:\users\анастасия лебедева\desktop\python\newspaper4\venv\scripts\python.exe -m pip install --upgrade pip' command.
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4> python -m django-admin startproject NewsPaper
# C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\venv\scripts\python.exe: No module named django-admin
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4> django-admin startproject NewsPaper
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4> cd NewsPaper
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\NewsPaper> python3 manage.py startapp news
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\NewsPaper> py manage.py startapp news
# Traceback (most recent call last):
#   File "manage.py", line 22, in <module>
#     main()
#   File "manage.py", line 18, in main
#     execute_from_command_line(sys.argv)
#   File "C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\venv\lib\site-packages\django\core\management\__init__.py", line 446, in execute_from_command_line
#     utility.execute()
#   File "C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\venv\lib\site-packages\django\core\management\__init__.py", line 420, in execute
#     django.setup()
#   File "C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\venv\lib\site-packages\django\__init__.py", line 24, in setup
#     apps.populate(settings.INSTALLED_APPS)
#   File "C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\venv\lib\site-packages\django\apps\config.py", line 228, in create
#     import_module(entry)
#   File "C:\Users\Анастасия Лебедева\AppData\Local\Programs\Python\Python38\lib\importlib\__init__.py", line 127, in import_module
#     return _bootstrap._gcd_import(name[level:], package, level)
#   File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
#   File "<frozen importlib._bootstrap>", line 991, in _find_and_load
#   File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
# ModuleNotFoundError: No module named 'news'
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\NewsPaper> py manage.py makemigrations
# Migrations for 'news':
#   news\migrations\0001_initial.py
#     - Create model Author
#     - Create model Category
#     - Create model Post
#     - Create model PostCategory
#     - Add field postCategory to post
#     - Create model Comment
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\NewsPaper> py manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, news, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying news.0001_initial... OK
#   Applying sessions.0001_initial... OK
# (venv) PS C:\Users\Анастасия Лебедева\Desktop\Python\NewsPaper4\NewsPaper> py manage.py shell
# Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from news.models import *
# >>> u1 = User.objects.create_user(username='User1')
# >>> u1
# <User: User1>
# >>> u2 = User.objects.create_user(username='User2')
# >>> u2
# <User: User2>
# >>> Author.objects.create(authorUser=u1)
# <Author: Author object (1)>
# >>> Author.objects.create(authorUser=u2)
# <Author: Author object (2)>
# >>> Category.objects.create(name='IT')
# <Category: Category object (1)>
# >>> Category.objects.create(name='Животные')
# <Category: Category object (2)>
# >>> Category.objects.create(name='Растения')
# <Category: Category object (3)>
# >>> Category.objects.create(name='Насекомые')
# <Category: Category object (4)>
# >>> Post.objects.create(author=Author.objects.get(id=1), categoryType='NW', title='title1', text='text1')
# KeyboardInterrupt
# >>> Post.objects.create(author=Author.objects.get(id=1), categoryType='NW', title='title1', text='text1')
# <Post: Post object (1)>
# >>> Post.objects.create(author=Author.objects.get(id=1), categoryType='AR', title='title2', text='text2')
# <Post: Post object (2)>
# >>> Post.objects.create(author=Author.objects.get(id=2), categoryType='AR', title='title3', text='text3')
# <Post: Post object (3)>
# >>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
# >>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
# >>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
# >>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
# >>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='comment1')
# <Comment: Comment object (1)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='comment2')
# <Comment: Comment object (2)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='comment3')
# <Comment: Comment object (3)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='comment4')
# <Comment: Comment object (4)>
# >>> Comment.object.get(id=1).like()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: type object 'Comment' has no attribute 'object'
# >>> Comment.objects.get(id=1).like()
# >>> Comment.objects.get(id=2).like()
# >>> Comment.objects.get(id=3).like()
# >>> Comment.objects.get(id=4).like()
# >>> Comment.objects.get(id=1).like()
# >>> Comment.objects.get(id=1).dislike()
# >>> Comment.objects.get(id=1).rating
# 1
# >>> Post.objects.get(id=1).like()
# >>> Post.objects.get(id=2).like()
# >>> Post.objects.get(id=2).like()
# >>> Post.objects.get(id=3).like()
# >>> Author.objects.get(id=1).update_rating()
# >>> Author.objects.get(id=1).ratingAuthor
# 11
# >>> Author.objects.get(id=2).update_rating()
# >>> Author.objects.get(id=2).ratingAuthor
# 5
# >>> a = Author.objects.order_by('-ratingAuthor')[:1]
# >>> a
# <QuerySet [<Author: Author object (1)>]>
# >>> for i in a:
# ...     i.ratingAuthor
# ...     i.authorUser.username
# ...
# 11
# 'User1'
# >>> a = Post.objects.order_by('-rating')[:1]
# >>> a
# <QuerySet [<Post: Post object (2)>]>
# >>> for i in a:
# ...     i.rating
# ...     i.dateCreation
# ...     i.title
# ...     i.preview()
# ...     i.authorUser.username
# ...
# 2
# datetime.datetime(2022, 3, 27, 16, 36, 58, 440475, tzinfo=datetime.timezone.utc)
# 'title2'
# 'text2...'
# Traceback (most recent call last):
#   File "<console>", line 6, in <module>
# AttributeError: 'Post' object has no attribute 'authorUser'
# >>> for i in a:
# ...     i.commentUser.username
# ...
# Traceback (most recent call last):
#   File "<console>", line 2, in <module>
# AttributeError: 'Post' object has no attribute 'commentUser'
# >>> for i in a:
# ...     i.postUser.username
# ...
# Traceback (most recent call last):
#   File "<console>", line 2, in <module>
# AttributeError: 'Post' object has no attribute 'postUser'
# >>> bestPost=Post.objects.all().order_by('-rating')[0]
# >>> print('Автор лучшей статьи', bestPost.author.authorUser.username)
# Автор лучшей статьи User1
# >>> comments = bestPost.comment_set.all()
# >>> for c in comments:
# ...     c.text
# ...
# 'comment2'
# 'comment3'
# >>> for c in comments:
# ...     c.dateCreation
# ...     c.text
# ...     c.rating
# ...     c.commentUser
# ...
# datetime.datetime(2022, 3, 27, 18, 41, 54, 662654, tzinfo=datetime.timezone.utc)
# 'comment2'
# 1
# <User: User1>
# datetime.datetime(2022, 3, 27, 18, 42, 12, 38237, tzinfo=datetime.timezone.utc)
# 'comment3'
# 1
# <User: User2>
# >>>
