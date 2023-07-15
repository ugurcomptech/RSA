# RSA Algoritması

RSA (Rivest-Shamir-Adleman), en yaygın olarak kullanılan şifreleme algoritmalarından biridir. İki ana bileşeni olan asimetrik bir şifreleme algoritmasıdır: anahtar üretimi ve şifreleme/çözme.

## Anahtar Üretimi

1. İki adet asal sayı seçin: p ve q.
2. n = p * q hesaplayın. Bu, genel anahtarın bir bileşenidir.
3. φ(n) = (p - 1) * (q - 1) hesaplayın. φ(n), Euler işlevidir ve diğer bileşenleri oluşturmak için kullanılır.
4. 1 < e < φ(n) olan bir "e" sayısı seçin. e, φ(n) ile aralarında asal olmalıdır. Bu, genel anahtarın diğer bileşenidir.
5. "d"yi hesaplamak için d * e ≡ 1 (mod φ(n)) denklemine göre d'yi bulun. d, özel anahtarın bir bileşenidir.

## Şifreleme

1. Metni temsil eden bir sayıya dönüştürün (örneğin, ASCII değerlerini kullanarak her harfi bir sayıya dönüştürebilirsiniz).
2. C = M^e (mod n) denklemine göre metni şifreleyin. C, şifrelenmiş metni temsil eden bir sayıdır.

## Çözme

1. Şifrelenmiş metni temsil eden sayıyı alın (C).
2. M = C^d (mod n) denklemine göre şifrelenmiş metni çözün. M, orijinal metni temsil eden bir sayıdır.
3. Sayıyı metne dönüştürün (örneğin, her sayıyı ASCII değerine dönüştürerek her sayıyı bir harfe dönüştürebilirsiniz).

Bu şekilde, RSA algoritması ile metinleri şifreleyebilir ve çözebilirsiniz. Önemli olan, genel anahtarın paylaşılabilir olduğu, ancak özel anahtarın gizli kalması gerektiğidir. Genel anahtarla şifreleme yapılırken, yalnızca özel anahtarla çözülebilen güvenli bir şifreleme sağlanır. Bu nedenle, RSA algoritması güvenli veri iletimi için yaygın olarak kullanılmaktadır.

Daha fazla bilgi için [RSA (kriptografi)](https://tr.wikipedia.org/wiki/RSA_(kriptografi)) sayfasını ziyaret edebilirsiniz.

## Algoritma Şeması

![image](https://github.com/ugurcomptech/RSA/assets/133202238/d2eb7904-ce10-4853-8bed-b703eaaabcf1)
