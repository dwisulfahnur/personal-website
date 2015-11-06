from app import *
db.create_all()

title= raw_input('title: ')
author= 'Dwi Sulfahnur'
content= raw_input('content: ')
category_id = input('category_id: ')

input = Blog(title,author,content,category_id)
db.session.add(input)
db.session.commit()
