# **Web Development Using Python**

A lot of people who try to learn Python are very much into backend web development and try to create something for their startups using frameworks like Django or Flask.

Here are a few tips coming from someone who's been doing exactly that for quite some time.

## **Choosing a Stack**

As I mentioned earlier, 2 good examples for easily creating the backend of your tech-based startup would probably be Flask or Django, but these 2 frameworks are different in many different ways.

1. **Size**

Flask is much smaller than Django to begin with, as Django is a includes more packages that influences the size of the module.

2. **Microservice vs Complex Application**

Flask is designed to be a web-facing component to serve a small "service" or a part of your tech stack, while Django includes many parts of your would be tech stack to deploy it all together at once.

For example at a large tech company, if you were to use Flask, you would be building small components of the tech stack at a time, like 1 for authentication, another for database communication and et cetera, while keeping functionality extensible through add ons.

While using Django, all these small services are integrated within Django, which allows robust and streamlined development of a full-fledged web application.

3. **Admin Interface**

Django includes an admin interface that allows developers to manage the web app database's contents, which makes it more favorable for content heavy applications. This functionality can be added into Flask as well, much like all of Django's, however native parts would *usually* perform better than third-party add-ons.

4. **Tooling**

Django comes with manage.py and django-admin which allows ways to manage your web app without having to set up many things on runtime, while Flask has the flask tool which is limited compared to Django's tools for deployment and management.

5. **Summary**

If you were to find yourself choosing between Flask and Django, you should ask yourself which parts you would be needing, and which parts you are more comfortable working with.

Personally I prefer Flask when I need to make something really fast to both provide a small application while having complete control over my front-end without having diskspace bloat on my back-end.

Both are good frameworks however, and each can do what the other can, where the main difference would be the experience of the developers themselves.