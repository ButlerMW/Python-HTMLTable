from flask import Flask, render_template
app = Flask(__name__)

@app.route('/table')
def table_index():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("table_index.html", users=users)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_page.html')

if __name__=="__main__":
    app.run(debug=True)