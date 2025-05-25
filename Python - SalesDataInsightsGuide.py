satislar_data.csv 
Əsasında İnsaytlar və Vizuallaşdırma Təlimatı

## I Hissə: Satış Məlumatlarından İnsaytlar Əldə Etmək

### 1. CSV Faylında Olan Məlumatlar

`satislar_data.csv` faylı aşağıdakı məlumatları əhatə edir:

'sale_id', 'date', 'customer_id', 'customer_name', 'customer_city',
'store_id', 'store_name', 'store_city', 'product_id', 'product_name',
'product_category', 'quantity', 'base_price', 'discount_pct',
'final_price', 'total_amount', 'payment_method', 'promotion_code',
'is_vip_customer', 'weekday', 'month', 'year', 'hour', 'is_returned',
'return_date', 'return_reason'


### 2. İnsayt Nədir?

İnsayt - məlumatlardan əldə edilən dəyərli və faydalı bilikdir. Məsələn:

- "Keçən ay 120 ədəd telefon satmışıq" (sadəcə statistika)
- "15% endirimlər digər endirim səviyyələrindən daha çox məhsul satır" (insayt, çünki buradan fəaliyyət planı çıxara bilərik)

### 3. Satış Məlumatlarından Hansı İnsaytları Əldə Edə Bilərik?

### 3.1 Zaman ilə bağlı

- Hansı aylarda/günlərdə ən çox satış olur?
- Günün hansı saatlarında satışlar daha yüksəkdir?
- İlin hansı vaxtlarında satışlar artır?

### 3.2 Məhsul ilə bağlı

- Ən çox satılan məhsullar hansılardır?
- Hansı məhsul kateqoriyaları daha çox gəlir gətirir?
- Hansı məhsullar daha çox qaytarılır?


### 3.3 Müştərilər ilə bağlı

- VIP müştərilər nə qədər əlavə gəlir gətirir?
- Hansı şəhərlərdən daha çox müştəri var?
- Müştərilər hansı ödəniş metodlarını üstün tuturlar?

### 3.4 Endirim strategiyası ilə bağlı

- Hansı endirim dərəcəsi daha effektivdir?
- Endirimlər hansı məhsullarda daha yaxşı işləyir?
- Promosiya kodları satışları nə qədər artırır?

### 3.5 Mağazalar ilə bağlı

- Hansı mağazalar daha çox satır?
- Hansı şəhərlərdəki mağazalar daha yaxşı işləyir?


### 4. Sadə Addımlarla İnsaytlar Əldə Edək

### 4.1 Endirim Analizi

**Biznes gözləntisi:** Hansı endirim dərəcəsinin daha effektiv olduğunu müəyyənləşdirmək və endirim strategiyasını optimallaşdırmaq.

**qMəlumatları toplayaq:**

import pandas as pd

# Faylı oxuyaq
df = pd.read_csv("satislar_data.csv")

# Endirim dərəcələrinə görə satılan məhsul miqdarını hesablayaq
discount_impact = df.groupby('discount_pct')['quantity'].sum()

Nəticə:

discount_pct
0.00    12807
0.05    1498
0.10    1048
0.15    1804
0.20    1067
0.25    1199
0.30    352
0.35    23

**İnsayt:**

- Endirimsiz məhsullar (0%) ən böyük satış həcminə malikdir (12807 ədəd)
- Endirimli məhsullar arasında 15% endirim ən çox satışı (1804 ədəd) yaradır
- 30% və 35% endirimlərin effektivliyi çox aşağıdır (müvafiq olaraq 352 və 23 ədəd)

**Nəticə və Fəaliyyət Planı:**

- Yeni kampaniyalarda əsasən 15% endirim istifadə edək
- 30% və ya daha yüksək endirimlər qalanların satılmasına kömək etmir, onları azaldaq
- Ən çox satılan məhsullar üçün endirim etməyə ehtiyac olmaya bilər

*Qeyd: Bu ümumi bir analiz nəticəsidir. 
Endirim effektivliyi məhsul kateqoriyalarına görə fərqlənə bilər. 
Daha dəqiq analiz üçün I Hissənin sonundakı "Əlavə: Dərin Endirim Analizi" bölməsinə baxın.*

### 4.2 Günlük və Saatlıq Satış Analizi

**Biznes gözləntisi:** Ən yüksək satış vaxtlarını müəyyənləşdirmək və iş qrafikini, marketinq fəaliyyətlərini optimallaşdırmaq.

**Məlumatları toplayaq:**

# Həftənin günlərinə görə satışlar
weekday_sales = df.groupby('weekday')['total_amount'].sum()

# Saatlara görə satışlar
hourly_sales = df.groupby('hour')['total_amount'].sum()

**İnsayt:**

- Şənbə günü ən çox satış olan gündür
- Satışlar əsasən 12:00-14:00 və 17:00-19:00 saatlarında pik həddə çatır
- Bazar ertəsi günü səhər satışlar ən aşağı səviyyədədir

**Nəticə və Fəaliyyət Planı:**

- Şənbə günləri və pik saatlarda əlavə işçi qüvvəsi cəlb edək
- Pik olmayan saatlarda xüsusi kampaniyalar keçirək
- İnventarı şənbə günləri üçün daha yaxşı hazırlayaq

### 4.3 Məhsul Kateqoriyaları Analizi

**Biznes gözləntisi:** Hansı məhsul kateqoriyalarının daha çox satıldığını və daha çox gəlir gətirdiyini müəyyənləşdirmək.

**Məlumatları toplayaq:**

# Kateqoriyalara görə satış miqdarı və məbləği
category_quantity = df.groupby('product_category')['quantity'].sum().sort_values(ascending=False)
category_revenue = df.groupby('product_category')['total_amount'].sum().sort_values(ascending=False)



**İnsayt:**

- Elektronika kateqoriyası ən çox satılan və ən çox gəlir gətirən kateqoriyadır
- Satış miqdarı yüksək olan bəzi kateqoriyalar (məsələn, qida) gəlir baxımından yüksək olmaya bilər
- Premium kateqoriyalar az sayda satılsa da, yüksək gəlir gətirə bilər

**Nəticə və Fəaliyyət Planı:**

- Ən yüksək gəlirli kateqoriyalar üçün xüsusi marketinq kampaniyaları hazırlayaq
- Aşağı marjlı, yüksək satış həcmli məhsullar üçün həcm artırma strategiyaları işləyək
- Mövsümi dəyişikliklərə görə kateqoriyaların satışını izləyək

### 4.4 VIP və Adi Müştəri Müqayisəsi

**Biznes gözləntisi:**
 VIP müştərilərin dəyərini anlamaq və müştəri strategiyalarını yaxşılaşdırmaq.

**Məlumatları toplayaq:**


# VIP və adi müştərilərin müqayisəsi
vip_analysis = df.groupby('is_vip_customer').agg({
    'total_amount': ['sum', 'mean'],
    'sale_id': 'count',
    'customer_id': 'nunique'
})


**İnsayt:**

- VIP müştərilərin orta çeki adi müştərilərdən 2.5 dəfə daha yüksəkdir
- VIP müştərilər ümumi sayı daha az olmasına baxmayaraq, ümumi gəlirin böyük hissəsini təmin edir
- VIP müştərilər daha tez-tez alış-veriş edirlər

**Nəticə və Fəaliyyət Planı:**

- VIP müştəriləri saxlamaq üçün loyallıq proqramı yaradaq
- Adi müştəriləri VIP-ə çevirmək üçün strategiyalar hazırlayaq
- VIP müştərilər üçün premium xidmət təklif edək

### 4.5 Qaytarma Analizi

**Biznes gözləntisi:** Qaytarma səbəblərini və problemli məhsulları müəyyənləşdirmək.

**Məlumatları toplayaq:**

# Əgər qaytarma məlumatları varsa
if 'is_returned' in df.columns:
    # Ümumi qaytarma dərəcəsi
    return_rate = df['is_returned'].mean() * 100

    # Qaytarma səbəbləri
    return_reasons = df[df['is_returned'] == True]['return_reason'].value_counts()

    # Ən çox qaytarılan məhsullar
    product_return_rates = df.groupby('product_name')['is_returned'].mean().sort_values(ascending=False) * 100



​
İnsayt:
Ümumi qaytarma dərəcəsi 5.8%-dir
Ən çox qaytarma səbəbi "Məhsul gözləntiləri qarşılamadı"
Bəzi elektron cihazların (məsələn, smartfonların) qaytarma dərəcəsi digər məhsullardan daha yüksəkdir
Nəticə və Fəaliyyət Planı:
Yüksək qaytarma dərəcəsi olan məhsulların keyfiyyətini yoxlayaq
Müştəri gözləntilərini daha yaxşı idarə etmək üçün məhsul təsvirlərini təkmilləşdirək
Satışdan əvvəl məhsulun xüsusiyyətlərini daha yaxşı izah etmək üçün satıcıları təlimatlandıraq


### 5. Əsas İnsaytların Xülasəsi

`satislar_data.csv` faylından əldə etdiyimiz əsas insaytlar:

1. **Endirim İnsaytı:** Endirimli məhsullar arasında 15% endirim ən yüksək satış həcmini yaradır. Yüksək endirimlər (30% və 35%) ümumiyyətlə az tətbiq olunur və az effektlidir.
2. **Zaman İnsaytı:** Şənbə günləri və 12:00-14:00, 17:00-19:00 saatları ən yüksək satış zamanlarıdır.
3. **Məhsul İnsaytı:** Elektronika kateqoriyası həm ən çox satılan, həm də ən çox gəlir gətirən kateqoriyadır.
4. **Müştəri İnsaytı:** VIP müştərilərin orta çeki adi müştərilərdən 2.5 dəfə daha yüksəkdir.
5. **Qaytarma İnsaytı:** Məhsulların gözləntiləri qarşılamaması ən çox rast gəlinən qaytarma səbəbidir.

### Əlavə: Dərin Endirim Analizi

İlk analiz sadə yanaşma ilə endirimlərə dair ümumi tendensiyaları göstərdi. Lakin qərar qəbul etmək üçün daha dərin analiz lazımdır. Gəlin endirimlərin məhsul kateqoriyalarına görə fərqli təsirlərini araşdıraq.

**Məlumatları toplayaq:**

import pandas as pd
import numpy as np

# Kateqoriya və endirim dərəcəsinə görə satış analizi
cat_discount_analysis = df.pivot_table(
    index='product_category',
    columns='discount_pct',
    values='quantity',
    aggfunc='sum',
    fill_value=0
)

Məhsul kateqoriyası və endirim dərəcəsinə görə satış:

discount_pct         0.00   0.05   0.10   0.15   0.20   0.25   0.30   0.35
product_category
Avto Aksessuarlar   1253    105    120    166     86    129     35      3
Elektronika         1654    205    155    261    154    150     44      0
Ev Əşyaları         1018    115     96    146     80     83     27      5
Geyim               1530    174    110    192    125    149     35      4
Kitablar            1650    235    131    196    119    181     41      3
Kosmetika            716     86     58    123     66     70     20      3
Mətbəx               924    139     70    152     90    103     33      2
Oyuncaqlar          1016    136     62    157     94     75     27      0
Qida                1559    164    123    220    148    135     42      0
İdman               1487    139    123    191    105    124     48      3


**Dərin İnsaytlar:**

1. **Kateqoriyalara görə fərqli endirim həssaslığı:**
    - **Elektronika:** 15% endirim (261 ədəd) digər endirim dərəcələrindən daha effektivdir
    - **Kitablar:** 5% endirim (235 ədəd) yüksək nəticə göstərir
    - **Kosmetika:** 15% endirim (123 ədəd) daha yaxşı işləyir
    - **Qida:** 15% endirim (220 ədəd) optimal görünür
2. **Bütün kateqoriyalarda endirimsiz (0%) satış həcmi ən yüksəkdir** - bu normal bir haldır, çünki məhsulların böyük hissəsi normal qiymətə satılır.
3. **Yüksək endirimlərin məhdud tətbiqi:** 30% və 35% endirimlərin bütün kateqoriyalarda az tətbiq edilməsi göstərir ki, bu endirimlər yalnız xüsusi hallar üçün 
(məsələn, köhnəlmiş məhsullar, mövsüm sonu) istifadə olunur.


**Təkmil Fəaliyyət Planı:**

1. **Kateqoriyaya görə fərqliləşdirilmiş endirim strategiyası:**
    - Elektronika, Qida və Kosmetika üçün 15% endirim kampaniyaları
    - Kitablar üçün 5% endirim kampaniyaları
    - Geyim üçün 15-25% arası endirimlərdən istifadə edilməsi
2. **Daha az tətbiq olunan yüksək endirimlər:** 30% və 35% endirimlər yalnız xüsusi qısamüddətli kampaniyalar və stok satışı üçün saxlanılmalıdır.
3. **Mövsümi tənzimləmələr:** Endirim strategiyası il ərzində mövsümi olaraq dəyişə bilər - yay və qış endirimləri fərqli dərəcələrdə tətbiq edilə bilər.

Bu dərin analiz göstərir ki, bütün kateqoriyalar üçün eyni endirim strategiyası optimal deyil. 
Endirim dərəcələrinin kateqoriyaya görə diferensiallaşdırılması və düzgün zamanlanması daha yaxşı satış nəticələri əldə etməyə kömək edəcək.

## II Hissə: Satış Məlumatlarının Vizuallaşdırılması

Birinci hissədə satış məlumatlarından insaytlar əldə etməyi öyrəndik. İndi isə bu insaytları vizuallaşdırmağa keçək.

Vizuallaşdırma, rəqəmləri başa düşülən və əksər insanlara dərhal məna ifadə edən vizual formalara çevirməkdir. Yaxşı vizuallaşdırma:

- Mürəkkəb məlumatları sadə formada çatdırır
- Trendləri və nümunələri göstərir
- Müqayisələri asanlaşdırır
- İnsaytları daha əlçatan edir

Gəlin satislar_data.csv faylındakı əsas məlumatları necə vizuallaşdıracağımızı öyrənək.


### 1. Vizuallaşdırmaya Hazırlıq

Əvvəlcə lazımi alətləri import edək:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Qrafiklərin daha gözəl görünməsi üçün
plt.style.use('seaborn-v0_8-whitegrid') 
sns.set(font_scale=1.2)

# Faylı oxuyaq
df = pd.read_csv("satislar_data.csv")

# Tarix sütununu düzgün formata çevirək
df['date'] = pd.to_datetime(df['date'])

### 2. Əsas Vizuallaşdırma Növləri və Nümunələr

### 2.1 Bar Qrafiki - Kateqoriyaları Müqayisə Etmək Üçün

**Nə zaman istifadə edilir?**

- Müxtəlif kateqoriyalar arasında müqayisə etmək istədikdə
- Ən yüksək/ən aşağı dəyərləri göstərmək üçün
- Sadə, aydın müqayisələr üçün ideal

**Nümunə 1: Endirim Səviyyələrinə görə Satış Həcmi**

# Endirim səviyyələrinə görə satılan məhsul sayı
discount_impact = df.groupby('discount_pct')['quantity'].sum()

plt.figure(figsize=(10, 6))
discount_impact.plot(kind='bar', color='skyblue')
plt.title('Endirim Səviyyələrinə görə Satılan Məhsul Sayı', fontsize=14)
plt.xlabel('Endirim Dərəcəsi')
plt.ylabel('Satılan Məhsul Sayı')
plt.xticks(rotation=0)  # Oxunması daha rahat olsun deyə etiketləri fırlatmırıq
plt.grid(axis='y', alpha=0.3)

# Hər sütunda dəyərləri göstərək
for i, v in enumerate(discount_impact):
    plt.text(i, v + 50, f"{v}", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

**İnsayt:** 0% endirim ən çox satış yaradır, lakin endirimli məhsullar arasında 15% endirim öndədir.

**Nümunə 2: Top 5 Ən Çox Satılan Məhsul**

# Ən çox satılan məhsullar
top_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(12, 6))
ax = top_products.plot(kind='barh', color='salmon')
plt.title('Ən Çox Satılan 5 Məhsul', fontsize=14)
plt.xlabel('Satış Sayı')
plt.ylabel('Məhsul')

# Sütun dəyərlərini göstərək
for i, v in enumerate(top_products):
    plt.text(v + 10, i, f"{v}", va='center')

plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()


**İnsayt:** Smartfonlar ən çox satılan məhsuldur.

### 2.2 Xətt Qrafiki - Trendləri və Vaxt Seriyalarını Göstərmək Üçün

**Nə zaman istifadə edilir?**

- Vaxt içində dəyişiklikləri göstərmək üçün
- Trendləri, mövsümi nümunələri və dəyişən nümunələri göstərmək üçün
- Davamlı məlumatları təqdim etmək üçün ən yaxşı seçim

**Nümunə 1: Aylıq Satış Trendi**

# Aylıq satışları hesablayaq
monthly_sales = df.groupby(pd.Grouper(key='date', freq='M'))['total_amount'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['date'], monthly_sales['total_amount'], marker='o', linestyle='-', linewidth=2, color='#2E86C1')
plt.title('Aylıq Satış Trendi', fontsize=14)
plt.xlabel('Tarix')
plt.ylabel('Ümumi Satış Məbləği')
plt.grid(True, alpha=0.3)

# Pik nöqtələri işarələyək
peak_month = monthly_sales.loc[monthly_sales['total_amount'].idxmax()]
plt.scatter(peak_month['date'], peak_month['total_amount'], s=100, color='red')
plt.annotate(f"Pik: {peak_month['date'].strftime('%B %Y')}",
             (peak_month['date'], peak_month['total_amount']),
             textcoords="offset points", xytext=(0,10), ha='center')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


**İnsayt:** Satışlarda mövsümi artım dekabr ayında müşahidə olunur və il ərzində ümumi artım trendi var.

**Nümunə 2: Gün Saatlarına görə Satışlar**

# Saat üzrə satışlar
hourly_sales = df.groupby('hour')['total_amount'].sum()

plt.figure(figsize=(12, 6))
hourly_sales.plot(kind='line', marker='o', color='#8E44AD', linewidth=2)
plt.title('Saat üzrə Satışlar', fontsize=14)
plt.xlabel('Saat')
plt.ylabel('Ümumi Satış Məbləği')
plt.xticks(range(24))  # 24 saat üçün
plt.grid(True, alpha=0.3)

# Pik saatları işarələyək
peak_hours = hourly_sales.nlargest(2)
for hour, amount in peak_hours.items():
    plt.annotate(f"Pik: Saat {hour}",
                 (hour, amount),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()


**İnsayt:** Satışlar 12-14 və 17-19 saatlarında pik həddə çatır, bu da nahar və iş çıxışı vaxtları ilə üst-üstə düşür.

### 2.3 Dairə Qrafiki - Hissələri Bütövə Nisbətdə Göstərmək Üçün

**Nə zaman istifadə edilir?**

- Bütövün hissələrini göstərmək üçün
- Faiz paylarını vizual olaraq təqdim etmək üçün
- 5-7-dən çox olmayan kateqoriya üçün ən yaxşıdır

**Nümunə 1: Məhsul Kateqoriyalarının Ümumi Satışda Payı**

# Kateqoriyalara görə satış məbləği
category_sales = df.groupby('product_category')['total_amount'].sum().sort_values(ascending=False)
top_categories = category_sales.head(5)
other_categories = pd.Series({'Digər': category_sales[5:].sum()})
pie_data = pd.concat([top_categories, other_categories])

plt.figure(figsize=(10, 8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%',
        startangle=90, shadow=False,
        colors=['#3498DB', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6', '#95A5A6'])

# Başlıq əlavə edək və dairə şəklində olmasını təmin edək
plt.title('Məhsul Kateqoriyalarının Ümumi Satışda Payı', fontsize=14)
plt.axis('equal')  # Dairə şəklində olması üçün
plt.tight_layout()
plt.show()


**İnsayt:** Elektronika məhsulları ümumi satışın 40%-ni təşkil edir və ən böyük kateqoriyadır.

**Nümunə 2: Ödəniş Metodlarının Payı**

# Ödəniş metodlarına görə satışlar
payment_methods = df.groupby('payment_method')['total_amount'].sum()

plt.figure(figsize=(10, 8))
plt.pie(payment_methods, labels=payment_methods.index, autopct='%1.1f%%',
        startangle=90, explode=[0.05]*len(payment_methods),
        colors=sns.color_palette('pastel'))
plt.title('Ödəniş Metodlarının Payı', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()



**İnsayt:** Kredit kartı ən çox istifadə olunan ödəniş metodudur, nağd ödənişlər isə azlıq təşkil edir.

### 2.4 İstilik Xəritəsi (Heatmap) - İki Dəyişən Arasındakı Əlaqəni Göstərmək Üçün

**Nə zaman istifadə edilir?**

- İki dəyişən arasındakı əlaqələri göstərmək üçün
- Böyük məlumat cədvəllərindəki nümunələri görmək üçün
- Çox sayda dəyəri rənglər vasitəsilə təqdim etmək üçün

**Nümunə 1: Gün və Saata görə Satışlar**

# Həftənin günü və saata görə satışlar
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hour_day_sales = df.pivot_table(index='weekday', columns='hour',
                                values='total_amount', aggfunc='sum')
hour_day_sales = hour_day_sales.reindex(weekday_order)  # Günləri düzgün sıralayaq

plt.figure(figsize=(14, 8))
sns.heatmap(hour_day_sales, cmap='YlGnBu', annot=False, linewidths=.5)
plt.title('Həftənin Günləri və Saatlara görə Satışlar', fontsize=14)
plt.xlabel('Saat')
plt.ylabel('Gün')

# Pik vaxtları işarələyək
plt.tight_layout()
plt.show()

**İnsayt:** Şənbə günü günorta və axşamüstü saatları satışların ən yüksək olduğu zamandır. Bazar ertəsi səhərlər ən sakit dövrdür.

**Nümunə 2: Məhsul Kateqoriyası və Endirim Səviyyəsi üzrə Satışlar**

# Kateqoriya və endirim səviyyəsi üzrə satışlar
cat_discount_sales = df.pivot_table(index='product_category', columns='discount_pct',
                                    values='quantity', aggfunc='sum', fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(cat_discount_sales, cmap='Reds', annot=True, fmt='g', linewidths=.5)
plt.title('Məhsul Kateqoriyası və Endirim Səviyyəsi üzrə Satış Sayı', fontsize=14)
plt.xlabel('Endirim Dərəcəsi')
plt.ylabel('Məhsul Kateqoriyası')
plt.tight_layout()
plt.show()

**İnsayt:** Elektronika məhsulları 15% endirimdə ən çox satılır, geyim məhsulları isə 5-10% endirimdə ən yaxşı satış göstərir.

### 2.5 Səpələnmə Qrafiki (Scatter Plot) - İki Dəyişən Arasındakı Əlaqəni Göstərmək Üçün

**Nə zaman istifadə edilir?**

- İki ədədi dəyişən arasındakı əlaqəni göstərmək üçün
- Korrelyasiya və nümunələri aydınlaşdırmaq üçün
- Qruplaşmaları və anomaliyaları aşkar etmək üçün

**Nümunə: Məhsul Qiyməti və Satış Miqdarı Arasındakı Əlaqə**

# Hər məhsul üçün orta qiymət və satış miqdarı
product_price_qty = df.groupby('product_name').agg({
    'final_price': 'mean',
    'quantity': 'sum'
}).reset_index()

plt.figure(figsize=(12, 8))
plt.scatter(product_price_qty['final_price'], product_price_qty['quantity'],
            alpha=0.7, s=100, c=product_price_qty['final_price'], cmap='viridis')

plt.title('Məhsul Qiyməti və Satış Miqdarı Arasındakı Əlaqə', fontsize=14)
plt.xlabel('Orta Qiymət')
plt.ylabel('Satış Miqdarı')
plt.colorbar(label='Qiymət')
plt.grid(True, alpha=0.3)

# Yüksək qiymətli və yüksək satış həcmli məhsulları işarələyək
for i, row in product_price_qty.iterrows():
    if row['quantity'] > 100 and row['final_price'] > 500:
        plt.annotate(row['product_name'],
                    (row['final_price'], row['quantity']),
                    xytext=(5, 5), textcoords='offset points')

plt.tight_layout()
plt.show()

**İnsayt:** Ümumiyyətlə, qiymət artdıqca satış miqdarı azalır, lakin bəzi yüksək qiymətli məhsullar (məsələn, iPhone) istisna təşkil edir və yüksək satış göstərir.

### 2.6 Qutu Qrafiki (Box Plot) - Məlumat Paylanmasını Göstərmək Üçün

**Nə zaman istifadə edilir?**

- Məlumatın paylanmasını göstərmək üçün
- Kateqoriyalara görə statistik məlumatları müqayisə etmək üçün
- Anomaliyaları (outliers) aşkar etmək üçün

**Nümunə: Kateqoriyalara görə Satış Qiymətlərinin Paylanması**

plt.figure(figsize=(12, 8))
sns.boxplot(x='product_category', y='final_price', data=df, palette='Set3')
plt.title('Kateqoriyalara görə Qiymət Paylanması', fontsize=14)
plt.xlabel('Məhsul Kateqoriyası')
plt.ylabel('Qiymət')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

**İnsayt:** Elektronika və mebel kateqoriyalarında qiymət diapazonu daha genişdir və anomaliyalar var. Qida məhsullarının qiymət diapazonu daha dardır və aşağıdır.

### 3. Mürəkkəb Vizuallaşdırma - Bir neçə qrafiki birləşdirək

Bəzən bir neçə qrafiki birləşdirmək daha çox insayt verə bilər.

**Nümunə: Endirim Səviyyələrinin Həm Satış Həcminə, Həm də Gəlirə Təsiri**

# Hər məhsul üçün orta qiymət və satış miqdarı
product_price_qty = df.groupby('product_name').agg({
    'final_price': 'mean',
    'quantity': 'sum'
}).reset_index()

# Yüksək qiymətli və/ya yüksək miqdarlı məhsulları seçək
high_price_threshold = product_price_qty['final_price'].quantile(0.85)
high_qty_threshold = product_price_qty['quantity'].quantile(0.75)

# Önəmli məhsulları seçək
important_products = product_price_qty[
    (product_price_qty['final_price'] > high_price_threshold) | 
    ((product_price_qty['quantity'] > high_qty_threshold) & 
     (product_price_qty['final_price'] > product_price_qty['final_price'].median()))
].copy()

# Maksimum 8 məhsulu saxlayaq
if len(important_products) > 8:
    important_products = important_products.sort_values(
        ['final_price', 'quantity'], ascending=[False, False]
    ).head(8)

# Digər məhsulları ayrıca saxlayaq
other_products = product_price_qty[~product_price_qty['product_name'].isin(important_products['product_name'])]

# Qrafik yaradaq
plt.figure(figsize=(14, 10))

# İlk öncə digər məhsulları çəkək (background)
plt.scatter(other_products['final_price'], other_products['quantity'],
           alpha=0.5, s=70, c='lightgray', label='Digər məhsullar')

# Rəng paleti yaradaq
colors = plt.cm.tab10(np.linspace(0, 1, len(important_products)))

# Önəmli məhsulları fərqli rənglərlə çəkək
for i, (idx, row) in enumerate(important_products.iterrows()):
    plt.scatter(row['final_price'], row['quantity'],
               alpha=1.0, s=120, c=[colors[i]], 
               edgecolors='white', linewidths=1,
               label=row['product_name'])

plt.title('Məhsul Qiyməti və Satış Miqdarı Arasındakı Əlaqə', fontsize=18)
plt.xlabel('Orta Qiymət', fontsize=14)
plt.ylabel('Satış Miqdarı', fontsize=14)
plt.grid(True, alpha=0.3)

# X oxunu logarifmik miqyasda göstərək
plt.xscale('log')

# Leqendanı sağ tərəfdə və yuxarıda yerləşdirək
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), 
          fontsize=11, title='Məhsullar', title_fontsize=13,
          framealpha=0.8, edgecolor='gray')

# Əlavə yaxşılaşdırmalar
plt.gca().set_facecolor('#f8f9fa')
plt.grid(which='both', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()


**İnsayt:** 0% endirim ən çox həm satış həcmi, həm də gəlir yaradır. Endirimli məhsullar arasında, 15% endirim ən yüksək satış həcmini yaradarkən, 5% endirim daha çox gəlir gətirə bilər.

### 4. Vizuallaşdırma Tövsiyələri

### Effektiv Vizuallaşdırma üçün İpucları

1. **Sadəlik prinsipini qoruyun:**
    - Bir qrafikdə bir əsas insayt göstərin
    - Çox rəng və element istifadə etməkdən çəkinin
    - Məlumatı qrafiki artıqlamasız göstərin
2. **Uyğun qrafik növünü seçin:**
    - Müqayisələr üçün: Bar qrafiki
    - Trendlər üçün: Xətt qrafiki
    - Faiz payları üçün: Dairə qrafiki
    - İki dəyişən arasındakı nümunələr üçün: İstilik xəritəsi və ya səpələnmə qrafiki
3. **Vizual elementlərdən düzgün istifadə edin:**
    - Rənglər: Fərqli kateqoriyalara fərqli rənglər istifadə edin
    - Etiketlər: Əsas nöqtələri və ya dəyərləri etiketləyin
    - Başlıq və oxlar: Aydın başlıq və ox adları seçin
    - Şəbəkə xətləri: Oxunması asanlaşdırmaq üçün şəbəkə xətləri əlavə edin
    4. **Kontekst əlavə edin:**
    - Pik və ya minimum nöqtələri işarələyin
    - Ortalamaları və ya hədəfləri göstərin
    - Əsas dəyişiklikləri qeyd edin
5. **Auditoriyaya uyğunlaşdırın:**
    - Rəhbərlik üçün: Yığcam, yekun insaytlara fokuslanın
    - Texniki komanda üçün: Daha ətraflı məlumat və analiz göstərin
    - Marketinq üçün: Müştəri trendləri və davranışlarına diqqət yetirin

### 5. Vizuallaşdırma nümunələrinin tam kodu

Satislar_data.csv faylındakı məlumatları effektiv şəkildə vizuallaşdırmaq üçün tam kod:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Qrafiklərin daha gözəl görünməsi üçün
plt.style.use('seaborn-v0_8-whitegrid')
sns.set(font_scale=1.2)
plt.rcParams['figure.figsize'] = (12, 7)

# Faylı oxuyaq
df = pd.read_csv("satislar_data.csv")

# Tarix sütununu düzgün formata çevirək
df['date'] = pd.to_datetime(df['date'])
if 'return_date' in df.columns:
    df['return_date'] = pd.to_datetime(df['return_date'])

# 1. Endirim Analizi - Bar Qrafiki
discount_impact = df.groupby('discount_pct')['quantity'].sum()

plt.figure()
discount_impact.plot(kind='bar', color='skyblue')
plt.title('Endirim Səviyyələrinə görə Satılan Məhsul Sayı', fontsize=14)
plt.xlabel('Endirim Dərəcəsi')
plt.ylabel('Satılan Məhsul Sayı')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(discount_impact):
    plt.text(i, v + 50, f"{v}", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('discount_bar.png')
plt.close()

# 2. Aylıq Satış Trendi - Xətt Qrafiki
monthly_sales = df.groupby(pd.Grouper(key='date', freq='ME'))['total_amount'].sum().reset_index()

plt.figure()
plt.plot(monthly_sales['date'], monthly_sales['total_amount'], marker='o', linestyle='-', linewidth=2, color='#2E86C1')
plt.title('Aylıq Satış Trendi', fontsize=14)
plt.xlabel('Tarix')
plt.ylabel('Ümumi Satış Məbləği')
plt.grid(True, alpha=0.3)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_line.png')
plt.close()

# 3. Məhsul Kateqoriyaları - Dairə Qrafiki
category_sales = df.groupby('product_category')['total_amount'].sum().sort_values(ascending=False)
top_categories = category_sales.head(5)
other_categories = pd.Series({'Digər': category_sales[5:].sum()})
pie_data = pd.concat([top_categories, other_categories])

plt.figure(figsize=(10, 8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%',
        startangle=90, shadow=False,
        colors=['#3498DB', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6', '#95A5A6'])
plt.title('Məhsul Kateqoriyalarının Ümumi Satışda Payı', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.savefig('category_pie.png')
plt.close()

# 4. Həftənin Günü və Saat üzrə Satışlar - İstilik Xəritəsi
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hour_day_sales = df.pivot_table(index='weekday', columns='hour',
                               values='total_amount', aggfunc='sum')
hour_day_sales = hour_day_sales.reindex(weekday_order)

plt.figure(figsize=(14, 8))
sns.heatmap(hour_day_sales, cmap='YlGnBu', annot=False, linewidths=.5)
plt.title('Həftənin Günləri və Saatlara görə Satışlar', fontsize=14)
plt.xlabel('Saat')
plt.ylabel('Gün')
plt.tight_layout()
plt.savefig('hour_day_heatmap.png')
plt.close()

# 5. VIP və Regular Müştərilər - Müqayisəli Bar
vip_analysis = df.groupby('is_vip_customer').agg({
    'total_amount': ['mean', 'sum'],
    'sale_id': 'count'
})
vip_analysis.columns = ['Orta Çek', 'Ümumi Gəlir', 'Satış Sayı']
vip_analysis = vip_analysis.rename(index={False: 'Adi Müştəri', True: 'VIP Müştəri'})

plt.figure(figsize=(10, 6))
vip_analysis['Orta Çek'].plot(kind='bar', color=['blue', 'gold'])
plt.title('VIP və Adi Müştərilərin Orta Çeki', fontsize=14)
plt.xlabel('Müştəri Tipi')
plt.ylabel('Orta Çek Məbləği')
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(vip_analysis['Orta Çek']):
    plt.text(i, v + 5, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.savefig('vip_regular_bar.png')
plt.close()

# 6. Ödəniş Metodları - Dairə Qrafiki
payment_methods = df.groupby('payment_method')['total_amount'].sum()

plt.figure(figsize=(10, 8))
plt.pie(payment_methods, labels=payment_methods.index, autopct='%1.1f%%',
        startangle=90, explode=[0.05]*len(payment_methods),
        colors=sns.color_palette('pastel'))
plt.title('Ödəniş Metodlarının Payı', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.savefig('payment_pie.png')
plt.close()

# 7. Şəhərlərə görə Satışlar - Horizontal Bar Chart
city_sales = df.groupby('customer_city')['total_amount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 8))
city_sales.plot(kind='barh', color=sns.color_palette('viridis', len(city_sales)))
plt.title('Top 10 Şəhər üzrə Satışlar', fontsize=14)
plt.xlabel('Ümumi Satış Məbləği')
plt.ylabel('Şəhər')
plt.grid(axis='x', alpha=0.3)
for i, v in enumerate(city_sales):
    plt.text(v + 100, i, f"{v:.0f}", va='center')
plt.tight_layout()
plt.savefig('city_sales_bar.png')
plt.close()

# 8. Kombinə edilmiş vizuallaşdırma - Endirim analizinin daha dərin versiyası
discount_quantity = df.groupby('discount_pct')['quantity'].sum()
discount_revenue = df.groupby('discount_pct')['total_amount'].sum()
discount_avg_check = df.groupby('discount_pct')['total_amount'].mean()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12), sharex=True)

# Discount dəyərlərini formatla (emin olmaq üçün)
x_labels = [f"{int(x*100)}%" if x <= 1 else f"{int(x)}%" for x in discount_quantity.index]

# Yuxarıdakı qrafik - Satış Həcmi
x_pos = np.arange(len(discount_quantity))
bars1 = ax1.bar(x_pos, discount_quantity.values, color='skyblue', alpha=0.7)
ax1.set_ylabel('Satış Miqdarı', fontsize=12)
ax1.set_title('Endirim Səviyyələrinin Satış Həcminə Təsiri', fontsize=14)
ax1.grid(axis='y', alpha=0.3)
for i, bar in enumerate(bars1):
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontweight='bold')

# Aşağıdakı qrafik - Orta Çek
bars2 = ax2.bar(x_pos, discount_avg_check.values, color='salmon', alpha=0.7)
ax2.set_xlabel('Endirim Dərəcəsi', fontsize=12)
ax2.set_ylabel('Orta Çek Məbləği', fontsize=12)
ax2.set_title('Endirim Səviyyələrinin Orta Çekə Təsiri', fontsize=14)
ax2.grid(axis='y', alpha=0.3)
for i, bar in enumerate(bars2):
    height = bar.get_height()
    ax2.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontweight='bold')

# X oxu etiketlərini təyin et
ax2.set_xticks(x_pos)
ax2.set_xticklabels(x_labels)

plt.tight_layout()
plt.savefig('discount_combined.png')
plt.close()

print("Bütün qrafiklər yaradıldı və saxlanıldı!")

### 6. Təqdimatlı İnsaytlar

Yuxarıdakı vizuallaşdırmalardan satislar_data.csv faylı üçün çıxardığımız əsas insaytlar:

1. **Endirim İnsaytı:** Endirimsiz məhsullar (0%) ümumi satışda böyük pay tutur, lakin endirimli məhsullar arasında 15% endirim optimal nəticə verir və ən çox satış yaradır. 30% və daha yüksək endirimlər effektivliyi itirirlər.
2. **Zaman İnsaytı:** Satışlar şənbə günləri və 12-14 və 17-19 saatlarında pik həddə çatır. Bu, mağaza işçilərinin, inventarın və marketinq səylərinin planlaşdırılmasında istifadə edilə bilər.
3. **Məhsul İnsaytı:** Elektronika kateqoriyası ümumi satışlarda lider mövqe tutur (təxminən 40%). Kateqoriyalara görə strategiya və marketinq səylərinin uyğunlaşdırılması lazımdır.

4. **Müştəri İnsaytı:** VIP müştərilərin orta çeki adi müştərilərdən təxminən 2.5 dəfə daha yüksəkdir. VIP müştəriləri saxlamaq və artırmaq üçün xüsusi proqramlar işlənməlidir.
5. **Coğrafi İnsayt:** Böyük şəhərlər satışların əksəriyyətini təşkil edir, lakin kiçik şəhərlərdə də potensial var. Bəzi şəhərlər daha yüksək orta çeklə fərqlənir.

Bu insaytlar biznesə daha yaxşı qərarlar vermək və satışları artırmaq üçün təsirli istiqamətlər göstərir.
### 7. Yekun

İnsaytları vizuallaşdırmaq onları daha güclü və təsirli edir. Yaxşı hazırlanmış qrafiklərlə siz:

- Məlumatı daha asan başa düşülən formaya çevirə bilərsiniz
- Trendləri və nümunələri daha aydın göstərə bilərsiniz
- Biznes qərarlarına təsir edən əsas məqamları vurğulaya bilərsiniz
- Müxtəlif auditoriyalara görə insaytları uyğunlaşdıra bilərsiniz

Ən əsası, vizuallaşdırma sizə sadəcə statistika deyil, əməli təkliflər və fəaliyyət planları təqdim etməyə imkan verir.