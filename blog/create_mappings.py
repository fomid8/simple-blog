# اجرای این کد در یک اسکریپت جداگانه یا فایل management command
from .documents import UserDocument, CategoryDocument, ArticleDocument

def create_mappings():
    UserDocument.init()
    CategoryDocument.init()
    ArticleDocument.init()
    print("Mappings created successfully.")

# فراخوانی این تابع در مدیریت یا در جای دلخواه
create_mappings()
