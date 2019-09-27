from django.db import models


class University(models.Model):
    univ_name = models.CharField(max_length=50)

    # class Meta:
    #     verbose_name = "University"
    #     verbose_name_plural = "Universities"
    #
    # def __unicode__(self):
    #     return self.univ_name


class Student(models.Model):
    rno = models.IntegerField(default=1000)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

      # return '% # class Meta:
    #     #     verbose_name = "Student"
    #     #     verbose_name_plural = "Students"
    #     #
    #     # def __unicode__(self):
    #     #  d%s%s%d' % (self.rno, self.first_name, self.last_name, self.age)







