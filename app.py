from flask import Flask, request, render_template_string

app = Flask(__name__)

contents = {
    "3 Idiots": ["happy", "relaxed", "https://theshesaga.com/wp-content/uploads/2025/09/2_20250906_214134_0001.png"],
    "Zindagi Na Milegi Dobara": ["happy", "excited", "relaxed", "https://www.acmodasi.in/amdb/images/movie/n/f/zindagi-na-milegi-dobara-2011-0pjbjb.jpg"],
    "Queen": ["happy", "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=3148693441967446"],
    "Piku": ["happy", "relaxed", "https://media.cinemaexpress.com/cinemaexpress%2F2025-04-19%2Fgiokhgc9%2FPiku.jpg?w=480&auto=format%2Ccompress&fit=max"],
    "Hera Pheri": ["happy", "https://m.media-amazon.com/images/M/MV5BMTliMjJlODMtN2I5Yi00OTBlLWFlMTctYWJmMWMzMjBmNGFhXkEyXkFqcGc@._V1_.jpg"],
    "Munna Bhai M.B.B.S.": ["happy", "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3526307400693563750"],
    "Chupke Chupke": ["happy", "relaxed", "https://m.media-amazon.com/images/I/617u-vB4CHL._AC_UF894,1000_QL80_.jpg"],
    "Jaane Tu... Ya Jaane Na": ["happy", "romantic", "https://www.bollywoodhungama.com/wp-content/uploads/2024/07/Jaane_Tu_Ya_Jeena_Na_Turns_16.jpg"],
    "Yeh Jawaani Hai Deewani": ["happy", "excited", "romantic", "https://img.indiaforums.com/media/800x0/64/4002-yeh-jawaani-hai-deewani.webp"],
    "Barfi!": ["happy", "romantic", "https://mir-s3-cdn-cf.behance.net/projects/808/994e17226005111.Y3JvcCw1NTAwLDQzMDEsMCw5NQ.jpg"],
    "Chhichhore": ["happy", "relaxed", "https://cdn.dnaindia.com/sites/default/files/styles/full/public/2018/10/09/741503-chichore-poster.jpg"],
    "Badhaai Ho": ["happy", "https://i.ytimg.com/vi/QClekWtc_rQ/maxresdefault.jpg"],
    "Dil Chahta Hai": ["happy", "relaxed", "https://as2.ftcdn.net/jpg/04/56/72/81/1000_F_456728129_mCy093Uth61pndEISQDu4LhZVay9R8Yr.jpg"],
    "Lagaan": ["happy", "excited", "https://i.etsystatic.com/35339233/r/il/8bdc48/5733121512/il_fullxfull.5733121512_6api.jpg"],
    "Kal Ho Naa Ho": ["sad", "romantic", "https://i.ytimg.com/vi/qgb7MME_CTc/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAN0WmihsRq_aUFQOuofHHDuRkIIQ"],
    "Rockstar": ["sad", "romantic", "https://posterboizz.in/cdn/shop/files/Rockstar-webp_1.jpg?v=1755552973&width=1946"],
    "Taare Zameen Par": ["sad", "happy", "https://www.iwmbuzz.com/wp-content/uploads/2025/08/aamir-khan-productions-sitaare-zameen-par-ai-style-announcement-steals-the-show-now-available-for-e282b9100-on-youtube.jpg"],
    "Anand": ["sad", "happy", "https://images.news18.com/ibnlive/uploads/2025/07/Guru-Dutt-AI-posters-2025-07-af322d2a4caefc01164ea4137b8dd60f-16x9.jpg"],
    "Veer-Zaara": ["sad", "romantic", "https://i.etsystatic.com/26820471/r/il/91d6cb/5106077624/il_570xN.5106077624_ln9j.jpg"],
    "Dilwale Dulhania Le Jayenge": ["romantic", "happy", "https://img.buzzfeed.com/buzzfeed-static/static/2015-10/20/3/enhanced/webdr13/original-22596-1445325601-1.jpg"],
    "Jab We Met": ["romantic", "happy", "https://i.etsystatic.com/27699529/r/il/e034eb/3185606278/il_fullxfull.3185606278_l5br.jpg"],
    "Kabhi Khushi Kabhie Gham": ["romantic", "happy", "https://i.etsystatic.com/27699529/r/il/d99816/3237205285/il_fullxfull.3237205285_51of.jpg"],
    "Aashiqui 2": ["romantic", "sad", "https://img2.freejobalert.com/news/2025/09/aashiqui-2-movie-poster-editing-68ce4c3205e4166683596-1200.webp"],
    "Baahubali: The Beginning": ["excited", "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3743235454172072909"],
    "Baahubali 2: The Conclusion": ["excited", "https://mir-s3-cdn-cf.behance.net/project_modules/max_632_webp/9ea83849455613.58b57541375e3.jpg"],
    "RRR": ["excited", "https://images.news18.com/ibnlive/uploads/2024/12/rrr_-behind-and-beyond_-makers-confirm-documentary-on-ss-rajamouli-directorial-share-first-poster-2024-12-de99d0120576d87019069c58505c25da-3x2.jpg"],
    "KGF: Chapter 2": ["excited", "https://c.ndtvimg.com/2022-01/m6urjsug_yash-_625x300_08_January_22.jpg"],
    "Pathaan": ["excited", "https://m.economictimes.com/thumb/msid-96029666,width-1200,height-900,resizemode-4,imgsize-65784/pathaan-poster-release-srk-returns-with-a-bang-in-new-film-check-here.jpg"],
    "Andhadhun": ["excited", "https://feminisminindia.com/wp-content/uploads/2019/01/andhadhun-poster.jpg.webp"],
    "Uri: The Surgical Strike": ["excited", "https://static.toiimg.com/thumb/msid-65993765,width-1070,height-580,imgsize-57226,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg"],
    "Andaz Apna Apna": ["relaxed", "happy", "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=655181923953523"],
    "English Vinglish": ["relaxed", "happy", "https://filmfare.wwmindia.com/content/2012/Jun/600x450_1339753042.jpg"],
    "Panchayat (Series)": ["relaxed", "happy", "https://s.yimg.com/ny/api/res/1.2/LSsbD8DDmwauj1wJuhgl2w--/YXBwaWQ9aGlnaGxhbmRlcjt3PTIwNDg7aD0xMTUyO2NmPXdlYnA-/https://media.zenfs.com/en/comingsoon_net_477/b7a54c8a22c1625a90692154064baa90"],
    "Gullak (Series)": ["relaxed", "happy", "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3381370096075397763"],
    "Mirzapur (Series)": ["excited", "https://s.yimg.com/ny/api/res/1.2/AsHYfN2DsmUthQvYUvomeA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTIwNDg7aD0xMTUyO2NmPXdlYnA-/https://media.zenfs.com/en/comingsoon_net_477/61e311cb69b272a2ffab426235f8993d"],
}

possible_moods = ['happy', 'sad', 'romantic', 'excited', 'relaxed']

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MoodFlix</title>
        <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
        <style>
            body, html {margin:0;padding:0;background:#141414;color:#fff;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;}
            .hero {background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.8)), url('https://i.etsystatic.com/25516846/r/il/28a604/3865202010/il_fullxfull.3865202010_hjku.jpg') center/cover no-repeat;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box;}
            h1 {font-family:'Bebas Neue',cursive;font-size:clamp(4rem, 12vw, 8rem);margin:0;letter-spacing:4px;text-shadow:0 4px 20px rgba(0,0,0,0.9);}
            .tagline {font-size:clamp(1.2rem, 5vw, 2rem);margin:20px 0 40px;max-width:90%;}
            .btn {background:#e50914;color:#fff;padding:16px 40px;font-size:clamp(1.2rem, 4vw, 1.8rem);border:none;border-radius:4px;cursor:pointer;transition:background 0.3s;margin:10px;}
            .btn:hover {background:#f40612;}
        </style>
    </head>
    <body>
        <div class="hero">
            <h1>MoodFlix</h1>
            <p class="tagline">Discover the perfect Indian movie or series based on your mood</p>
            <div>
                <a href="/single" class="btn">Single Mood</a><br>
                <a href="/multi" class="btn">Group Mood</a>
            </div>
        </div>
    </body>
    </html>
    '''

common_style = '''
<style>
    body {background:#141414;color:#fff;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;margin:0;padding:0;min-height:100vh;}
    h1 {text-align:center;padding:40px 0;font-size:clamp(2rem, 8vw, 3rem);}
    .container {max-width:1400px;margin:0 auto;padding:20px;}
    .grid {display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:20px;}
    .card {position:relative;overflow:hidden;border-radius:8px;box-shadow:0 4px 15px rgba(0,0,0,0.6);transition:transform 0.3s;cursor:pointer;background:#221f1f;height:250px;display:flex;align-items:center;justify-content:center;}
    .card:hover, .card:active {transform:scale(1.08);}
    .card img {width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;}
    .card h3 {position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,0.8);padding:15px;margin:0;font-size:1.2rem;text-align:center;z-index:1;}
    .mood-text {font-size:clamp(1.5rem, 6vw, 3rem);color:#e50914;z-index:1;}
    a.back {display:block;text-align:center;margin:40px 0;color:#e50914;font-size:1.2rem;text-decoration:none;}
    a.back:hover {text-decoration:underline;}
    input[type="text"] {width:90%;max-width:600px;padding:20px;font-size:1.5rem;border-radius:4px;border:none;background:#333;color:#fff;margin-bottom:20px;}
    button {background:#e50914;padding:15px 40px;font-size:1.5rem;border:none;border-radius:4px;cursor:pointer;}
</style>
'''

# Routes remain the same as previous fixed version, just with updated grid in common_style

@app.route('/single', methods=['GET', 'POST'])
def single():
    if request.method == 'POST':
        mood = request.form['mood'].lower()
        suggestions = []
        for title, data in contents.items():
            if mood in [m.lower() for m in data[:-1]]:
                suggestions.append((title, data[-1]))
        if not suggestions:
            suggestions = [("No match found.", None)]
        return render_template_string(common_style + '''
        <div class="container">
            <h1>Suggestions for {{ mood }}</h1>
            <div class="grid">
                {% for title, poster in suggestions %}
                <div class="card">
                    {% if poster %}
                    <img src="{{ poster }}" alt="{{ title }}" onerror="this.style.display='none'">
                    {% endif %}
                    <h3>{{ title }}</h3>
                </div>
                {% endfor %}
            </div>
            <a href="/" class="back">← Back to Home</a>
        </div>
        ''', mood=mood.capitalize(), suggestions=suggestions)

    return render_template_string(common_style + '''
    <div class="container">
        <h1>What's your mood?</h1>
        <div class="grid">
            {% for mood in possible_moods %}
            <div class="card">
                <form method="post" style="width:100%;height:100%;">
                    <input type="hidden" name="mood" value="{{ mood }}">
                    <button type="submit" style="width:100%;height:100%;background:transparent;border:none;cursor:pointer;">
                        <span class="mood-text">{{ mood.capitalize() }}</span>
                    </button>
                </form>
            </div>
            {% endfor %}
        </div>
        <a href="/" class="back">← Back to Home</a>
    </div>
    ''', possible_moods=possible_moods)

@app.route('/multi', methods=['GET', 'POST'])
def multi():
    # Same as before...
    if request.method == 'POST':
        moods_str = request.form['moods']
        input_moods = [m.strip().lower() for m in moods_str.split(',') if m.strip()]
        if not input_moods:
            return common_style + '<h2 style="text-align:center;color:#e50914;padding:80px;">Please enter moods! <a href="/multi" style="color:#fff;">Retry</a></h2>'
        scored = []
        for title, data in contents.items():
            cmoods = [m.lower() for m in data[:-1]]
            poster = data[-1]
            match_count = sum(1 for im in input_moods if im in cmoods)
            if match_count > 0:
                scored.append((title, match_count, poster))
        scored.sort(key=lambda x: (-x[1], x[0]))
        suggestions = [(t, p) for t, _, p in scored]
        if not suggestions:
            suggestions = [("No match.", None)]
        return render_template_string(common_style + '''
        <div class="container">
            <h1>Group Suggestions: {{ moods }}</h1>
            <div class="grid">
                {% for title, poster in suggestions %}
                <div class="card">
                    {% if poster %}
                    <img src="{{ poster }}" alt="{{ title }}" onerror="this.style.display='none'">
                    {% endif %}
                    <h3>{{ title }}</h3>
                </div>
                {% endfor %}
            </div>
            <a href="/" class="back">← Back to Home</a>
        </div>
        ''', moods=', '.join([m.capitalize() for m in input_moods]), suggestions=suggestions)
    
    return render_template_string(common_style + '''
    <div class="container" style="text-align:center;padding-top:60px;">
        <h1>Group Mood</h1>
        <p style="font-size:1.3rem;margin-bottom:30px;">Enter multiple moods (comma-separated)</p>
        <form method="post">
            <input type="text" name="moods" placeholder="e.g. happy, romantic, excited">
            <br><br>
            <button type="submit">Get Recommendations</button>
        </form>
        <a href="/" class="back">← Back to Home</a>
    </div>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)