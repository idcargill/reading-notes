# Djano Models

[Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)

## Fields

- CharField: Characters
- TextField: large arbitrary strings
- IntegerField: ints
- DateField: Datetime
- EmailField: unknown
- FileField: Files / Images
- AutoField: Automatic increments/ for primary key
- ForeignKey: id field from a relational model
- ManyToManyField: Specifies relationships

## Models

- class based
- common methods: \_\_str\_\_ and get_absolute_url
- Use models to perform CRUD (similar to mongoose)

- Model.objects.all()  Find all
- instance.save()
- Model.objects.filter(title__contains='something') filter search (dunder separates fields)

### Django Admin

[Django Admin](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)

- Register models with admin.py
  >admin.site.register(Model)
- Create superuser
- register models with admin/list display

```python
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'car')

  # Filter Views
  list_filter = ('status', 'food')

```

[A very annoying Guide to Django](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)
[less annoying Django blog](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)