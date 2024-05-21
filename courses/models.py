from django.db import models

# Create your models here.
# ----------------------------------------------------------------
# Custom Manager (Course)
# ----------------------------------------------------------------
class CustomCourseManager(models.Manager):

    def get_queryset(self):
        return CourseQuerySet(self.model)
    
class CourseQuerySet(models.QuerySet):

    def range(self,start_price,end_price):
        return self.filter(course_price__range=(start_price,end_price))
    
    def search(self,keyword):
        return self.filter(course_name__icontains=keyword)
# =====================================================================
#   Tag Models
# =====================================================================

class Tag(models.Model):
    tag_name=models.CharField(max_length=50,blank=False)
    
    def __str__(self):
        return self.tag_name
# =====================================================================
#   Category Models
# =====================================================================

class Category(models.Model):
    category_name=models.CharField(max_length=50,blank=False)
    category_tag_id = models.ForeignKey(Tag,on_delete=models.PROTECT,null=True)
    
    def __str__(self):
        return self.category_name


    
# =====================================================================
#   Mentor Models
# =====================================================================

class Mentor(models.Model):
    mentor_name=models.CharField(max_length=70,default="")
    mentor_speciality=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    mentor_salary=models.PositiveIntegerField(default=0)
    mentor_schedule_time=models.CharField(max_length=50,default="")
    mentor_experience=models.CharField(max_length=50,default="")
    mentor_picture=models.ImageField(upload_to="mentor/",null=True)

    def __str__(self):
        return self.mentor_name
    

class Course(models.Model):
    course_name=models.CharField(max_length=70,default="")
    course_description=models.TextField(default="")
    course_price=models.PositiveIntegerField(default=0)
    # course_category=models.CharField(max_length=50,default="")
    mentor=models.ForeignKey(Mentor,on_delete=models.PROTECT,null=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    course_picture=models.ImageField(upload_to="course/",null=True)

    # Changing manager name(Product.productManger.all())
    courseManager=models.Manager()
    cm=CustomCourseManager()

    def __str__(self):
        return self.course_name