define s = Character(_("[isim]"), color="#660099")
define u = Character("?")
define a = Character("Ahmet", color="#0000FF")
define b = Character("Bengi", color="#00FFFF")
define o = Character("Öğretmen", color="#00FF00")
define ay = Character("Ayşegül", color="#ff55f1")
define an = Character("Anne", color="#FF0000")


transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0
transform allright:
    xalign 1.15
    yalign 1.0

define slowdissolve = Dissolve(1.0)

# Oyunun başladığı yer*

label start:

    python:
        isim = renpy.input(_("Karakterinize isim verin"))

        isim = isim.strip() or __("Utangaç")



    play music "varsayılan müzik.mp3" fadeout 1


    scene okul
    with fade


    show ana karaktersol at slightright


    s "Okul bugün yorucuydu."
    s "Ama en azından tatile girdiğimiz için mutluyum"

    show ogretmen at slightleft
    with moveinleft

    s "Merhaba Öğretmenim"
    o "Merhaba [isim], Görüyorum da yorulmuşsun."
    s "Evet Öğretmenim, Ama tatile girdiğimiz için mutluyum doğrusu"
    o "Ben de seninle o konuda konuşmak istiyordum"
    o "Bu sene tatilin başında İngilizcenizi geliştirebilmeniz için bir kamp olacak."
    s "Kamp mı?"
    o "Evet, bir İngilizce kampı. Kamptayken iletişimi sadece İngilizce gerçekleştireceğiz."
    s "Kulağa ilgi çekici geliyor öğretmenim"
    o "İlgili olduğunu bildiğim için ben de seni davet etmeyi düşünüyordum zaten"
    s "Annemden izin alabilirsem katılmayı çok isterim Öğretmenim."
    o "Bunu duyduğuma sevindim. O zaman katılmak için benimle iletişime geçmen yeter. Görüşmek üzere."
    s "Görüşürüz Öğretmenim."

    hide ogretmen
    with moveoutleft

    show ana karaktersol at center
    with moveoutleft

    s "İngilizce kampı... Gerçekten kulağa harika geliyor."

label ev:

    scene bg ev giris
    with fade

    show ana karaktersol at slightright
    with moveinright

    s "Anne ben geldim"
    an " Hoşgeldin mutfaktayım gel"

    hide ana karaktersol
    with moveoutleft

    scene bg ev mutfak
    with fade

    show anne at slightleft
    with dissolve
    show ana karaktersol at slightright
    with moveinright

    s "Anne bugün öğretmenim bir İngilizce Kampı'ndan bahsetti ve beni de davet etti."
    an "Bu harika [isim]. Eğer Katılmak istersen gidebilirsin."
    s "Teşekkürler anne."


    hide ana karaktersol
    with moveoutright

    scene black
    with fade


    #bazı iç konuşmalar*
    "2 Gün Sonra"



label kamp:

    play music "kampmüzik.mp3" fadeout 1

    # kamp için uygun bir müzik bulunup yeni müzik çalınacak queue music "varsayılan müzik.mp3" fadeout 1


    scene kamp oda gündüz
    with fade


    show ana karakter
    s"Ahhh iyi bir uykuydu"

    s "Kampta olduğum için mutluyum"
    s "Good morning to all..  \n(Günaydın herkese...)"
    s "İngilizce konuşmaya alışsam iyi olur"


    #odasından çıkıp etrafla etkileşim kurma zamanı

    scene bg kamp1
    with fade

    show ogretmen at slightleft
    with dissolve

    show ana karaktersol at slightright
    with moveinright

    s "Günaydın öğretmenim"
    o "What"
    s "Ah..."
    play sound "1.mp3"
    s "Good morning Teacher"
    play sound "2.mp3"
    o "Good Morning"
    s "(Şimdi karnımın acıktığını nasıl söyleyecektim ya)"

    #yeni bir sahne karakterler vardır ana karakter olaya girer ve diyaloglar için kullanıcıya seçenekler sunulur
    #seçeneklerin olduğu bölmenin kodu bu şekilde işleyecektir.

    label choice1:
    menu:

        "I am Hungry":
            jump choice1_yes

        "I am good":
            jump choice1_no

        "I am full ":
            jump choice1_no2

        "I can do it":
            jump choice1_no3

    label choice1_yes:

        $ menu_flag = True
        play sound "3.mp3"

        s "I am Hungry "


        jump choice1_done


    label choice1_no:

        $ menu_flag = False

        "Bu cümle 'Ben İyiyim' anlamına geliyor. Tekrar dene"

        jump choice1

    label choice1_no2:

        $ menu_flag = False

        "Bu cümle 'Ben Tokum' anlamına geliyor. Tekrar dene"

        jump choice1


    label choice1_no3:

        $ menu_flag = False

        "Bu cümle 'Ben yapabilirim' anlamına geliyor. Tekrar dene"

        jump choice1


    label choice1_done:

        # burdan devam edilir


    play sound "4.mp3"
    o "Oh Breakfast is ready. Come Join Us."


    s "(*Öğretmen Yemeğin Hazır olduğunu ve onlara katılmam gerektiğini söyledi sanırım)"
    play sound "5.mp3"
    s "Of course  \n(Tabii ki)"

    scene bg yemekhane
    with fade

    show ana karakter at slightleft
    with moveinleft

    s "Burası yemekhane olmalı"

    show ahmetsol at slightright
    with moveinright

    play sound "6.mp3"
    u "Hello, My name is Ahmet"
    s "(*Güzel, Birileri ile tanışma fırsatı)"


    label choice2:
        menu:

            "Hello Ahmet, Thank you":
                jump choice2_no2

            "Hello Ahmet, I am lost":
                jump choice2_no

            "Hello Ahmet, My name is [isim]. Nice to meet you":
                jump choice2_yes

            "Hello Ahmet, I am 14 years old":
                jump choice2_no3

        label choice2_yes:

            $ menu_flag = True
            play sound "7.mp3"

            s "Hello Ahmet, My name is [isim]. Nice to meet you"

            jump choice2_done


        label choice2_no:

            $ menu_flag = False

            s "Bu cümle 'Merhaba Ahmet, Ben kayboldum.' anlamına geliyor. Tekrar dene"

            jump choice2

        label choice2_no2:

            $ menu_flag = False

            s "Bu cümle 'Merhaba Ahmet, Teşekkür ederim' anlamına geliyor. Tekrar dene"

            jump choice2


        label choice2_no3:

            $ menu_flag = False

            s "Bu cümle 'Merhaba Ahmet, Ben 14 yaşındayım.' anlamına geliyor. Tekrar dene"

            jump choice2


        label choice2_done:

            # burdan devam edilir

    s "(Ahmet iyi birine benziyor.) "
    play sound "8.mp3"
    a "Do you like the camp?"
    s "(Kampı sevip sevmediğimi soruyor)"
    play sound "9.mp3"
    s "Yes, I like the camp"
    play sound "10.mp3"
    a "I am happy to hear that  \n(Bunu duyduğuma sevindim)"
    s "(İyi bir şey konuştuğumuza eminim ama artık yemek yemeliyim)"

    label choice3:
    menu:

        "Okay, Let's Go":
            jump choice3_no3

        "Okay, Let's jump":
            jump choice3_no

        "Okay, Let's buy it":
            jump choice3_no2

        "Okay, Let's Eat ":
            jump choice3_yes

    label choice3_yes:

        $ menu_flag = True
        play sound "11.mp3"

        s "Okay, Let's Eat "

        jump choice3_done


    label choice3_no:

        $ menu_flag = False

        s "Bu cümle 'Tamam, Hadi Zıplayalım' anlamına geliyor. Tekrar dene"

        jump choice3

    label choice3_no2:

        $ menu_flag = False

        s "Bu cümle 'Tamam, Hadi satın alalım' anlamına geliyor. Tekrar dene"

        jump choice3


    label choice3_no3:

        $ menu_flag = False

        s "Bu cümle 'Tamam, Hadi gidelim' anlamına geliyor. Tekrar dene"

        jump choice3


    label choice3_done:

        # burdan devam edilir


    play sound "12.mp3"
    a "Okaaay"

    scene black
    with fade

    s "Kahvaltı çok güzeldi. Karnımızı doyurduktan sonra bize kamp alanına gitmemiz söylendi."

    scene bg kamp1
    with fade

    show ana karakter at slightleft
    show ahmet at center
    show bengi at left
    show ogretmensol at right

    play sound "13.mp3"
    o "Good morning to all  \n(Herkese Günaydın)"
    play sound "14.mp3"
    o "We want you to meet each other  \n(Biz sizin kendi aranızda tanışmanızı istiyoruz.)"
    play sound "15.mp3"
    o "Until the evening, You are in free time. \n(Akşama kadar serbest vakittesiniz.)"
    play sound "16.mp3"
    o "Explore around and meet each other.  \n(Etrafı keşfedin ve birbirinizle tanışın)"
    play sound "17.mp3"
    o "See you at evening. \n(Akşama görüşürüz)."
    s "(İşte bu güzel bir fırsat olucak.)"

    hide ogretmensol
    with moveoutright
    hide ahmet
    with moveoutright
    show ana karakter at slightright with moveoutright
    hide ana karakter
    show ana karaktersol at slightright
    show bengi at slightleft with moveoutright
    s "Hello I am [isim]"
    play sound "18.mp3"
    u "Hello my name is Bengi, Nice to meet you."
    play sound "19.mp3"
    b "How old are you?"


    label choice4:
    menu:

        "I am 12 years old. How old are you?":
            jump choice4_yes

        "I am fine thanks and you?":
            jump choice4_no

        "I am Hungry thank you":
            jump choice4_no2

        "I like it, thank you":
            jump choice4_no3

    label choice4_yes:

        $ menu_flag = True

        play sound "20.mp3"
        s "I am 12 years old. How old are you?"

        jump choice4_done


    label choice4_no:

        $ menu_flag = False

        s "Bu cümle 'Ben iyiyim, sen nasılsın' anlamına geliyor. Tekrar dene"

        jump choice4

    label choice4_no2:

        $ menu_flag = False

        s "Bu cümle 'Ben açım, Teşekkürler' anlamına geliyor. Tekrar dene"

        jump choice4


    label choice4_no3:

        $ menu_flag = False

        s "Bu cümle 'Bunu sevdim, Teşekkürler' anlamına geliyor. Tekrar dene"

        jump choice4


    label choice4_done:

        # burdan devam edilir


    play sound "21.mp3"
    b "I am 11 years old."
    play sound "22.mp3"
    s "So you are younger than me  \n(O zaman sen benden küçüksün)"
    play sound "23.mp3"
    b "Yes"
    s "(Acaba buraya nereden gelmiş?)"

    label choice5:
    menu:

        "Where are you going?":
            jump choice5_no

        "Where are you from?":
            jump choice5_yes

        "Are you sure about that?":
            jump choice5_no2

        "What is wrong?":
            jump choice5_no3

    label choice5_yes:

        $ menu_flag = True

        play sound "24.mp3"
        s "Where are you from?"

        jump choice5_done


    label choice5_no:

        $ menu_flag = False

        s "Bu cümle 'Nereye gidiyorsun?' anlamına geliyor. Tekrar dene"

        jump choice5

    label choice5_no2:

        $ menu_flag = False

        s "Bu cümle 'Bundan emin misin?' anlamına geliyor. Tekrar dene"

        jump choice5


    label choice5_no3:

        $ menu_flag = False

        s "Bu cümle 'Sorun nedir?' anlamına geliyor. Tekrar dene"

        jump choice5


    label choice5_done:

        # burdan devam edilir


    play sound "25.mp3"
    b "I'm from Ankara, You?"
    play sound "26.mp3"
    s "I'm from Isparta"
    play sound "27.mp3"
    b "What are your hobbies?"
    s "(Bana hobilerimi soruyor)"
    s "(Hmm... Ben yüzmekten, kitap okumaktan ve basketbol oynamaktan hoşlanırım)"

    label choice6:
    menu:

        "I like playing games, watching TV and cooking":
            jump choice6_no3

        "I hate reading a book, dancing and singing":
            jump choice6_no

        "I like black, red and blue":
            jump choice6_no2

        "I like swimming, reading a book and playing basketball":
            jump choice6_yes

    label choice6_yes:

        $ menu_flag = True

        play sound "28.mp3"
        s "I like swimming, reading a book and playing basketball"

        jump choice6_done


    label choice6_no:

        $ menu_flag = False

        s "Bu cümle 'Ben Kitap okumaktan, dans etmekten ve şarkı söylemekten nefret ederim.' anlamına geliyor. Tekrar dene"

        jump choice6

    label choice6_no2:

        $ menu_flag = False

        s "Bu cümle 'Ben siyahı, kırmızıyı ve maviyi severim' anlamına geliyor. Tekrar dene"

        jump choice6


    label choice6_no3:

        $ menu_flag = False

        s "Bu cümle 'Ben oyun oynamayı, televizyon seyretmeyi ve yemek yapmayı severim' anlamına geliyor. Tekrar dene"

        jump choice6


    label choice6_done:

        # burdan devam edilir


    play sound "29.mp3"
    b "How Great it is \n( Ne kadar da güzel)"
    play sound "30.mp3"
    s "So how is it going in the camp? \n(Kampta nasıl gidiyor)"
    play sound "31.mp3"
    b "Actually, I lost my necklace yesterday. \n(Aslında dün kolyemi kaybettim)"
    play sound "32.mp3"
    s "What a shame. If I see it anywhere, I will bring it to you. \n(Ne yazık, Eğer biryerde görürsem, Sana getiririm.)"
    play sound "33.mp3"
    b "Thank you"
    play sound "34.mp3"
    s "Now let's go there and meet other people. \n(Şimdi şuraya gidelim ve başkalarıyla tanışalım)"
    play sound "35.mp3"
    b "Yeah, sure. \n(Evet, Tabii)"

    hide ana karaktersol with moveoutright
    hide bengi with moveoutright

    scene black
    with fade

    s "(Kalabalığa ilerlerken Bengi'nin Ahmet'le tanışmaya yöneldiğini gördüm)"
    s "(Bende ilerlediğimde öğretmenle konuşan birini gördüm ve neler olduğunu öğrenmek için yanlarına gittim.)"


    scene bg kamp2
    with fade

    show ogretmensol at allright
    show ayşegül at slightright

    o "I dont know about this necklace. You can ask around the people\n (Kolye hakkında bir şey bilmiyorum. Etraftaki insanlara sorabilirsin.)"
    u " Okay, teacher."

    show ana karakter at slightleft
    with moveinleft

    o "Here is [isim] coming. You can start with asking him.\n(İşte [isim] geliyor. Ona sorarak başlayabilirsin.)"
    u "Okay, teacher."
    hide ogretmensol
    with moveoutright
    hide ayşegül
    show ayşegülsol at slightright
    s "Uh... Hello."
    u "Hello [isim], My name is Ayşegül"
    s "What is the problem?\n(Sorun nedir?)"
    ay "I found a necklace. I am trying to find who lost it\n(Bir kolye buldum. Kimin kaybettiğini bulmaya çalışıyorum.)"
    s "(Aa bu Bengi'nin kaybettiğini söylediği kolye olabilir)"



    label choice7:
    menu:

        "I think that could be Bengi's necklace":
            jump choice7_yes

        "I think that is mine":
            jump choice7_no

        "I think that is yours":
            jump choice7_no2

        "I think I can find it":
            jump choice7_no3

    label choice7_yes:

        $ menu_flag = True

        s "I think that could be Bengi's necklace"

        jump choice7_done


    label choice7_no:

        $ menu_flag = False

        s "Bu cümle 'Sanırım o benim' anlamına geliyor. Tekrar dene"

        jump choice7

    label choice7_no2:

        $ menu_flag = False

        s "Bu cümle 'Sanırım o senin' anlamına geliyor. Tekrar dene"

        jump choice7


    label choice7_no3:

        $ menu_flag = False

        s "Bu cümle 'Sanırım ben onu bulabilirim' anlamına geliyor. Tekrar dene"

        jump choice7


    label choice7_done:

        # burdan devam edilir

    ay "Really? How do you know?\n(Gerçekten mi? Nasıl biliyorsun?)"

    label choice8:
    menu:

        "No, I don't know anything":
            jump choice8_no2

        "Yes, I made it up":
            jump choice8_no

        "Yes, She told me that she lost her necklace":
            jump choice8_yes

        "Yes, Öğretmen told me to stop":
            jump choice8_no3

    label choice8_yes:

        $ menu_flag = True

        s "Yes, She told me that she lost her necklace"

        jump choice8_done


    label choice8_no:

        $ menu_flag = False

        s "Bu cümle 'Evet, Ben uydurdum' anlamına geliyor. Bengi'nin sana bahsettiğini söylemelisin. Tekrar dene"

        jump choice8

    label choice8_no2:

        $ menu_flag = False

        s "Bu cümle 'Hayır, Ben bir şey bilmiyorum' anlamına geliyor. Bengi'nin sana bahsettiğini söylemelisin. Tekrar dene"

        jump choice8


    label choice8_no3:

        $ menu_flag = False

        s "Bu cümle 'Evet, Öğretmen bana durmamı söyledi.' anlamına geliyor. Bengi'nin sana bahsettiğini söylemelisin. Tekrar dene"

        jump choice8


    label choice8_done:



    ay "That is great but I don't know Bengi\n(Bu harika ama ben Bengi'yi tanımıyorum)"
    s "I can make you meet with her\n(Ben seni onla tanıştırabilirim.)"
    s "She is there talking with Ahmet. Let's go"

    hide ana karakter
    show ana karaktersol
    hide ana karaktersol with moveoutleft
    hide ayşegül with moveoutleft

    scene bg kamp1
    with fade

    show ahmetsol at right
    show bengisol at slightright




    show ana karakter at slightleft
    with moveinleft
    show ayşegül at left
    with moveinleft

    s "Hello there Bengi and Ahmet"
    s "This is Ayşegül"
    b "Helloo"
    a "Hello"
    s "Bengi we have some news for you\n(Bengi sana bazı haberlerim var.)"
    ay "Yes we have"
    b "What is it?\n(Nedir o?)"

    label choice9:
    menu:

        "Ayşegül playing a game":
            jump choice9_no

        "Ayşegül found a necklace":
            jump choice9_yes

        "Ayşegül caught a fish":
            jump choice9_no2

        "Ayşegül found a ring":
            jump choice9_no3

    label choice9_yes:

        $ menu_flag = True

        s "Ayşegül found a necklace"

        jump choice9_done


    label choice9_no:

        $ menu_flag = False

        s "Bu cümle 'Ayşegül oyun oynuyor' anlamına geliyor. Tekrar dene"

        jump choice9

    label choice9_no2:

        $ menu_flag = False

        s "Bu cümle 'Ayşegül balık yakaladı' anlamına geliyor. Tekrar dene"

        jump choice9


    label choice9_no3:

        $ menu_flag = False

        s "Bu cümle 'Ayşegül yüzük buldu' anlamına geliyor. Tekrar dene"

        jump choice9


    label choice9_done:

    ay "And [isim] thinks this is yours\n(Ve [isim] senin olduğunu düşünüyor.)"
    b "Bu Muhteşem"
    b "Yani ımmm This is awesome"

    s "Yes I just remembered that you told me you lost one\n(Evet Ben senin bana kaybettiğini söylediğini hatırladım.)"
    b "Ah thank you so much"

    ay "Here, This is it\n(İşte burada)"
    b "Ahh Yes that's mine\n(Ahh evet bu benim)"
    b "Thank you again"

    scene black
    with fade

    s "4 Arkadaş sohbet edip iyice tanışıp beraber vakit geçirdikten sonra akşama doğru öğretmenin olduğu yere toplanmıştık. Bizi neyin beklediğini henüz bilmiyorduk"

    scene kamp gece
    with fade

    show ana karakter at left
    show ayşegül at slightleft
    show bengi at center
    show ahmet at slightright
    show ogretmensol at allright

    o "Okay students, We are here because we are going to play games for more English practice.\(Evet öğrenciler,Daha fazla İngilizce pratiği için burda oyun oynamak için toplandık."
    ay "That is so great"
    o "You are going to play this game with your 1 friend.\n(Bu oyunu 1 arkadaşınız ile oynayacaksınız)"
    o "And you are going to tell him/her a theme like fruits or colors.\n(Ve ona bir tema söyleyeceksiniz. Örneğin meyveler ve renkler.)"
    o "And he/she is going to tell 5 things of this theme\n(Ve o da size bu tema hakkında 5 tane şey sayacak.)"
    a "That is fine"
    o "Let's Start then"

    hide ogretmensol
    with moveoutright
    hide ahmet
    with moveoutright
    hide bengi
    with moveoutright
    show ayşegül at slightright
    with moveoutright
    hide ayşegül
    show ayşegülsol at slightright
    show ana karakter at slightleft
    with moveoutright

    s "Hi Ayşegül"
    ay "Hello [isim]"
    s "You go first"
    ay "Okay I'm choosing"
    ay "I say Fruits"
    s "(Hmmm Meyveler)"


    label choice10:
    menu:

        "Apple, Blue, Tree, Car, Cup":
            jump choice10_no

        "Flag, Orange, Computer, Phone, Mandarin":
            jump choice10_no2

        "Orange, Apple, Coffee, Book, Table":
            jump choice10_no3

        "Pear, Apple, Strawberry, Orange, Apricot":
            jump choice10_yes

    label choice10_yes:

        $ menu_flag = True

        s "Pear, Apple, Strawberry, Orange, Apricot"

        jump choice10_done


    label choice10_no:

        $ menu_flag = False

        s "Burda 'Blue=Mavi, Tree=Ağaç, Car=Araba, Cup=Kupa' anlamına geliyor. Tekrar dene"

        jump choice10

    label choice10_no2:

        $ menu_flag = False

        s "Burda 'Flag=Bayrak, Computer=Bilgisayar, Phone=Telefon' anlamına geliyor. Tekrar dene"

        jump choice10


    label choice10_no3:

        $ menu_flag = False

        s "Burda 'Coffee=Kahve, Book=Kitap, Table=Masa' anlamına geliyor. Tekrar dene"

        jump choice10


    label choice10_done:


    ay "Okay, That is all true. Now your turn."
    "Birazdan yapacağın alıştırmada doğru cevap bulunmuyor. Cevap verildikten sonra geriye gelip yeni cevapları deneyerek bütün şıklardaki şeyleri öğrenebilirsin."

    label choice11:
    menu:

        "Colors":
            jump choice11_yes

        "Animals":
            jump choice11_no

        "Vegetables":
            jump choice11_no2

        "Jobs":
            jump choice11_no3

    label choice11_yes:

        $ menu_flag = True

        s "Colors"

        ay "Blue, Red, Purple, Orange, Green"

        jump choice11_done


    label choice11_no:

        $ menu_flag = False

        s "Animals"
        ay "Dog, Cat, Donkey, Horse, Monkey"

        jump choice11_done

    label choice11_no2:

        $ menu_flag = False

        s "Vegetables"
        ay "Tomato, Potato, Broccoli, Onion, Carrot"

        jump choice11_done


    label choice11_no3:

        $ menu_flag = False

        s "Jobs"
        ay "Doctor, Engineer, Teacher, Lawyer, Police"

        jump choice11_done


    label choice11_done:

    s "That's all correct"

    hide ayşegülsol
    with moveoutright
    show ahmetsol at slightright
    with moveinright

    a "Hello [isim]"
    s "Hi Ahmet"
    "Birazdan yapacağın alıştırmada doğru cevap bulunmuyor. Cevap verildikten sonra geriye gelip yeni cevapları deneyerek bütün şıklardaki şeyleri öğrenebilirsin."

    label choice12:
    menu:

        "Month Names":
            jump choice12_yes

        "Weather":
            jump choice12_no

        "Sports":
            jump choice12_no2

        "Vehicles":
            jump choice12_no3

    label choice12_yes:

        $ menu_flag = True

        s "Month Names"

        ay "January, February, March, April, May"

        jump choice12_done


    label choice12_no:

        $ menu_flag = False

        s "Weather"
        ay "Sunny, Cloudy, Rainy, Snowy, Stormy"

        jump choice12_done

    label choice12_no2:

        $ menu_flag = False

        s "Sports"
        ay "Football, Basketball, Tennis, Skiing, Volleyball"

        jump choice12_done


    label choice12_no3:

        $ menu_flag = False

        s "Vehicles"
        ay "Car, Boat, Plane, Bus, Train"

        jump choice12_done


    label choice12_done:

    a "That is Correct."
    s "Okay now you."
    a "Hmmmm, I pick Clothes"

    label choice13:
    menu:

        "Dress, Skirt, Skiing, Apple, June":
            jump choice13_no

        "August, Stormy, Shoes, Table, Plane":
            jump choice13_no2

        "Skirt, Shoes, Pants, Dress, Socks":
            jump choice13_yes

        "Pants, Socks, Orange, Bus, Shoes":
            jump choice13_no3

    label choice13_yes:

        $ menu_flag = True

        s "Skirt, Shoes, Pants, Dress, Socks"

        jump choice13_done


    label choice13_no:

        $ menu_flag = False

        s "Burda 'Skiing=Kayak Yapmak, Apple=Elma, June=Haziran' anlamına geliyor. Tekrar dene"

        jump choice13

    label choice13_no2:

        $ menu_flag = False

        s "Burda 'August=Ağustos, Stormy=Fırtınalı, Table=Masa, Plane=Uçak' anlamına geliyor. Tekrar dene"

        jump choice13


    label choice13_no3:

        $ menu_flag = False

        s "Burda 'Orange=Portakal ya da Turuncu, Bus=Otobüs' anlamına geliyor. Tekrar dene"

        jump choice13


    label choice13_done:

    a "Congrats, That is all true"

    hide ahmetsol
    with moveoutright
    show bengisol at slightright
    with moveinright

    s "Hello there Bengi"
    b "Hello [isim], Thanks for the necklace again."
    s "No problem."
    b "Okay I am starting now"
    b "I pick Month names"

    label choice14:
    menu:

        "July, September, October, November, December":
            jump choice14_yes

        "August, Swimming, Boat, Tree, People":
            jump choice14_no

        "June, Door, Black, August, December":
            jump choice14_no2

        "January, Computer, March, April, Hat":
            jump choice14_no3

    label choice14_yes:

        $ menu_flag = True

        s "July, September, October, November, December"

        jump choice14_done


    label choice14_no:

        $ menu_flag = False

        s "Burda 'Swimming=Yüzmek, Boat=Bot, Tree=Ağaç, People=İnsan' anlamına geliyor. Tekrar dene"

        jump choice14

    label choice14_no2:

        $ menu_flag = False

        s "Burda 'Door=Kapı, Black=Siyah' anlamına geliyor. Tekrar dene"

        jump choice14


    label choice14_no3:

        $ menu_flag = False

        s "Burda 'Computer=Bilgisayar, Hat=Şapka' anlamına geliyor. Tekrar dene"

        jump choice14


    label choice14_done:

    b "That is all correct"
    s "Now, I pick..."

    label choice15:
    menu:

        "Fruits":
            jump choice15_yes

        "Animals":
            jump choice15_no

        "School Stuffs":
            jump choice15_no2

        "Technological devices":
            jump choice15_no3

    label choice15_yes:

        $ menu_flag = True

        s "Fruits"

        b "Banana, Strawberry, Pear, Orange, Lemon"

        jump choice15_done


    label choice15_no:

        $ menu_flag = False

        s "Animals"
        b "Sheep, Horse, Bee, Fly, Penguin"

        jump choice15_done

    label choice15_no2:

        $ menu_flag = False

        s "School Stuffs"
        b "Pencil, Rubber, Book, Notebook, Pencil Sharpener"

        jump choice15_done


    label choice15_no3:

        $ menu_flag = False

        s "Technological Devices"
        b "Telephone, Computer, Tv, Fridge, Washing Machine"

        jump choice15_done


    label choice15_done:

    s "That's all correct"

    s "Okay, I guess we are done here.\n(Tamam, Sanırım bitirdik.)"
    b "Yes, I am so nice to meet everybody in here.\n(Evet Burdaki herkesle tanıştığım için mutluyum.)"

    show ogretmensol at allright
    with moveinright
    hide bengi
    show bengisol at slightright

    o "Okay everybody, Now to your beds to have a sleep.\n(Evet herkes şimdi uyumak için yataklarına)"
    s "Okay bye everybody"

    hide ana karakter
    with moveoutleft

    scene kamp oda gece
    with fade

    show ana karakter at center
    with moveinleft

    s "Aah what a day\n(Ne gündü ama)"
    s "Let's get to sleep"
    "Teşekkürler""Oyunun şu ana kadar yazılı olan kısmını bitirdiniz. \nYeni yamalar için beklemede kalın."







# This ends the game.

    return
