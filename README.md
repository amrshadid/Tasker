# Welcome to Tasker!
Tasker is a collaboration tool that **organizes your projects into boards**
![](https://ibb.co/sJ2xLdX)

## To make system ready
you must install **Django** and make **environment** the work ready

-you must make migrate, go to path manage.py
> python manage.py migrate

-you need to install bootstrap 4
> pip install django-bootstrap4

-now run system
> python manage.py runserver

## You can visit demo web
[Tasker](http://amrshadid.pythonanywhere.com)


## UML diagrams

@startuml
graph LR
A[Dashboard]--> Add dashboard
Dashboard--> Dashboard list
Dashboard list-->Open dashboard
Dashboard list-->Setting dashboard
Setting dashboard -->Edit Member
Setting dashboard-->Delete dashboard
Open dashboard-->Ticket list
Ticket list-->Add ticket
Ticket list-->Manage ticket
Manage ticket-->Ticket details
Ticket details-->Add comments
@enduml
