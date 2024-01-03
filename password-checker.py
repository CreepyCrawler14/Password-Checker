from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['GET'])
def check_password():
    password = request.args.get('password')
    wordlist = request.args.get('wordlist')

    try:
        with open(wordlist, 'r', encoding='latin-1') as wordlist_file:
            for line in wordlist_file:
                if password == line.strip():
                    result = f"Password '{password}' found in '{wordlist}'."
                    break
            else:
                result = f"Password '{password}' not found in '{wordlist}'."

        return result

    except FileNotFoundError:
        return f"Error: Wordlist '{wordlist}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
