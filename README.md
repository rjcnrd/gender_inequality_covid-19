# Visualisation of the gendered impact of COVID-19 in the UK using Python Dash 

## Project Background
We launched this collaboration at the beginning of April 2020, when political leaders and the press were looking for (missing) evidence of domestic violence and other gendered issues created by the lockdown measures in several European countries. 

We got in touch with UN Women UK to support their efforts in producing a single touchpoint on those issues using data science tools.

Our work consisted in helping with the creation of an online survey which was distributed through the numerous PR channels of UN Women UK. We then worked together with a team of volunteers on the creation of the “Everyday Allyship” platform, specifically the pillar Data for which we built several graphs that communicate the learnings of the online survey to visitors of the Everyday Allyship platform as well as press and political actors. The results of our work will soon be deployed on everydayallyship.com.

## Results

We summarise the outcome of the survey in 4 main graphs. The graphs created in this application are embedded via iframes in the Wordpress-based page that constitutes the Everyday Allyship platform, where each graph is "solo" embedded using it's unique URL. 

We nevertheless maintained an overview page containing all of the visualisations within this application for easier testing in development and to enable Dash developers to get inspired by our graphs.

<img src="https://github.com/rjcnrd/gender_inequality_covid-19/blob/master/assets/screenshot_map.jpg" alt="map graph"
	title="Map graph" width="400" />
	
<img src="https://github.com/rjcnrd/gender_inequality_covid-19/blob/master/assets/screenshot_mental.jpg" alt="mental health graph"
	title="mental health graph" width="400" />
	
<img src="https://github.com/rjcnrd/gender_inequality_covid-19/blob/master/assets/screenshot_sankey.jpg" alt="sankey graph graph"
	title="sankey graph" width="400" />
	
<img src="https://github.com/rjcnrd/gender_inequality_covid-19/blob/master/assets/screenshot_pie.jpg" alt="pie chart"
	title="pie chart" width="400" />

## Setup of the Repository 

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

#### Deploy the app on Heroku

Make sure you have master up to date, then

```
git push heroku master
```
deployed app: https://gender-inequality-covid-19.herokuapp.com/

## Built With

* [Plotly/Dash](https://plotly.com/dash/) 
* [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
* [Typeform API](https://developer.typeform.com/)
* [Heroku](www.heroku.com)
* [Undraw for Images](http://undraw.co/)

## Authors

Amélie Meurer and Roberta Conrad

## License

This project is licensed under the MIT License.
