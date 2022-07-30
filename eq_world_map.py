import json
from matplotlib.pyplot import title 

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename= 'data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)  # veri kümesinin tamamını all_eq_data da sakladık
    
all_eq_dicts = all_eq_data['features']  # features anahtarı ile ilişkili olan veriyi alırız ve all_eq_dicts te saklarız

mags, lons, lats, hover_texts = [], [], [], []  # deprem, enlem ve boylam büyüklüklerini saklamak için boş listeler
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # her bir depremin büyüklüğü mag anahtarı altında bu sözlüğün properties ksımında saklamaktadır.
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
    
    
readeble_file = 'data/readeble_eq_data.json' # aynı veriyi daha okunur yapmak için veriyi  bir dosya oluşturduk
with open(readeble_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)  # bu fonksiyon bir json veri nesnesi alır ve bir dosya nesnesi alır ve veriyi bu dosyaya yazar. 
    # indent veri yapısına uygun girintiyi kullanarak veriyi oluşturmasını sağlar.
    
#depremlerin haritasını çıkar.
# data = [Scattergeo(lon=lons, lat=lats)] # scatter nesnesini liste içinde oluşturduk çünkü oluşturulan
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text': hover_texts, 
    'marker' : {'size': [5*mag for mag in mags],
    'color' : mags,
    'colorscale' : 'Viridis',
    'reversescale' : True,
    'colorbar': {'title': 'Magnitude'}
    },
    }]
# herhangi bir görselleştirme üzerinde birden fazla veri kümesi işleyebiliriz.
my_layout = Layout(title='Global Earthquakes')


fig = {'data': data, 'layout': my_layout} # veri yerleşimi olan bir sözlük oluşturduk
offline.plot(fig, filename='global_earthquakes.html')