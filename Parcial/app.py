from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html',page='main')

@app.route('/apexcharts')
def chart():
    return render_template('charts-apexcharts.html')

@app.route('/chartjs')
def chartjs():
    return render_template('charts-chartjs.html')

@app.route('/echarts')
def echarts():
    return render_template('charts-echarts.html')

@app.route('/accordion')
def accordion():
    return render_template('components-accordion.html')

@app.route('/alerts')
def alerts():
    return render_template('components-alerts.html')

@app.route('/badges')
def badges():
    return render_template('components-badges.html')

@app.route('/breadcrumbs')
def breadcrumbs():
    return render_template('components-breadcrumbs.html')

@app.route('/buttons')
def buttons():
    return render_template('components-buttons.html')

@app.route('/cards')
def cards():
    return render_template('components-cards.html')

@app.route('/carousel')
def carousel():
    return render_template('components-carousel.html')

@app.route('/list-group')
def list_group():
    return render_template('components-list-group.html')

@app.route('/modal')
def modal():
    return render_template('components-modal.html')

@app.route('/pagination')
def pagination():
    return render_template('components-pagination.html')

@app.route('/progress')
def progress():
    return render_template('components-progress.html')

@app.route('/spinners')
def spinners():
    return render_template('components-spinners.html')

@app.route('/tabs')
def tabs():
    return render_template('components-tabs.html')

@app.route('/tooltips')
def tooltips():
    return render_template('components-tooltips.html')

@app.route('/editors')
def editors():
    return render_template('forms-editors.html')

@app.route('/elements')
def elements():
    return render_template('forms-elements.html')

@app.route('/layouts')
def layouts():
    return render_template('forms-layouts.html')

@app.route('/validation')
def validation():
    return render_template('forms-validation.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('icons-bootstrap.html')

@app.route('/boxicons')
def boxicons():
    return render_template('icons-boxicons.html')

@app.route('/remix')
def remix():
    return render_template('icons-remix.html')

@app.route('/blank')
def blank():
    return render_template('pages-blank.html')

@app.route('/contact')
def contact():
    return render_template('pages-contact.html')

@app.route('/error-404')
def error404():
    return render_template('pages-error-404.html')

@app.route('/faq')
def faq():
    return render_template('pages-faq.html')

@app.route('/login')
def login():
    return render_template('pages-login.html')

@app.route('/register')
def register():
    return render_template('pages-register.html')

@app.route('/data')
def data():
    return render_template('tables-data.html')

@app.route('/general')
def general():
    return render_template('tables-general.html')

@app.route('/profile')
def profile():
    return render_template('user-profile.html')

if __name__ == '__main__':
    app.run(debug=True)
