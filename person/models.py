from django.db import models


class Person(models.Model):
    f_name = models.CharField(max_length=30, verbose_name="First Name")
    m_name = models.CharField(max_length=30,
                              blank=True, verbose_name="Middle Name")
    l_name = models.CharField(max_length=30,
                              verbose_name="Last Name")
    is_male = models.BooleanField(default=False)
    is_female = models.BooleanField(default=False)
    other = models.BooleanField(default=False,
                                verbose_name="Prefer not to say")

    def __str__(self):
        if self.m_name == "":
            return f'{self.l_name.upper()}, {self.f_name.upper()}'
        return (f'{self.l_name.upper()}, '
                f'{self.f_name.upper()}) '
                f'{self.m_name.upper()[0]}')
