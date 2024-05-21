from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
# Create your models here.

class Cart(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	courses=models.ManyToManyField(Course,through="CartItem")


class CartItem(models.Model):
	cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
	courses=models.ForeignKey(Course,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=0)

class Orders(models.Model):
	order_id=models.CharField(primary_key=True,max_length=40)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=100,default="")
	last_name=models.CharField(max_length=200,default="")
	address_line_1=models.TextField()
	address_line_2=models.TextField()
	city=models.CharField(max_length=100,default="")
	state=models.CharField(max_length=100,default="")
	phoneno=models.PositiveIntegerField(default=0)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
	order=models.ForeignKey(Orders,on_delete=models.CASCADE,default="")
	courses=models.ForeignKey(Course,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=0)
