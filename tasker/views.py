from django.shortcuts import render
from django.db import connection

def index(request):
    # Execute raw SQL query to fetch data from the contacts table
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        print(rows)
    # Pass the fetched data to the template for rendering
    context = {
        'contacts': rows
    }
    return render(request, 'index.html', context)
