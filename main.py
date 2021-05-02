from website import create_app

app = create_app()

if __name__ == '__main__':  # if only we run file from this director.
    # automatically re run web server, jo nereiktu kas kart manually serverio jungt
    app.run(debug=True)
