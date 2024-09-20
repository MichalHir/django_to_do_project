# my_tennis_club_django101

https://github.com/ranerlich7/my_tennis_club_django101


Homework: connect court and person
Let a person reserve a court
So reserve function should have a 2 select boxes of people that can reserve
# member1=models.ForeignKey(Member,on_delete=models.SET_NULL,related_name='courts', null=True,blank=True)
  # member2=models.ForeignKey(Member,on_delete=models.SET_NULL,related_name='courts', null=True,blank=True)


cls

Retrieve records where the join date field is within a specified date rangeMember.objects.filter(firstname__startswith='S').values()


Retrieve all records where the court is in the list [1,2,3]
Next lines - we can do it with court model. try also with member model
Retrieve all records where the court is occupied=true. 


python -m venv venv
.\venv\Scripts\activate
Pip install -r requirements.txt

Python manage.py runserver
Python manage.py shell