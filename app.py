from flask import Flask, request

import requests

app = Flask(__name__)

@app.route('/search_quran', methods=['GET'])

def search_quran():

    text = request.args.get('text')

    r = requests.get(f"https://api-quran.cf/quransql/index.php?text={text}&type=search")

    decoded_text = r.text.encode('utf-8').decode('unicode_escape')

    return decoded_text

if __name__ == '__main__':

    app.run(debug=True)

