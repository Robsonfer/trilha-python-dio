from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(f'Veja a data e hora de Oslo: {data}')
print(f'Veja a data e hora de SP: {data2}')
