from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def visitors():

    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    # Increment the count
    visitors_count = visitors_count + 1

    # Overwrite the count
    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()

    # Render HTML with count variable
    return render_template("index2.html", count=visitors_count)

@app.route('/', methods=['POST'])
def covid_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    text = request.form['text']

    corona_data = 'https://covid-api-262.herokuapp.com/?country='+text
    print(corona_data)
    return render_template("index2.html", image=corona_data, count=visitors_count)

if __name__ == "__main__":
    app.run()
