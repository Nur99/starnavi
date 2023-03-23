<h3 align="center">
Hi there, I'm Nurymzhan 👋
</h3>

<h2 align="center">
I'm a Software Engineer 💻, VideoMaker 📸, and Amateur Table Tennis player!
</h2> 

I love the entire process of implementing architectures, editing videos and algorithms and data structures. 

### 🤝 Connect with me:

<a href="https://www.linkedin.com/in/nurymzhan-ayapbergen-15582623a/"><img align="left" src="https://raw.githubusercontent.com/yushi1007/yushi1007/main/images/linkedin.svg" alt="Yu Shi | LinkedIn" width="21px"/></a>
</br>
- 💬 If you have any question/feedback, please do not hesitate to reach out to me!

## 🔭 I'm currently working on

- Remofirst
- Algorithms and data structures (Leetcode)

## 🌱 I'm currently learning

- 📱 React Native
- Devops (Kubernetes, AWS)
- FastAPI
- Adobe, CapCut  

## 📝 How I built this project

- Built with help of Django Framework. Used this [https://github.com/HackSoftware/Django-Styleguide](code style guide).
- Created a folder apps, divided apps inside them as users and posts. Kept API view side code in minimum lines. Implemented with service methods.
- Used JWT.
- Kept clean coding style with help of pre-commit.
- Added swagger documentation.
- Added Celery configurations for any possible future implementations. 
- Used PostgreSQL. 
- Added .gitignore to hide sensitive credentials (.env file, ...).
- Created a bot and kept it in fully separate format from Django. Used only SQL commands and only python default libraries.
- Added some activity function inside middleware.

## 📝 How to run Django project

- py

## 📝 How to run bot

- python bot.py number_of_users
- python bot.py max_posts_per_user
- python bot.py max_likes_per_user
- python bot.py signup_users N (N is a random integer number. You can create N users, then they will create K (0, max_posts_per_users) posts. New users will like new posts randomly. )
- the bot can work without docker, it is enough to create virtual environment and install requirements.txt, migration commands and just run commands above. it is enough to work with sqlite