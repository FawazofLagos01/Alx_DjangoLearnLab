# Django Permissions and Groups Setup

This document explains how custom permissions and groups are configured in this project as required in the task **"Managing Permissions and Groups in Django"**.

---

## 1. Custom Permissions (models.py)

Custom permissions were added inside the `Book` model:

```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("can_view", "Can View Book"),
            ("can_create", "Can Create Book"),
            ("can_edit", "Can Edit Book"),
            ("can_delete", "Can Delete Book"),
        ]
