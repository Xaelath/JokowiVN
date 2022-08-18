# Declare characters used by this game.
define j = Character(_("Jokowi"), color="#e30d0d", what_prefix='"', what_suffix='"', callback=high_beep)
define jpot = Character(_("Jokowi"), color="#e30d0d", image="jpot",  what_prefix='"', what_suffix='"', callback=high_beep)

#define jnar = Character(_("Jokowi"), color="#e30d0d", callback=high_beep)

define jkecil = Character(_("Jokowi(kecil)"), color="#AA4E4E", what_prefix='"', what_suffix='"',  callback=kecil_beep)
define pjkue =  Character(_("Penjual"), color="#7f8a8e", what_prefix='"', what_suffix='"',  callback=arang_beep)
define Sujiatmi = Character(_("Sujiatmi"), color="#f097eb", what_prefix='"', what_suffix='"',  callback=low_beep)

define wartawan1 = Character(_("Wartawan 1"), what_prefix='"', what_suffix='"',  color="#ffffff", callback=waratawanbeep)
define wartawan2 = Character(_("Wartawan 2"), what_prefix='"', what_suffix='"',  color="#ffffff", callback=waratawanbeep)
define gibran = Character(_("Gibran"),  what_prefix='"', what_suffix='"', color="#158d85", callback=high_beep2)

define narrator = Character(None, kind=nvl, callback=narrator_beep)
define narrator2 = Character(None, kind=adv, callback=narrator_beep)

#define position
transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightleft75:
    xalign 0.25
    yalign 0.36

transform slightright:
    xalign 0.75
    yalign 1.0

#define music
define audio.wayhome = "/audio/the-way-home-6674.mp3"
define audio.triumph = "/audio/triumphant-long-6673.mp3"
define audio.salmon = "/audio/one-eyed-salmon-7482.mp3"
define audio.melodyofnature = "/audio/melody-of-nature-main-6672.mp3"
define audio.cinema_ambient = "/audio/cinematic-ambient-feeling-ambient-piano-music-for-videos-7767.mp3"
define audio.happydays = "/audio/ambient-piano-happy-days--5541.mp3"
define audio.indonesiaraya = "/audio/indonesiaraya.mp3"
define audio.angel = "/audio/angel-piano-main-9625.mp3"
define audio.simpleday = "/audio/simple-piano-melody-9834.mp3"
define audio.lobby = "/audio/AA/1-03 Gyakuten Saiban 5 - Trial.mp3"
define audio.question = "/audio/AA/1-04 Questioning ~ Moderato 2013.mp3"
define audio.logic = "/audio/AA/1-05 Logic Trinity.mp3"
define audio.objection = "/audio/AA/1-07 Phoenix Wright ~ Objection! 2013.mp3"
define audio.question2 = "/audio/AA/1-09 Questioning ~ Allegro 2013.mp3"
define audio.suspense = "/audio/AA/1-10 Suspense 2013.mp3"
define audio.pursuit = "/audio/AA/1-11 Pressing Pursuit ~ Keep Pressing On.mp3"
define audio.noisy = "/audio/AA/1-33 Noisy People.mp3"
define audio.choice = "/audio/AA/2-07 Chains of the Heart ~ Psyche-Lock 2013.mp3"
define audio.pursuit2 = "/audio/AA/2-16 Variation.mp3"
define audio.enddebat = "/audio/AA/2-18 Gyakuten Saiban 5 ~ End.mp3"
define audio.investigation = "/audio/AA/1-23 Investigation ~ Opening 2013.mp3"
define audio.examination = "/audio/AA/2-05 Investigation ~ Examination.mp3"
define audio.difficult = "/audio/AA/1-34 Suspicious People.mp3"
define audio.suspicious = "/audio/AA/1-35 Difficult People.mp3"

#dontforgettoaddspoilers

#define sound
define audio.logowav = "/audio/567205__ddmyzik__simple-clean-logo.wav"
define audio.clap1= "/sfx/cheering-and-clapping-crowd-1-5995.ogg"
define audio.cheer1= "/sfx/crowd-cheer-ii-6263.ogg"
define audio.clap2 = "/sfx/short-crowd-cheerflac-6713.ogg"
define audio.clap3 = "/sfx/small-applause-6695.ogg"
define audio.crowd = "/sfx/crowded-avenue-people-talking-vendors-shouting-musicians-playing-part-1-7099.ogg"
define audio.laugh = "/sfx/Audience-Laughing-1-Sound-Effect.ogg"


#transitions

#Decare style and images
image white = "#ffffff"

style chapter_intro:
    color'#ffffff'
    size 42
    font "VCR_OSD_MONO_1.001.ttf"

style monologue:
    color'#ffffff'
    size 28
    font "VCR_OSD_MONO_1.001.ttf"

style monologue2:
    color'#ffd6d6'
    size 28
    font "VCR_OSD_MONO_1.001.ttf"
    outlines [ (absolute(20), "#ff0000", absolute(0), absolute(0)) ]


# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default presiden = False
default point = 0
default trueend = False
default rng = 0

#menu change
default persistent.finish = None
default show_quick_menu = True
#default persistent.quiz = None

#splashscreen
image splash = "splash.png"

label splashscreen:
    scene white
    with Pause(1)

    play sound logowav

    show splash with dissolve
    with Pause(2)

    scene white with dissolve
    with Pause(1)

    #need disclaimer
    #add in respect to STTI rector that passed away

    return

# The game starts here.

label prolog:

    stop music fadeout 1.0
    play music wayhome

    scene black with dissolve


    show text "{=chapter_intro}PROLOG{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5
    show text "{=chapter_intro}JALAN PANJANG MENUJU CAHAYA{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 2.0
    scene black with dissolve

    window hide
    scene scene1 with fade
    window show


    "{size=+4}{color=#e30d0d}Siapa Sesungguhnya raykat?{/color}{/size}"
    "Siapa yang menjadi objek dari kata yang sangat indah \"pembangunan\" yang terpampang di berbagai berita tentang pemerintahan?"
    "Apakah Partai,{w} para wakil rakyat, {w} atau pemimpin?"
    "Mereka yang berjuang untuk siapa? {w}Sebab, kata \"rakyat\" sering didengungkan."
    "Siapakah Rakyat?"
    nvl clear
    window hide
    "Apakah mereka yang berada di kota besar,{w} orang-orang kritis yang begitu percaya diri berbicara dan banyak didengarkan?"
    "Apakah orang-orang mapan yang memiliki usaha besar?"
    "Apakah aktivis yang berani berteriak di jalan-jalan menuntut ini dan itu?"
    "Atau orang-orang serperti kami,{w} yang selalu terbangun pagi dengan harapan besar akan merasakan nasib baik di hari itu karena kehidupan yang tak pasti?"
    nvl clear
    window hide
    scene scene2 with fade
    window show

    "Pemikiran ini sesungguhnya telah ada di benak saya, jauh sbelum lantai istana saya pijak."
    "Jauh sebelum nama Jokowi dikenal di Indonesia."
    "Jauh sebelum kiprah politik menjadi bagian dari hidup saya."
    "Jauh sebelum ucapan saya didengar banyak orang"
    "Saya adalah suatu dari puluhan bocah cilik yang berenang di sungai yang keruh sebagai satu-satunya kenikmatan hidup."
    nvl clear
    "Bukan,{w} kami bukan sedang piknik. {w} Rumah kami memang di bantaran sungai."
    "Bangunan dari bambu yang lembap dan berimpitan."
    "Suara gemercik air kali adalah bunyuk terindah."
    "Menyusul suara radio,{w} satu-satunya benda berbunyi sebelum kami memiliki telivisi."
    nvl clear
    "Dari Radio itulah muncul kata \"rakyat\", juga\"pembangunan\"."
    "Dua kata yang terasa tidak masuk akal ini,{w} karena kami tidak mengeti siapa subjek dan objeknya."
    "Apakah kami yang disebut rakyat?"
    "Jika iya,{w} kenapa kami tak merasakan indahnya pembangunan."
    nvl clear

    with dissolve
    show jokowibw with Dissolve(2.0)
    with Pause (1.0)

    
    j "Saya Jokowi Widodo.{w} Ini adalah kisah masa muda saya,{w} sewaktu memulai perjalanan hidup." with fade

    nvl clear
    hide jokowibw with Dissolve(2.0)
    stop music fadeout 1.0
    scene expression "#000"
    with Dissolve(3.0)
    window hide

label chapter1:

    stop music fadeout 1.0
    scene black with fade

    show text "{=chapter_intro}Bagian I{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5
    show text "{=chapter_intro}Sekolah Kehidupan dari Solo{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 2.0
    scene black with dissolve

    
    scene scene3 with fade
    play music simpleday fadein 2.0

    $ narrator = Character(None, kind=adv, callback=narrator_beep)
    window show
    "Ini saya waktu kecil.{w} Saya berasal dari kota solo jawa tengah.{w} Saya anak sulung dari empat bersaudara. {w}Tiga adik saya semuanya perempuan.
    {w}Saya berasal dari keluarga biasa. {w}"
    "Kami berulang kali pindah rumah kontrakan, rumah sederhana yang mampu dibayar bapak untuk tempat tinggal kami sekeluarga."
    scene scene4 with fade
    "Bapak berjuang, untuk hidup kami dengan berjualan bambu dan kayu dipasar.{w} Ibu sangat gigih membantu bapak.{w}"
    "Setelah selesai masak dan membereskan rumah. {w} Ia segera pergi ke lapak dagang bapak untuk membantu mengikat bambu dan kayu."
    "Mereka melakukan itu semua demi anak-anaknya demi bisa sekolah. {w} Mereka meyakinkan saya bahwa sekolah akan mampu mengubah hidup saya."
    "Perjuangan dan usaha bapak sangat menginspirasi saya. {w} Usaha bapak berjalan baik dangan makan laku dan saya tahu ibu mulai punya uang."
    "Sayapun mulai nakal waktu itu."
    "Saya iseng sering memanggil pedagang makanan apa saya yang lewat dekat rumah.{w} Tukang siomay, tukang bakso, tukang jajanan pasar."
    "Ibupun terpaksa membayar apapun yang saya pesan."
    "Suatu kali saya asal manggil saya ada tukang lewat di depan rumah."

    scene expression "#000" with Dissolve(1.0)
    scene scene5 with fade
    show jokowikecil
    pause(2.0)
    show jokowikecil at slightleft with move
    jkecil "Bu, beli kuenya satu!"
    show penjualarang at slightright with moveinright

    pjkue "Iya nak, bentar."
    "Saya pikir jual kue pasar, ternyata tukang arang."
    "Ibu muncul sebelum saya sempat berlari,{w} terpaksa ibu membelinya dan langsung meyodorkan bungkusan berisi arang untuk saya makan sambil berkata."
    scene scene6 with fade
    Sujiatmi "Ayo makan habisan, yah!"
    Sujiatmi "Kamu kan yang kepingin jajan?"

    scene scene8 with fade
    "Suatu hari kami kena gusur pemerintah daerah karena rumah kami daerah rumah kami akan dibangun fasilitas kota."
    "Kami sekeluaraga terusir begitu saja tanpa ada perhatian di mana kami akan tinggal."
    "Kejadian ini membuat kami sekeluarga sangat terpukul.{w} Kami terpaksa menumpang di rumah Paman."
    "Keadaan yang sulit membuat kami sekeluarga gigih berjuang lebih keras."
    "Bapak menjadi supir angkutan umum, setelah sekolah saya membantu Ibu berjualan di pasar meneruskan usaha Bapak."
    scene scene7 with fade
    "Kami sekeluarga menjalani hidup tanpa mengeluh dan saling mengalirkan energi positif."
    "Bersama-sama kami berjuang untuk tidak lagi menumpang.{w} Kerja keras tidak pernah sia-sia."
    "Bapak bisa membuka bengkel usaha kayu."

    scene scene10 with fade
    "Setelah beberapa tahun akhirnya uang bisa terkumpul untuk bisa membeli rumah sederhana."
    "Tahun 1980 akhirnya saya memutuskan untuk kuliah di jurusan teknologi kayu kehutanan UGM."
    "Saya memilih jurusan tersebut agar saya dapat belajar lebih mendalam tentang perkayuan."
    "Saya ingin mengikuti jejak Bapak, ingin membangun bisnis kayu bapak menjadi besar."

    stop music fadeout 2.0

label chapter2:
    
    stop music fadeout 1.0
    scene black with dissolve
    window hide

    show text "{=chapter_intro}BAB II{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5
    show text "{=chapter_intro}JALAN PANJANG MENUJU CAHAYA{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 2.0
    scene black with dissolve

    $ narrator = Character(None, kind=adv, callback=narrator_beep)
    play music simpleday fadein 2.0
    window show

    scene scene9 with fade
    "Ini saya gondrong waktu kuliah dan saya suka banget dengerin musik cadas dari Nazareth, Queen, Metallica, Judas Priest, Guns N' Roses."
    "Saya juga hobi banget naik gunung. {w} Gunung Lawu, gunung Merapi, gunung Merbabu, gunung Kerinci, sudah saya daki."
    "Menginjak masa penulisan skripsi di masa kuliah saya sudah agak kalem."
    "Akan menginjak dunia kerja saya memutuskan lebih serius."

    stop music fadeout 2.0
    scene expression "#000" with Dissolve(3.0)

    show text "{=monologue}{i}Tak lama kemudian...{/i}{/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5

    play music angel

    scene scene13 with fade
    "Saya bertemu dengan gadis bernama Iriana.{w} Dia teman adik saya yang sering main ke rumah."
    "Pertama, curi-curi pandang,{w} lama-lama jadi jatuh cinta."
    "Iriana orangnya sederhana dan itu yang saya suka."
    "Pacaran waktu itu berat di ongkos tapi ringan di hati."
    "Saya naik bus penuh sesak, bolak-balik jogja-solo demi bertemu Iriana."

    scene scene11 with fade
    "Lulus kuliah tahun 1985 saya melamar ke sebuah perusahaan Kertas Kraft Aceh."
    "Setelah diterima saya baru tahun akan ditempatkan di hutan rimba."
    "Pekerjaan saya adalah mempersiapkan persemaian pinus untuk kemudian ditanam di lapangan di hutan-hutan yang gundul."
    "Beberapa bulan setelah itu saya kembali ke solo untuk menikahi iriana, dan menyiapkan keberangkatan kami ke aceh."

    scene scene12 with fade
    "Masa awal pernikahan kami berada di hutan rimba selama 2.5 tahun."
    "Pada tahun kedua Iriana sudah dalam kondisi hamil dan kita memutuskan untuk melahirkan anak pertama kali di solo."

    scene scene14 with fade
    "Kembali ke Solo, mulai ikut paman berkerja di pabrik mebel untuk mencari pengalaman."
    "Di sini saya belajar banyak tentang bagaimana menjadi pengusaha yang baik."
    "Semua posisi pernah saya lakoni. Di produksi, di pemasaran semuanya pernah saya alami."

    scene scene15 with fade
    "Tahun 1987 anak pertama saya lahir, Gibran Rakabuming. {w}Gibran itu singkatan itu dari gigih dan berani."
    "Saya ingin putra pertama saya punya semangat hidup seperti namanya."

    scene scene16 with fade
    "Lahirnya gibran juga memicu saya untuk mendirikan perusahaan pertama saya yang bergerak di bisnis mebel, dengan nama CV RAKABU."
    "Tapi ternyata menjadi pengusaha bukanlah sesuatu yang mudah."

    scene scene17 with dissolve
    "Saya pernah habis ditipu,{w} barang sudah dikirim tapi tidak dibayar,{w} lalu orangnya menghilang."
    "Kalau kita jatuh yah harus bangkit lagi."
    "Tidak lama setelah itu saya mendapatkan pinjaman modal usaha."
    "Dengan samangat untuk bangkit dan berkembang saya bergerak cepat untuk mencari pesanan sampai luar negeri dengan cara ikut pameran-pameran mebel."
    "Hasil usaha saya mulai terlihat, kantor tidak pernah sepi dari kunjungan pembeli."

    scene scene18 with fade
    "Disini saya bertemu dengan pembeli dari perancis Bernard Chene."
    "Dia yang memberi sebuatan \"Jokowi\" untuk saya. untuk membedakan Joko Widodo dengan joko-joko lainnya yang banyak beliau kenal."
    "Sejak saat itu orang-orang lingkungan pengusaha mebel mulai memanggil saya Jokowi."

    scene scene20 with fade
    "Dua anak saya lahir setelah keadaaan ekonomi keluarga membaik."
    "Kahiyang Ayu dan Kaesang Pangarep."
    "Saya ingin anak-anak saya mengenak sekolah kehidupan yang dilandasi perjuangan untuk mandiri."
    "Supaya merupa semua mampu membangun kehidupan yang kukuh."
    "Keluarga adalah sumber kekuatan terbesar bagi saya."

    stop music fadeout (2.0)
    scene expression "#000" with Dissolve (2.0)

label chapter3:

    stop music fadeout 1.0
    scene black with dissolve
    window hide

    show text "{=chapter_intro}BAGIAN KETIGA{/=chapter_intro}" with fade:
            xalign 0.5 yalign 0.5
    pause 1.5
    show text "{=chapter_intro}THE POWER OF BLUSUKAN{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 2.0
    show text "{=monologue}{i}Saya masuk ke dunia politik dan pemerintahan awalnya tanpa rencana.\n Maju menjadi walikota karena dorongan teman-teman di organisasi.\n Anehnya, semakin saya menghindari dan menolak jalan itu,\n Semakin mudah jalan terhampar di depan mata.\n Saya artikan itu, Allah memang menginginkan saya terjun ke dalamnya.{/i}{/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 5.0
    scene black with dissolve

    $ narrator = Character(None, kind=adv, callback=narrator_beep)
    window show

    play music melodyofnature
    scene scene21 with fade
    jpot "Awal mula masuk kancah politik bukan suatu hal yang direncanakan."
    jpot "Saya tidak pernah bercita-cita terjun ke dalam dunia politik."
    jpot "Bermula dari usaha saya sebagai pebisnis perkayuan yang sudah sukses baik di nasional maupun internasional."
    jpot "Di dalam kegiatan usaha saya, saya melihat banyak pengrajin meubel atau pengrajin kayu yang nasib usahanya sangat prihatin."
    jpot "Karena tidak mampu bersaing dengan pengusaha besar."
    jpot "Saya ingin mengangkat nasib para pengrajin dan pengusaha kecil ini untuk lebih maju dalam usahanya."
    jpot "Dari sinilah saya dengan para pengusaha mebel dan kerajinan baik yang besar maupun yang kecil membuat sebuah organisasi."

    scene scene22 with fade
    jpot "Pada tahun 1988 berdirilah Asmindo, Asosiasi Pengusaha Mebel Indonesia."
    jpot "Lalu berdiri juga cabang organisasi di Surakarta pada tahun 2002 dengan nama Asmindo Komda Surakarta, dan saya terpilih sebagai ketua secara aklamasi."
    jpot "Di Asmindo inilah daya kritis saya terasah pada persoalan rakyat."
    jpot "Di Asmindo selain bisnis juga membahas akan kemajuan kota kami yaitu Solo."
    jpot "Saya ingin Solo menjadi kota yang dapat memanjukan pengusaha lokal, terutama pengusaha menengah ke bawah."
    jpot "Saya mengkritik pemerintah yang tidak dapat membuat Solo sebagai kota wisata yang dikunjungi banyak turis."
    jpot "Padahal jika dilihat Solo adalah kota budaya, tapi pariwisata di Solo sepi tidak berkembang."
    jpot "Dari kritik-kritik yang sering saya cetuskan dalam kegiatan saya sebagai pembicara."
    jpot "Diberbagai kegiatan inilah saya mulai dilirik partai politik untuk dijadikan calon walikota Solo."

    scene scene23 with fade
    jpot "Dari awal yang merupakan guyonan dan rumor, tapi makin lama rumor itu semakin berkembang."
    jpot "Saya yang dari awal memang tidak berminat terjun ke dunia politik menolak rumor tersebut."
    jpot "Namun akhirnya saya berfikir kenapa saya tidak membangun Solo dengan cara menjadi walikota?"
    jpot "Seandainya saya menjadi walikota saya dapat membangun dan mengembangkan kota Solo menjadi lebih baik."
    jpot "Tapi saya tidak langsung mengambil keputusan untuk ikut dalam pemilihan walikota."
    jpot "Saya meminta pendapat kepada istri dan anak-anak saya terlebih dahulu agar mereka tidak kaget nantinya. "
    jpot "Bagi saya suara dan pendapat keluarga sangat penting karena mereka adalah bagian hidup saya."
    jpot "Akhirnya saya siap mencalonkan diri menjadi walikota Solo berpasangan dengan FX Hadi Rudyatmo di bawah bendera Partai Demokrasi Indonesia (PDI)."

    scene scene24 with fade
    jpot "Pada tahun 2005 kami memulai kampanye pemilihan walikota Solo."
    jpot "Dalam berkampanye saya memiliki pemikiran lain dalam melaksanakan kampanye."
    jpot "Saya tidak ingin kampanye yang menyedot banyak uang."
    jpot "Saya ingin berkampanye dengan menjadi diri sendiri  yaitu rakyat biasa yang pernah hidup susah dan mampu menjadi lebih baik karena bekerja keras."
    jpot "Dibantu oleh wartawan Anggit Noegroho, saya membuat branding untuk saya sendiri sebagai rakyat biasa, disinilah saya memulai {i}blusukan.{/i}"
    jpot "Blusukan memiliki makna bukan hanya mengunjungi suatu daerah."
    jpot "Tetapi juga menjangkau suatu tempat sampai sudut terdalam, merasakan kehidupan rakyat sampai ke lorong yang tak terlihat oleh masyarakat luar."
    jpot "Dengan kampanye blusukan ini akhirnya saya dapat memenangkan pilkada Solo dan terpilih sebagai walikota dengan jumlah pemilih 37%%."
    jpot "Tantangan sebagai walikota sangat berat."
    jpot "Karena saya ingin mempertahakan kota Solo sebagai warisan budaya “Heritage” dengan mempertahankan situs-situs bersejarah, tradisi batik, dan atraksi seni"
    jpot "Sementara tuntutan zaman menginginkan perubahan yang besar."
    jpot "Tantangan terbesar saya sewaktu menjadi walikota Solo adalah menertibkan pedagang kaki lima yang berjumlah hampir 5000 pedagang."
    jpot "Tapi berkat pendekatan yang baik para pedagang akhirnya dapat dipindahkan ke tempat yang lebih pantas dan seharusnya. "

    scene scene25 with fade
    show jokowicolor with Dissolve(1.0)

    j "Selama saya memimpin Solo antara tahun 2005 hingga tahun 2012."
    j "Saya sangat bahagia telah melakukkan hal-hal yang memberi perubahan baik."
    j "Dihadapi oleh dua pilihan pada saat itu."
    j "Ingin membangun Solo sebagai kota modern atau ingin mempertahankan Solo sebagai kota budaya."
    j "Saya lakukan keduanya di dalam kondisi harmonis."
    j "{i}City Branding{/i} Solo saya bangkitkan kembali untuk membuat kota ini kembali menarik sebagai tujuan wisata."
    j "Pasar rakyat dan ruang-ruang publik berarura budaya dihidupkan."
    j "Dipercantik dengan perbaikan di sana-sini."
    j "Berbagai sentra seni diagrahkan kembali."
    j "Sementara itu, semangat {i}blusukan{/i} terus berjalan. Tak ada waktu senggang."
    j "Mengunjungi dan berdialog dengan rakyat bagaikan napas yang menghidupkan tubuh pemerintahan."
    j "Tidak boleh berhenti. Hanya saja jadi walikota, {i}blusukan{/i} dilakukan lebih dari terkonsep dan tersegementasi."
    j "Jadi saya ciptakan kegiatan rutin mengunjungi rakyat setiap hari Jumat."
    j "Namanya {i}Mider Projo{/i} yang artinya keliling kota dan kamping."
    j "Jadi, setelah olahraga pagi di hari Jumat, dengan bersepeda saya menuju satu wilayah bersama jajaran staf."
    j "Masih mengenakan baju olahraga saja, memasuki wilayah pelosok Solo yang memang tidak mungkin memakai kenadaraan karena banyak gang kecil."
    j "Nah, pada saat {i}mider projo{/i} inilah saya bisa mendata lagi persoalan rakyat dan melihat hal-hal tak beres yang bisa ditolong."
    j "Apa yang terjadi di Solo di masa saya menjadi walikota menuai banyak pujian juga kritikan."
    j "Banyak yang bilang Jokowi Pencitraan. Sengaja menggeber aksi-aksi heroik agar dipuji secara nasional."
    j "Saya sungguh heran dengan pandangan ini."
    j "Apa yang saya lakukan itu memang sesuatu yang harus dilakukan. Tak ada yang berlebihan."
    j "Memang yang seharusnya itu yang dilakukan Pemerintah Kota Solo. Bukan hal yang istimewa."
    j "Kita tanpa sadar berada di zona nyaman yang tidak beres dianggap wajar sehingga,"
    j "Ketika ada sesuatu yang sebetulnya wajar justru dianggap pencitraan."

    nvl clear
    hide jokowicolor with Dissolve(1.0)
    stop music fadeout 1.0
    scene expression "#000"
    with Dissolve(1.0)

    scene black with dissolve

    show text "{=monologue}7 tahun setelah diangkat menjadi Walikota...{/monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5

    show text "{=monologue}Maret 2012{/monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5

    scene black with dissolve

    #recheck
    play music triumph
    scene scene26 with fade
    "Pada 17 Maret 2012, ponsel saya berdering saat saya sedang asyik menonton pentas Opera Van Java."
    "Kaget, SMS dari Ibu Megawati yang merupakan tokoh besar dari PDI Perjuangan."
    "Saya diminta segera ke Jakarta esok pagi dengan pesawat yang paling pagi."
    "Agendanya, saya diminta mengikuti rapat yang digelar DPP dan DPD PDIP di markas besar di tebet."
    "Dengan segera saya mengontak Anggit, meminta agar ia mendampingi saya."
    "Saya juga mengajak Hanggo yang merupakan ajudan saya."

    scene scene27 with fade
    "Setibanya di sana bukan main terkejutnya saya melihat keriuhan susana di sekitar kantor DPP PDIP."
    "Wartawan merubung saya ketika saya berjalan menuju gerbang kantor"
    "Pertanyaan-pertanyaan yang menysasar ke satu topik yang tajam bersahutan."

    wartawan1 "Pak, Bapak akan maju ke Pilkada DKI?"
    wartawan2 "Pak Jokowi sudah mengetahui perihal akan dicalonkan jadi gubernur"
    "Saya tertawa. Bukan terawa tenang, tapi tertawa bingung"
    "Saya tinggalkan para wartawan dan masuk ke dalam gedung markas besar PDIP"

    scene scene28 with flash
    play audio clap1
    "Di dalam, saya sangat terkejut. Tepuk tangan meriah menyambut saya."
    "Saya masih belum bisa mengusai diri karena terkejut."
    "Ini {i}surprise{/i}. Tidak saya sangka ada sambutan sebegini hangat dan meriah. Ada apa?"
    "Apa yang dibicarakan?"
    "Ternyata rapat memutuskan saya untuk maju ke Pilkada DKI Jakarta, calon PDI Perjuangan."
    "Suara tepuk tangan gegap gempita. Saya terhenyak. Bunyi Riuh tepuk tangan terus membahana."
    "Saya tak menduga akan dipercaya dan didukung sebesar ini."
    "Rapat itu hanya berlangsung selama menit dan saya langsung pamit ke hotel bersama Anggit dan Hanggo."

    scene scene28 with fade
    "Esok harinya berlangsunglah rapat untuk memutuskan calon Wakil saya."
    "Waktu terus berjalan dan akhirnya rapat memutuskan Pak Ahok menjadi wakil saya."
    "Namun tidak semua berjalan dengan lancar."
    "Banyak rakyat memiliki opini tentang saya dengan alasan Saya tidak amanah karena tugas masih berjalan di Solo tapi saya sudah melompat ke Jakarta."

    scene extra1 with fade
    "Di dalam keluarga saya sendiri terjadi Penolakan."
    "Istri saya mengeluh karena alasan orang tentang berganti kepemimpinan sebelum selesai menjalankan."
    "Sedangkan anak saya Gibran hanya menyengir ketika saya meminta izin."
    gibran "Bapak yakin ingin ikut pilkada?"
    j "Bapak yakin menang."
    "Anak-anak saya sudah terbiasa mendegar celetukan saya yang kelewat percaya diri."
    "Tapi, saat itu saya memang yakin akan menang. Entah kenapa."
    "Ketiga anak saya, walau tidak setuju, selalu memberi pandangan positif dan teduh."
    "Walaupun mereka menolak, bukan karena tak suka dan percaya."
    "Namun untuk meyakinkan saya apa bisa saya jadi Gubernur."

    scene scene29 with fade
    "Kampanye dilakukan dengan dana seadanya. Tanpa kemewahan."
    "Tidak lama kemudian setelah kampanye berakhir, Saya dan Pak Ahok berhasil memenangkan pilkada yang sangat emosional saat itu."
    "Tahun 2012 kami dilantik menjadi Gubernur dan Wakil Gubernur DKI Jakarta periode 2012-2017."

    show text "{=monologue}{i}Lembaran perjalanan baru dimulai...{/i}{/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 3.0

    scene black with dissolve
    show text "{=monologue}{i}Dua tahun saya memimpin Jakarta,\n panggilan yang lebih besar kemudian datang.{/i}{/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 2.0
    show text "{=monologue}{i}PDIP memajukan saya sebagai contoh kuat di Pemilihan Presiden 2014.{/i}{/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 3.0

    $ narrator = Character(None, kind=nvl, callback=narrator_beep)
    scene scene30 with fade
    "Prinsip Kepemimipinan saya selalu sama, baik di Solo maupun Jakarta. Mencari masalah sampai ke akarnya, berani mengurai dan melakukan upaya untuk meneyelesaikannya,"
    "Sambil membangun energi positif untuk bersama-sama melihat tujuan baik."
    "Bersama-sama meilhat tujuan baik, inilah rahasia yang penting itu."
    "Ya, sebuah wilayah tidak akan maju jika hanya menuruti ambisi pemimpin yang tidak pernah diketahui rakyatnya."
    "Sebuah wilayah juga tiadk akan maju jika sang pemimpin terlalu populis,dan sibuk menghibur rakatnya dengan hadiah-hadiah yang menyenangkan rakatnya dengan hadiah-hadiah menyenangkan"
    nvl clear
    
    "Yang tidak berdampak baik untuk jangka panjang."
    "Sebuah wilayah pun tak akan maju ketika sang pempimpin gentar melakukan tindakan yang perlu dilakukan dan memilih memilihara problem."
    "Maka kunci kemajuan sebuah wilayah pertama=tama adalah mindset sang pemimpin terlebih dulu karena ia yang akan menggerakkan."
    "Masalah akan terus menjadi masalah jika sepakat menyuburkannya dan berpikir bahwa kita tak bisa mencari jalan keluar."
    "Masalah akan teratasi, walau prosesnya butuh waktu, jika kita berani mengakui itu dan memulai langkah berani untuk membenahinya."

    nvl clear

    "Demikianlah, dari Jakarta saya didorong untuk mengikuti pemilihan presiden pada tahun 2014."
    "Ini perkembangan amanah. Saya Menyetujui maju bersama Pak Jusuf Kalla."
    "Sekali lagi, ini bukan tentang keinginan untuk memanfaatkan kesempatan dan meraih pencapaian yang lebih tinggi.{w} Saya harus meluruskan ini."
    "Bahwa ini bukan tentang Ambisi.{w} Bukan tentang syahwat berkuasa."
    "Ini adalah sebuah jalan pengabdian yang terus berproses dan menemukan jalan-jalan baru pengabdian secara alamiah."
    
    nvl clear
    
    "Takdir telah mengantarkan saya memimpin Solo dan mengurai persoalan-persoalan disana."
    "Sesuatu yang kemudian diendus oleh Jakarta. Jakarta mengundang saya."
    "Memberi tantangan pada saya utnuk mengurai persoalan-persoalan di kota ini."
    "Itu terendus oleh masyarakat dalam skala nasional. Apakah itu bisa saya ciptakan dengan hanya bermodalkan keinginan?"
    "Kepercayaan itu datang karena proses kerja dan hasil. Pada satu titik akhirnya saya mengerti bahwa manusia yang terus bertumbuh, menambah kepasistas karyanya, mampu memperluas dampak manfaat, maka ia tidak bisa terhindar sebagai tumpuan harapan."
    nvl clear
    "Saya ada di posisi itu."
    "Maka saya sambut tantangan itu, Saya maju bersama Pak Jusuf Kalla. Saya sangat ingin mengalirkan energi dan rona baru kepemimpinan untuk bangsa ini."
    "Bangsa yang sesungguhnya memiliki semangat dan kemampuan hebat untuk bisa berkali-kali lipat lebih baik."

    nvl clear

    scene black with dissolve
    show text "{=chapter_intro}Pilihan Membumi{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    
    scene scene30 with fade

    "Keluarga saya agaknya terlatih untuk dewasa dan tak kaget lagi dengan perkembangan pengabdian saya."
    "Gibran, Kahiyang, dan Kaesang semakin paham langkah ayah mereka sudah bukan lagi urusan keluarga, tapi urusan masyarakat luas."
    "Ketika sebelumnya saya hendak mulai berkampaye, tidak ada lagi tanya jawab tentang apakah saya diizinkan. Ketiganya sudah lebih dulu bicara pada saya."
    "Saya berpamitan untuk kampanye pada mereka. Saya katakan bhwa hari-hari kampanye akan berlangsung dengan tajam."
    "People power. Ke mana pun saya bergerakm saya melihat kehadiran mereka dengan berbagai aksi dukungan heroik."

    nvl clear

    "Suatu hari seorang relawan perempuan mengatakan sesuatu pada saya,"
    "\"Pak Jokowi, saya mau memberikan waktu dengan energi saya sepanjang masa kampanye ini demi mendukung Bapak dan Pak JK.\"\"Karena saya yakin Pak Jokowi akan menangkat kami menuju kehidupan yang lebih baik.\""

    "Ucapan itu membuat saya sangat terharu. Karena keinginan kuat dan keyakinan bahwa hari esok bisa diperjuangkan untuk menjadi lebih baik, mereka memberikan dukungan dahsyat kepada calon pemimpin yang mereka percaya."
    "Bagi saya ini adalah suntikan energi sekaligus juga lecutan untuk bisa menjawab harapan mereka."

    nvl clear

    "Sepanjang masa masa kampanye itu nyaris saya tidak punya waktu istrirahat. Setiap hari bergerak."
    "Di sekujur  Jakarta, luar kota, juga luar pulau. Bersama Pak Jusuf Kalla saya bahu-membahu meyakinkan rakyat bahwa kami bisa memimpin Indonesia dengan baik."

    
    stop music fadeout 2.0
    scene expression "#000" with Dissolve (2.0)

label chapter4:

    nvl clear
    window hide

    stop music fadeout 1.0
    scene black with dissolve
    show text "{=chapter_intro}EPILOG{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5
    scene black with dissolve

    scene black with fade

    $ persistent.finish == True
    play music cinema_ambient fadein 3.0
    scene end1_1 with dissolve

    $ narrator = Character(None, kind=adv, callback=narrator_beep)
    window show
    "Mei 2014"
    
    j "Saya dan Pak Jusuf Kalla akhirnya memenangkan pertarungan yang sangat emosional itu."
    j "Setelah melalui perdebatan hasil pilpres, kami akhirnya diakui secara sah sebagai pemenang pilpres."
    j "Luar biasa gegap gempita teriakan pendukung yang menyambut kemenangan saya dan Pak Jusuf Kalla."
    j "Ibu Megawati menggelar temu pers di rumahnya di Jagakarsa, Jakarta Selatan."
    j "Halaman rumah itu penuh sesak. Semua pendukung utama selama masa kampanya hadir, juga para pimpinan PDIP serta partai pendukung lainnya."
    j "Di antara gegap gempita susana di rumah Ibu Megawati, perasaaan saya berkalana di dalam lorong sunyi batin saya."
    j "Saya tahu bahwa di depan nanti akan ada tantangan yang akan saya hadapi luar biasa dashatnya."
    j "Saya bukan lagi memimpin Solo dan Jakarta."
    j "Tapi, Indonesia, negara dengan penduduk lebih dari 260 juta jiwa, memliki 17 ribu pulau, 714 suku, dan 34 provinsi."
    j "Kita bangsa yang hebat."
    j "Kita pasti bisa menciptakan perubahan yang baik."
    j "Saya yakin yang saya alami waktu muda sedang kalian alami sekarang."
    j "Tidak ada jokowi hari ini jika tidak ada sejarah susah hidup saya."
    j "Teruslah berjuang mewujudkan mimpi-mimpi kalian."
    j "{cps=10}Salam dari Joko Widodo.{/cps}"

    scene black with dissolve
    show text "{=monologue}Acara pelantikan pertama Joko Widodo (Jokowi) sebagai Presiden ke-7 Indonesia dilakukan di Gedung DPR/MPR,\n Jakarta pada tanggal 20 Oktober 2014 .{/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5
    scene black with dissolve
    show text "{=monologue}Acara ini menandai secara resmi dimulainya masa jabatan pertama Joko Widodo sebagai Presiden dan\n masa jabatan kedua dan terakhir Jusuf Kalla sebagai Wakil Presiden Indonesia. {/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5
    scene black with dissolve
    show text "{=monologue}Keduanya dilantik setelah memenangkan pemilihan umum presiden pada 9 Juli 2014. {/=monologue}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 1.5
    scene black with dissolve
    

    $ show_quick_menu = False
    $ _game_menu_screen = None
    $ _dismiss_pause = False
    $ _skipping = True
    $ _rollback = False
    window hide

    scene black with fade

    call credits from _call_credits

    show extrashade
    return


label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene scene30
    with dissolve
    show extrashade
    show text "{=chapter_intro}VISUAL NOVEL BIOGRAFI JOKO WIDODO{/=chapter_intro}" with Dissolve(1):
            xalign 0.5 yalign 0.5
    pause 2.0
    scene expression "#000" with dissolve
    show cred at Move((0.5, 3.5), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    scene white with fade
    show stticred:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    #fix
    scene end1_3 with fade
    
    "Terima kasih karena telah menyelesaikan Biografi Jokowi Widodo."
    "Visual Novel Novel Jokowi Berakhir."

    return

label quiz:
    
    stop music fadeout 1.0
    $ _rollback = False
    $ narrator = Character(None, kind=adv, callback=narrator_beep)
    $ show_quick_menu = False
    
    scene quiz with fade

    play music question fadein 2.0

    show jokowicolor with Dissolve(1.0)
    with Pause (1.0)
    
    j "Selamat datang di bagian Quiz."
    j "Anda akan diberikan beberapa pertanyaan berdasarkan Latar belakang Joko Widodo yang ada di Visual Novel ini."
    j "Ambil waktu Anda dan Silahkan menjawab dengan baik."

    hide jokowicolor with fade


    "Pertanyaan Pertama."

label pertanyaan1:

$ rng = renpy.random.randint(1,2)

if rng == 1:

    "Dari mana Jokowi berasal?"

    menu:
            "Dari mana Jokowi berasal?"
            "Kota Solo Jawa Tengah":
                $ point += 1
            

            "Jakarta":
                $ point += 0

    jump pertanyaan2


elif rng == 2:


    "Apakah nama penuh dari Jokowi?"

    menu:
            "Nama penuh Jokowi?"
            "Joko Widodo":
                $ point += 1
            

            "Jokowi Widodo":
                $ point += 0

label pertanyaan2:

    "Pertanyaan Kedua."

$ rng = renpy.random.randint(1,2)

if rng == 1:

    "Apa nama penuh Ibunda Joko Widodo?"

    menu:
            "Apa nama penuh Ibunda Joko Widodo?"
            "Sujiatmi Notomihardjo":
                $ point += 1

            "Wiroredjo Notomihardjo":
                $ point += 0
                
            "Sani Notomihardjo":
                $ point += 0

    jump pertanyaan3    


elif rng == 2:

    "Berapa saudara kandung Jokowi miliki?"

    menu:
            "Saudara kandung Jokowi miliki?"
            "Dua":
                $ point += 0

            "Tiga":
                $ point += 0

            "Empat":
                $ point += 1

    jump pertanyaan3


label pertanyaan3:

    "Pertanyaan Ketiga."

$ rng = renpy.random.randint(1,2)

if rng == 1:

    "Dimanakah Jokowi Pernah berkuliah pada tahun 1980?"

    menu:
            "Dimanakah Jokowi Pernah berkuliah?"
            "Teknologi Kayu Kehutanan Universitas Gajah Mada.":
                $ point += 1

            "Teknologi Mesin Universitas Gajah Mada":
                $ point += 0
            
            "Teknologi Kayu Institut Teknologi Bandung":
                $ point += 0


    jump pertanyaan4

elif rng == 2:

    "Apa usaha yang dilakukan Orang Tua Joko Widodo saat ia masih anak-anak?"

    menu:
            "Usaha yang dilakukan Orang Tua Joko Widodo?"
            "Menjual Bambu dan Kayu dipasar":
                $ point += 1

            "Pedagang Kaki Lima":
                $ point += 0
            
            "Petani":
                $ point += 0

    jump pertanyaan4
    
label pertanyaan4:

    "Pertanyaan Keempat."

$ rng = renpy.random.randint(1,2)

if rng == 1:

    jpot "Pertanyaan ini agak personal namun, Apakah Hobi Joko Widodo?."

    menu:
            "Apa Hobi Joko Widodo?"
            "Mendaki gunung.":
                $ point += 1
            

            "Bermain Game":
                $ point += 0
            
            "Boxing":
                $ point += 0
    
    "Benar Hobbi Saya adalah mendaki gunung."
    "Pertanyaan Kelima."
    
    jump pertanyaan5

elif rng == 2:

    "Apa tujuan dari Joko Widodo memilih masuk ke Universitas Kehutanan?"

    menu:
            "Tujuan Joko Widodo memilih Universitas yang mendalami tentang Teknologi Kehutanan?"
            "Membangun bisnis kayu Orang tuanya menjadi lebih besar":
                $ point += 1
            
            "Membangun Teknologi yang dapat membangun hutan Indonesia menjadi lebih baik":
                $ point += 0
            
    jump pertanyaan5

label pertanyaan5:

    "Pertanyaan kelima"

$ rng = renpy.random.randint(1,2)

if rng == 1:

    "Siapakah nama Istri Joko Widodo?"

    menu:
            "Siapakah nama Istri Joko Widodo?"
            "Iriana":
                $ point += 1
            
            "Iriani":
                $ point += 0

            "Sri Sunarni":
                $ point += 0
    
    jump pertanyaan6
    
elif rng == 2:

    "Apa nama Perusahaan kertas yang Jokowi lamari setelah ia lulus pada tahun 1985?"

    menu:
            "Apa nama perusahaan kertas yang Jokowi lamari pada tahun 1985?"
            "Kertas Kraft Aceh":
                $ point += 1
            
            "Paper Box Indonesia":
                $ point += 0

            "Indo Kreasi Grafika":
                $ point += 0

    jump pertanyaan6
                 
label pertanyaan6:

    "Pertanyaan Keenam."
    
$ rng = renpy.random.randint(1,2)

if rng == 1:
    
    "Apa nama Perusahaan pertama Joko Widodo"

    menu:
            "Apa nama Perusahaan pertama Joko Widodo"
            "Freeport":
                $ point += 0
            
            "CV RAKABU":
                $ point += 1

            "Asmindo":
                $ point += 0

    
    jump pertanyaan7

elif rng == 2:

    "Siapakah nama anak pertama Joko Widodo yang lahir pada tahun 1987"

    menu:
            "Nama anak pertama Joko Widodo?"
            "Kahiyang Ayu":
                $ point += 0
            
            "Gibran Rakabuming":
                $ point += 1

            "Kaesang Pangarep":
                $ point += 0

    jump pertanyaan7
            
label pertanyaan7:

    "Pertanyaan Ketujuh."

$ rng = renpy.random.randint(1,2)

if rng == 1:
        
    "Tahun berapakah Joko Widodo Naik menjadi Walikota di Solo dan berapa lama?"

    menu:
            "Tahun berapakah Joko Widodo Naik menjadi Walikota di Solo dan berapa lama?"
            "2003 sampai 2012":
                $ point += 0
            
            "2003 sampai 2008":
                $ point += 0

            "2005 sampai 2012":
                $ point += 1

    jump pertanyaan8

elif rng == 2:

    "Siapakah yang memberi nama pembeli dari Prancis yang memberi sebutan Joko Widodo 'Jokowi' "

    menu:
            "Siapa nama pembeli dari Prancis yang memberi sebutan 'Jokowi'?"
            "Bernando Torres":
                $ point += 0
            
            "Barrack Obama":
                $ point += 0

            "Bernard Chene":
                $ point += 1

    jump pertanyaan8

label pertanyaan8:
    
    "Pertanyaan Kedelapan."

$ rng = renpy.random.randint(1,2)

if rng == 1:
        
    "Pada saat pemilihan kepala daerah 2012 di DKI Jakarta."
    "Siapakah yang menjadi Wakil Gubernur Joko Widodo?"

    menu:
            "Siapakah yang menjadi Wakil Gubernur Joko Widodo pada tahun 2012 DKI Jakarta?"
            "Basuki Tjahaja Purnama/Ahok":
                $ point += 1
            
            "Prabowo Subianto":
                $ point += 0

            "Megawati Soekarno Putri":
                $ point += 0

    jump pertanyaan9

elif rng == 2:

    "Siapakah pasangan Joko Widodo saat ia mencalonkan diri menjadi walikota solo pada tahun 2003 sampai 2012?"

    menu:    
            "Siapakah pasangan Joko Widodo saat ia mencalonkan diri menjadi walikota solo pada tahun 2003 sampai 2012?"
            "FX Hadi Rudyatmo":
                $ point += 1
            
            "Ahok":
                $ point += 0

            "Slamet Suryanto":
                $ point += 0

    jump pertanyaan9
            
label pertanyaan9:

    "Pertanyaan Kesembilan."

$ rng = renpy.random.randint(1,2)

if rng == 1:
        
    "Siapakah Wakil Presiden Joko Widodo saat Pemilihan Presiden ke-7?"

    menu:
            "Siapakah Wakil Presiden Joko Widodo saat Pemilihan Presiden ke-7?"
            "Ma'ruf Amin":
                $ point += 0
            
            "Jusuf Kalla":
                $ point += 1

            "Boediono":
                $ point += 0

    jump pertanyaan10

elif rng == 2:

    "Apakah metode yang sangat dikenal saat Joko Widodo berkampanye untuk menemui dan berkomunikasi rakyat?"

    menu:
            "Nama metode yang dilakukan Jokowi sangat terkenal?"
            "Parade Sederahana":
                $ point += 0
            
            "Blusukan":
                $ point += 1

    jump pertanyaan10
    
label pertanyaan10: 

    "Pertanyaan Kesepuluh."
        
    "Kapan Pelantikan Presiden ke-7 Joko Widodo dilaksanakan?"

    menu:
            "Kapan Pelantikan Presiden ke-7 dilaksanakan?"
            "20 Oktober 2014 ":
                $ point += 1
            
            "24 Oktober 2014":
                $ point += 0

            "20 Desember 2014 ":
                $ point += 0
    
    
    show jokowicolor with dissolve
    j "Jumlah point anda adalah ...."
    j "[point] Poin!"
   
    if point >= 10:
        j "Selamat karena telah menjawab dengan hasil yang Sempurna. Luar Biasa"
        "Kembali ke menu"
        return
    elif point >= 7:
        j "Selamat karena telah menjawab dengan hasil yang Baik."
        "Kembali ke menu"
        return
    elif point >= 5:
        j "Selamat karena telah menjawab dengan hasil yang Cukup."
        "Cobalah bermain quiz lagi!"
        "Kembali ke menu"
        return
    elif point >= 1:
        j "Tidak masalah jika anda belum mendapatkan point yang baik."
        "Kegagalan merupakan sukses yang tertenda. Coba Kembali!"
        "Kembali ke menu"
        return
    else:
        j "Untuk medapatkan Angka 0 itu sebenarnya cukup mengagumkan. Antara sengaja atau belum memulai cerita Biografi Saya."

        show jokowicolor at Shake((0.50, 0.60, 0.5, 0.5), 3.0, dist=10)
        j "Silahkan coba ulang dan menjawab dengan benar."
        "Kembali ke menu"

        return


