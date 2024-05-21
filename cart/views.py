from django.shortcuts import render,HttpResponseRedirect
from courses.models import Course
from .models import Cart,CartItem,Orders,OrderItem
from .forms import OrderForm
from razorpay import Client
import uuid
# Create your views here.
def add_to_cart(request,courseId):
	#fetching Course object with the help of id
	course = Course.courseManager.get(id=courseId)
	#fetch current login user
	user=request.user
	cart,created=Cart.objects.get_or_create(user=user)
	cartitem,created=CartItem.objects.get_or_create(cart=cart,courses=course)
	quantity=request.GET.get("quantity")
	cartitem.quantity+=int(quantity)
	cartitem.save()
	return HttpResponseRedirect("/courses")

# ------------------------------------------------
# View Cart
# -------------------------------------------------
def view_cart(request):
	cart,created=Cart.objects.get_or_create(user=request.user)
	cartitems = cart.cartitem_set.all()	
	total=0
	request.session['cart_id']=cart.id
	for cartitem in cartitems:
		total+=cartitem.quantity*cartitem.courses.course_price

	return render(request,"cart/cart.html",{"cartitems":cartitems,"total":total})

# ------------------------------------------------
# Remove Cart item from cart
# -------------------------------------------------

def delete_cartitem(request,cartItemId):
	cartitem = CartItem.objects.get(id = cartItemId)
	cartitem.delete()
	return HttpResponseRedirect("/cart")

# ------------------------------------------------
# Update Final Quantity
# -------------------------------------------------
def update_quantity(request,cartItemId):
	cartitem=CartItem.objects.get(id=cartItemId)
	cartitem.quantity=request.GET.get('quantity')
	cartitem.save()
	return HttpResponseRedirect("/cart")

def checkout(request):
	if request.method=='GET':
		data={'first_name':request.user.first_name,'last_name':request.user.last_name}
		form=OrderForm(initial=data)
		return render(request,"cart/checkout.html",{"form":form})
	if request.method=='POST':
		form=OrderForm(request.POST)
		order_id=uuid.uuid4().hex
		print(form.is_valid())
		if form.is_valid():
			order=Orders.objects.create(order_id=order_id,
						 user=request.user,
						 first_name=form.cleaned_data["first_name"],
						 last_name=form.cleaned_data["last_name"],
						 address_line_1=form.cleaned_data["address_line_1"],
						 address_line_2=form.cleaned_data["address_line_2"],
						 city=form.cleaned_data["city"],
						 state=form.cleaned_data["state"],
						 phoneno=form.cleaned_data["phoneno"]
						 )
			
			cart=Cart.objects.get(pk=request.session.get('cart_id'))
			for cartitem in cart.cartitem_set.all():
				OrderItem.objects.create(order=order,
							 			courses=cartitem.courses,
							 			quantity=cartitem.quantity
							 			)
			return HttpResponseRedirect("/cart/payment/"+order.order_id)
		
def payment(request,orderId):
	amount=0
	order=Orders.objects.get(order_id=orderId)
	for orderitem in order.orderitem_set.all():
		amount+=orderitem.courses.course_price*orderitem.quantity
		
	# ===============================
	# razor pay
	client=Client(auth=("rzp_test_JM3Z2yoL7rOls7","L6S69L0okABxAACBAnphj9UQ"))
	data={"amount":amount*100,"currency":"INR","receipt":orderId}
	payment=client.order.create(data=data)
	print(payment)
	return render(request,"cart/payment.html",{"amount":amount,"payment":payment})

