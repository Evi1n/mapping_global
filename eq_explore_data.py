import json


filename= 'data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)  # veri kümesinin tamamını all_eq_data da sakladık
    
all_eq_dicts = all_eq_data['features']  # features anahtarı ile ilişkili olan veriyi alırız ve all_eq_dicts te saklarız

mags, lons, lats = [], [], []  # deprem, enlem ve boylam büyüklüklerini saklamak için boş listeler
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # her bir depremin büyüklüğü mag anahtarı altında bu sözlüğün properties ksımında saklamaktadır.
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
      
print(mags[:10])
print(lons[:5])
print(lats[:5])

print(len(all_eq_dicts))  
    
    
readeble_file = 'data/readeble_eq_data.json' # aynı veriyi daha okunur yapmak için veriyi  bir dosya oluşturduk
with open(readeble_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)  # bu fonksiyon bir json veri nesnesi alır ve bir dosya nesnesi alır ve veriyi bu dosyaya yazar. 
    # indent veri yapısına uygun girintiyi kullanarak veriyi oluşturmasını sağlar.
    
    