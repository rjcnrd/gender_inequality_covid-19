# Analysis of the gendered impact of COVID-19 in the UK 

In several European countries, radical political measures such as nation-wide lockdowns and other restrictions impacting the economy have been implemented following the covid-19 outbreak in Spring 2020.

Many of these political decisions and consequences of the pandemic impact women different then men. This project aims at painting a picture of the current situation to raise public attention and action to the subject.

### Setup

After cloning the repo, create a virtual environment & start the app following the steps below.

#### Create environment
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

#### Launch the dash app
```
python3 app.py
```
Open http://127.0.0.1:8050/ in your browser to see the app.

#### Update the environment
```
pip3 freeze>requirements.txt
```

#### Deploy the app on Heroku :

Make sure you have master up to date, then :

```
git push heroku master
```
Link can be found : https://dash-app-gender-violence.herokuapp.com

## Built With

* [Plotly/Dash](https://plotly.com/dash/) 
## Authors

Amélie Meurer and Roberta Conrad

## License

This project is licensed under the MIT License.
