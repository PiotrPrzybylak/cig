from flask import Flask, render_template, request
import os
import psycopg2
import psycopg2.extras

connection_string = os.environ.get('DATABASE_URL')
app = Flask(__name__)


@app.route("/")
def hello_world():
    restaurants = execute_select("select name from restaurants")
    return render_template("restaurants.html", restaurants=restaurants)


def execute_select(statement, variables=None, fetchall=True):
    result_set = []
    with psycopg2.connect(connection_string) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Port is " + str(port))
    print("ccccccc")
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
    )
