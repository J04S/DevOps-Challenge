from flask import Flask
app = Flask(__name__)

@app.route('/getWeatherForecast')
def getWeatherForecast():
    return "Today is gonna be a great sunny python day!"