#  pip install pytz types-pytz
from datetime import datetime

data_str_data = '2022/04/20 07:49:23'
# from pytz import timezone
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'


# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.now()
data = datetime.strptime(data_str_data, data_str_fmt)
print(data.timestamp())  # Isso está na base de dadosprint(data)
print(datetime.fromtimestamp(1670849077))
# data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)