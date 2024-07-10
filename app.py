from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/<words>')
def wierdify(words: str):
    values: dict[str, str] = {"Infinity": "+!![]/+[]", "NaN": "+{}", "[object Object]": "{}", "false": "![]", "true": "!![]", "undefined": "[][[]]"}
    chars: str = "".join(set("".join(values.keys())))+"0123456789"
    if len((wrong_letters := list(filter(lambda x: x not in chars, [*words])))) != 0:
        return f"error: letters {", ".join(wrong_letters)} are impossible to get."
    else:
        res: list[str] = []
        for i in words:
            if i.isdigit():
                res.append(f"(({"+!![]"*int(i)})+[])")
                continue
            word = values[(word2 := list(filter(lambda x: i in x, values))[0])]
            res.append(f"({word}+[])[{"+[]" if word2.index(i) == 0 else "+!![]" * word2.index(i)}]")
        return "+".join(res)


if __name__ == '__main__':
    app.run(debug=True)
