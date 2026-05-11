from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>

    <head>

        <title>Happy Sweet 21 Adik Jeno ♡</title>

        <style>

            body{
                background:#b7e4c7;
                text-align:center;
                font-family:Arial;
                padding-top:40px;
            }

            h1{
                color:white;
                font-size:50px;
            }

            p{
                color:white;
                font-size:25px;
                margin:30px;
                line-height:45px;
            }

            .gallery{
                display:flex;
                flex-wrap:wrap;
                justify-content:center;
                gap:20px;
                margin-top:30px;
            }

            .gallery img{
                width:200px;
                height:200px;
                object-fit:cover;
                border-radius:20px;
                box-shadow:0px 0px 15px white;
            }

            button{
                background:white;
                color:#52b788;
                border:none;
                padding:15px 30px;
                font-size:20px;
                border-radius:15px;
                cursor:pointer;
                margin-bottom:30px;
            }

        </style>

    </head>

    <body>

        <h1>Happy Sweet 21 Adik Jeno ♡</h1>

        <button onclick="playMusic()">
            Play Music ♡
        </button>

        <audio id="music" loop>
            <source src="/static/bsb.mp3" type="audio/mpeg">
        </audio>

        <script>
        function playMusic() {
            var music = document.getElementById("music");
            music.volume = 0.3;
            music.play();
        }
        </script>

        <div class="gallery">

            <img src="/static/naila1.jpeg">
            <img src="/static/naila2.jpeg">
            <img src="/static/naila3.jpeg">
            <img src="/static/naila4.jpeg">
            <img src="/static/naila5.jpeg">
            <img src="/static/naila6.jpeg">
            <img src="/static/naila7.jpeg">
            <img src="/static/naila8.jpeg">
            <img src="/static/naila9.jpeg">
            <img src="/static/naila10.jpeg">

        </div>

        <p>
        happy sweet 21 adik ♡.<br><br>

        today is your birthday, dan jujur aku masih ga nyangka ternyata kita udah kenal selama ini. dari 2020 sampai sekarang, banyak banget hal yang udah dilewatin, dan aku seneng karena di semua waktu itu kita masih tetep saling kenal sampai hari ini.<br><br>

        aku cuma mau bilang makasih banyak yaa, karena tanpa sadar kamu udah jadi salah satu orang yang selalu ada di banyak cerita hidup aku.<br><br>

        makasih karena udah jadi sahabat yang baik, yang selalu bikin suasana jadi lebih nyaman dan hangat.<br><br>

        dan yang paling penting, makasih yaa karena udah mau bertahan sejauh ini. aku tau hidup ga selalu gampang, tapi kamu hebat karena masih bisa sampai di titik sekarang.<br><br>

        aku harap di umur 21 ini kamu bisa lebih bahagia, lebih tenang, dan lebih sering ketawa.<br><br>

        semoga semua hal baik dateng ke hidup kamu satu satu, semoga kamu selalu sehat, panjang umur, dan semua yang kamu harapin bisa tercapai pelan pelan.<br><br>

        kalau suatu hari kamu capek, jangan lupa istirahat yaa. kamu ga harus selalu kuat setiap waktu.<br><br>

        tetap jadi adik yang aku kenal selama ini.<br><br>

        dan semoga suatu hari nanti kamu bisa ketemu jeno lagi.<br><br>

        maaf yaa kalau web ini masih sederhana dan maaf juga karena aku baru bisa bikin sekarang. tapi aku bikin ini dengan tulus karena aku pengen kamu punya sesuatu buat diinget di ulang tahun kamu tahun ini.<br><br>

        once again, happy sweet 21 adik ♡.<br><br>

        with love, jeje pacar jake ♡
        </p>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)