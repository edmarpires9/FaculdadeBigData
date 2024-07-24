from datetime import datetime
data = datetime.now()
print(data)
print(f'{data:%d/%m/%Y}')