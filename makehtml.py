from jinja2 import Template

# HTMLテンプレート
html_template = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ video_title }}</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
            color: #333;
        }
        h1, h2 {
            text-align: center;
            color: #212529;
            margin: 20px 0;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        .video-container {
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
            max-width: 100%;
            background-color: #000;
            margin-bottom: 40px;
        }
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .setlist-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .setlist-table th, .setlist-table td {
            padding: 12px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }
        .setlist-table th {
            background-color: #343a40;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .setlist-table td {
            color: #555;
        }
        .setlist-table tr:hover {
            background-color: #f1f1f1;
        }
        .setlist-table td a {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }
        .setlist-table td a:hover {
            text-decoration: underline;
        }
        .ad-container {
            margin: 20px 0;
            text-align: center;
        }
        .ad-container iframe {
            width: 100%;
            height: 150px;
            border: none;
        }
        @media (max-width: 768px) {
            h1, h2 {
                font-size: 1.5em;
            }
            .setlist-table th, .setlist-table td {
                padding: 10px;
            }
            .ad-container iframe {
                height: 100px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>動画タイトル: {{ video_title }}</h1>

        <div class="video-container">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/{{ video_id }}" 
            title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>

        <div class="ad-container">
            <iframe src="https://example.com/your-ad" title="広告"></iframe>
        </div>

        <h2>音楽セットリスト</h2>
        
        <table class="setlist-table">
            <thead>
                <tr>
                    <th>タイムスタンプ</th>
                    <th>曲名</th>
                    <th>アーティスト</th>
                </tr>
            </thead>
            <tbody>
                {% for song in setlist %}
                <tr>
                    <td><a href="https://youtu.be/{{ video_id }}?t={{ song.timestamp }}" target="_blank">{{ song.timestamp_text }}</a></td>
                    <td>{{ song.title }}</td>
                    <td>{{ song.artist }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <div class="ad-container">
            <iframe src="https://example.com/your-ad" title="広告"></iframe>
        </div>
    </div>
</body>
</html>
"""

a=[[987, '20:47', '童話迷宮 / Douwa Meikyu', '田村ゆかり'], [1595, '26:35', '天体観測 / Tentai Kansoku', 'BUMP OF CHICKEN'], [2082, '34:42', '少女レイ / Shoujo Rei', 'みきとP'], [2402, '40:02', 'あいわな / I Wanna', '湊あくあ']]
# 動的に置き換えるデータ
video_data = {
    "video_title": "【歌枠】あたしったら三十路のくせして海賊コスプレ婚期もちょっとアレ【ホロライブ/宝鐘マリン】",
    "video_id": "7rRH0GOtdS8",
    "setlist": [
        {"timestamp": a[i][0], "timestamp_text": a[i][1], "title": a[i][2], "artist": a[i][3]}
        for i in range(4)
        
    ]
}

# テンプレートにデータを適用してHTMLを生成
template = Template(html_template)
output_html = template.render(video_data)

# 出力結果を表示するか、ファイルに保存
with open("output.html", "w", encoding="utf-8") as f:
    f.write(output_html)

print("HTMLが生成されました。")
