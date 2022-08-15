from flask import Flask, render_template, request
import os
import psycopg2
import psycopg2.extras

connection_string = os.environ.get('DATABASE_URL')
app = Flask(__name__)


@app.route("/")
def hello_world():
    restaurants = execute_select("select * from restaurants")
    rankings = execute_select("select * from rankings")
    for ranking in rankings:
        ranking_restaurants = []
        ids = ranking['restaurants_ids'].split(",")
        for i in range(len(ids)):
            for restaurant in restaurants:
                if restaurant['id'] == int(ids[i]):
                    if 'ratings' not in restaurant:
                        restaurant['ratings'] = []
                    restaurant_ranking = restaurant.copy()
                    rating = 1 - (i) / (len(ids) - 1)
                    restaurant_ranking['place'] = "{:.3f}".format(rating)
                    ranking_restaurants.append(restaurant_ranking)
                    restaurant['ratings'].append(rating)
                    break
        ranking['restaurants'] = ranking_restaurants
    for restaurant in restaurants:
        if 'ratings' in restaurant:
            restaurant['average'] = "{:.3f}".format(sum(restaurant['ratings']) / len(restaurant['ratings']))
            restaurant['votes'] = len(restaurant['ratings'])
        else:
            restaurant['average'] = "--"
            restaurant['votes'] = 0
    restaurants.sort(key= lambda x: x['average'], reverse=True)
    return render_template("restaurants.html", restaurants=restaurants, rankings=rankings)


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
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
    )
