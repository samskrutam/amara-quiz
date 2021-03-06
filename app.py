from flask import Flask, render_template, request
import random

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    all_vargas = ['स्वर्गवर्गः','व्योमवर्गः','दिग्वर्गः','कालवर्गः','धीवर्गः','शब्दादिवर्गः','नाट्यवर्गः','पातालभोगिवर्गः','नरकवर्गः','वारिवर्गः','भूमिवर्गः','पुरवर्गः','शैलवर्गः','वनौषधिवर्गः','सिंहादिवर्गः','मनुष्यवर्गः','ब्रह्मवर्गः','क्षत्रियवर्गः','वैश्यवर्गः','शूद्रवर्गः','विशेष्यनिघ्नवर्गः','सङ्कीर्णवर्गः','विशेष्यनिघ्नवर्गः','सङ्कीर्णवर्गः','नानार्थवर्गः','अव्ययवर्गः']
    return render_template('index.html', all_vargas=all_vargas)

def getMainTokenPart(token_line):
    line_parts = token_line.split(",")
    return line_parts[0]

def getSynonymTokenPart(token_line):
    line_parts = token_line.split(",")
    return line_parts[4]

@app.route('/quiz')
def quiz():

    filter_name = request.args.get('varga')
    filename = 'amara/tokens/tokens_' + filter_name + '.utf8'
    lines = open(filename).read().splitlines()

    question_line = random.choice(lines)
    question_line_parts = question_line.split(",")

    question = question_line_parts[0]
    sloka_index = question_line_parts[1]
    linga = question_line_parts[2]
    varga = question_line_parts[3]
    sloka_index_parts = sloka_index.split(".")
    sloka_index_relevant_parts = sloka_index_parts[0:3]
    sloka_index_line = sloka_index_parts[3]
    sloka_number = ".".join(sloka_index_relevant_parts)
    answer = question_line_parts[4]
    synonym = question_line_parts[4]
    answer = answer.replace("_", " ")

    context_filename = 'amara/slokas/Sloka_' + sloka_number + '.utf8'
    context = open(context_filename).read().splitlines()

    context_index = int(sloka_index_line)-1
    context[context_index] = '<span class="highlight">' + context[context_index] + '</span>'
    context_html = "<br/>".join(context)

    isSynonym = lambda token_line: true;

    synonyms = list(filter(lambda token_line: getSynonymTokenPart(token_line) == synonym, lines))
    synonyms_main_part = map(getMainTokenPart, synonyms)
    synonyms_string = " ".join(synonyms_main_part)

    return render_template('quiz.html', question=question, varga=varga, answer=answer, sloka_index=sloka_index, sloka_number=sloka_number, context=context_html, filter=filter_name, synonyms=synonyms_string, linga=linga)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
