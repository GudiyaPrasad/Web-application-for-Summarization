from flask import Flask, render_template, request

from text_summary1 import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form.get('rawtext', '')
        
        if not rawtext:
            return render_template('error.html', error_message='Please enter some text.')

        try:
            summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)
        except Exception as e:
            # Handle summarization errors gracefully
            return render_template('error.html', error_message=f'Error during summarization: {str(e)}')

        return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)

    # Handle the GET request (if needed)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

