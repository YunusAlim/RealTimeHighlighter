# Gerçek Zamanlı Söz Dizimi Vurgulayıcı

Projede, gerçek zamanlı söz dizimi vurgulama özelliğine sahip bir metin editörü uygulaması yapılmıştır. Proje python dilinde yazılmıştır. Vurgulayıcı, GUI üzerinde token’ları renklendirir, hataları anında bildirir. Bunu karakter karakter analiz eder. Her ne kadar aynı projeyi java dilinde oluşturmak isteyip sonuna kadar java dilinde devam etsem de belki java dilinde olan teknik yetersizliğim belki de java dilinde, istediğim vurgulayıcıyı oluşturmanın gerçekten python'a göre çok daha zor oluşu sebebiyle projeyi tamamlayamadım. Python dilinde java dilinde geldiğiim yere çok daha çabuk gelmemin dışında proje dosyasını okuduğumda aklımda canlanan projeyi oluşturabildim.
Tanıtım Videosu: https://www.youtube.com/watch?v=wBx1jKcJEVM&t=9s


## Özellikler

- Gerçek zamanlı söz dizimi vurgulama: Açılan ekrandaki kod bloğunun doğruluğunun kontrolü.
- 11 farklı token türü için renklendirme: 11 farklı tokenı anlayıp ona uygu renk ile eşleştirebilme.


## Kurulum

Bu proje için yalnızca güncel bir Python kurulumu yeterlidir. Kodun arayüzü için kullanılan tkinter kütüphanesi, Python'ın standart kütüphaneleri arasında yer aldığından ayrıca yüklemeye gerek yoktur.


## Sözdizimsel Analiz (Parser)
- Top-Down yaklaşımı kullanılmıştır.
- Parse ağacı önyineleme (preorder) şeklinde oluşturulur.
- Bağlamdan bağımsız gramer (Context-Free Grammar) ile ayrıştırma yapılır.


	program → stmt*

	stmt → decl_stmt | assign_stmt | if_stmt | while_stmt

	decl_stmt → TYPE ID '=' expr ';'

	assign_stmt → ID '=' expr ';'

	if_stmt → 'if' '(' condition ')' block

	while_stmt → 'while' '(' condition ')' block

	condition → expr COMPARISON expr

	block → '{' stmt* '}'

	expr → term (('+' | '-') term)*

	term → NUMBER | ID


## Sözcüksel Analiz (Lexer)

- Her karakter tek tek incelenir.
- Her token türü için özel tanıma koşulları (if-else blokları) uygulanır.


### Token Türleri

1. TYPE : Veri tipi (int, float)
2. KEYWORD : koşul ve döngü (if, while)
3. ID : Değişken adları (x, y, total)
4. NUMBER : Sayılar (0, 5, 100)
5. OP : Operatörler +, -, =
6. COMPARISON :Karşılaştırma ifadeleri <, >, ==, !=
7. SEMICOLON : Satır sonu (;)
8. BRACE : Süslü parantez ({})
9. PAREN : Parantez (())
10.UNKNOWN : Tanımlanamayan karakterler (@, #, vb.)
11.COMMENT : Yorum Savaşı (//)


## GUI Özellikleri 

- Tkinter tabanlıdır.
- Kod yazıldıkça `KeyRelease` olayına bağlı olarak analiz çalışır (real-time).
- Renkli vurgulama `Text` widget'ına tag eklenerek yapılır.
- Sonuç durumu alt kısımda `"✔ Syntax OK"` veya `"❌ Syntax Error"` olarak görünür.
