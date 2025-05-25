
SSELECT * FROM musteriler;
--------------------------

SELECT ad, soyad, email FROM musteriler;
-------------------------

WHERE Şərti ilə Filtrləmə
Kod:
SELECT ad, soyad, yas FROM musteriler WHERE yas > 30;

SELECT ad, soyad FROM musteriler WHERE email LIKE '%@gmail.com';
-----------------------
ORDER BY ilə Sıralama
Kod:

SELECT ad, soyad, yas FROM musteriler ORDER BY yas DESC;

SELECT ad, soyad, yas FROM musteriler ORDER BY yas DESC, ad ASC;
-----------------------

Aggregat Funksiyalar (COUNT, SUM, AVG, MAX, MIN)
Kod:

SELECT COUNT(*) AS musteri_sayi, AVG(yas) AS orta_yas FROM musteriler WHERE seher = 'Baki';

SELECT MAX(yas) AS en_yasli, MIN(yas) AS en_genc FROM musteriler;
-----------------------
GROUP BY ilə Qruplaşdırma
Kod:

SELECT seher, COUNT(*) AS musteri_sayi FROM musteriler GROUP BY seher;

SELECT seher, SUM(sifaris_miqdari) AS umumi_sifaris FROM sifarisler GROUP BY seher;

------------------------

JOIN ilə Cədvəlləri Birləşdirmə
Kod:

SELECT m.ad, m.soyad, s.sifaris_id, s.miqdar 
FROM musteriler m 
INNER JOIN sifarisler s ON m.musteri_id = s.musteri_id;

SELECT m.ad, m.soyad, s.sifaris_id 
FROM musteriler m 
LEFT JOIN sifarisler s ON m.musteri_id = s.musteri_id;
-------------------------

INSERT ilə Məlumat Əlavə Etmə
Kod:

INSERT INTO musteriler (ad, soyad, yas, seher) 
VALUES ('Ali', 'Huseynov', 28, 'Baki');

INSERT INTO musteriler (ad, soyad, yas, seher) 
VALUES 
    ('Ali', 'Huseynov', 28, 'Baki'),
    ('Ayten', 'Aliyeva', 35, 'Gence');

-------------------------


UPDATE ilə Məlumat Yeniləmə
Kod:

UPDATE musteriler 
SET yas = 29 
WHERE musteri_id = 1;


UPDATE musteriler 
SET yas = 30, seher = 'Sumqayit' 
WHERE musteri_id = 1;

---------------------------

DELETE ilə Məlumat Silmə
Kod:

DELETE FROM musteriler WHERE musteri_id = 1;

DELETE FROM musteriler WHERE yas < 18;

---------------------------

Subquery (Alt Sorğu)
Kod:

SELECT ad, soyad 
FROM musteriler 
WHERE musteri_id IN (
    SELECT musteri_id 
    FROM sifarisler 
    WHERE miqdar > 1000
);

SELECT ad, soyad 
FROM musteriler m 
WHERE EXISTS (
    SELECT 1 
    FROM sifarisler s 
    WHERE s.musteri_id = m.musteri_id AND s.miqdar > 1000
);
---------------------------


Cədvəl Yaratma (CREATE TABLE)
Kod:

CREATE TABLE musteriler (
    musteri_id INT PRIMARY KEY,
    ad VARCHAR(50),
    soyad VARCHAR(50),
    yas INT,
    seher VARCHAR(50)
);


CREATE TABLE sifarisler (
    sifaris_id INT PRIMARY KEY,
    musteri_id INT,
    miqdar DECIMAL(10,2),
    tarix DATE,
    FOREIGN KEY (musteri_id) REFERENCES musteriler(musteri_id)
);

Mürəkkəb Sorğu (JOIN, GROUP BY, HAVING)
Kod:

SELECT m.seher, COUNT(s.sifaris_id) AS sifaris_sayi, SUM(s.miqdar) AS umumi_miqdar
FROM musteriler m
INNER JOIN sifarisler s ON m.musteri_id = s.musteri_id
GROUP BY m.seher
HAVING COUNT(s.sifaris_id) > 10
ORDER BY umumi_miqdar DESC;

