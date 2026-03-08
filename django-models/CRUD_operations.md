# CRUD Operations in Django Shell

This document demonstrates the Create, Retrieve, Update, and Delete operations performed on the **Book** model within the `bookshelf` app.

---

## Create
`from bookshelf.models import Book`  
`book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`  
`book`

**Expected Output:**
```
<Book: 1984 by George Orwell (1949)>
```

---

## Retrieve
`Book.objects.all()`

**Expected Output:**
```
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
```

---

## Update
`book = Book.objects.get(title="1984")`  
`book.title = "Nineteen Eighty-Four"`  
`book.save()`  
`book`

**Expected Output:**
```
<Book: Nineteen Eighty-Four by George Orwell (1949)>
```

---

## Delete
`book = Book.objects.get(title="Nineteen Eighty-Four")`  
`book.delete()`  
`Book.objects.all()`

**Expected Output:**
```
<QuerySet []>
```

---

## Summary
- **Create:** Added a new book instance.  
- **Retrieve:** Displayed the created book.  
- **Update:** Changed the title to *Nineteen Eighty-Four*.  
- **Delete:** Removed the book and confirmed deletion.  

All CRUD operations were successfully executed and documented.

