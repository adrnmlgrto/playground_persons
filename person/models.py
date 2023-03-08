from django.db import models


class Person(models.Model):
    f_name = models.CharField(max_length=30, verbose_name="First Name")
    m_name = models.CharField(max_length=30, blank=True, verbose_name="Middle Name")
    l_name = models.CharField(max_length=30, verbose_name="Last Name")

    def __str__(self):
        if self.m_name == "":
            return f'{self.l_name.upper()}, {self.f_name.upper()}'
        return f'{self.l_name.upper()}, {self.f_name.upper()} {self.m_name.upper()[0]}'
