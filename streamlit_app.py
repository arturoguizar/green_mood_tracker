from green_mood_tracker.clustering import lda_wordcloud
from green_mood_tracker.predict import twint_prediction
from green_mood_tracker.utils import simple_time_tracker

import streamlit as st
import pytz
import pandas as pd
import joblib
import numpy as np
from datetime import datetime

from green_mood_tracker.datavisstreamlit import all_plotting
from green_mood_tracker.datavisstreamlit import altair_plot_like, altair_plot_tweet
from green_mood_tracker.datavisstreamlit import plot_map
import plotly.express as px
import plotly.graph_objects as go
import altair as alt


# from TaxiFareModel.data import get_data
# from TaxiFareModel.utils import geocoder_here


st.markdown("# Green Mood Tracker")
st.markdown("**Energy Sentiment Analysis**")


@st.cache
def read_data():
	pass

@st.cache
def select_data(topic='Solar Energy',country='USA',like_prediction = 'Per Tweet'):
	if country == 'USA':
		if topic == 'Climate Change':
			comment_dataframe_US_climate = pd.read_csv("green_mood_tracker/raw_data/US/[_climate_, _change_].csv")
			altair_sent_by_year_US_climate, altair_like_by_year_US_climate, layout_US_climate, data_slider_US_climate = plot_map(comment_dataframe_US_climate,country='US',like_prediction = like_prediction)
			return altair_sent_by_year_US_climate, altair_like_by_year_US_climate, layout_US_climate, data_slider_US_climate

		elif topic == 'Energy Prices':
			comment_dataframe_US_prices = pd.read_csv("green_mood_tracker/raw_data/US/[_energy_, _prices_].csv")
			altair_sent_by_year_US_prices, altair_like_by_year_US_prices, layout_US_prices, data_slider_US_prices = plot_map(comment_dataframe_US_prices,country='US',like_prediction = like_prediction)
			return altair_sent_by_year_US_prices, altair_like_by_year_US_prices, layout_US_prices, data_slider_US_prices

		elif topic == 'Green Energy':
			comment_dataframe_US_green = pd.read_csv("green_mood_tracker/raw_data/US/[_green_, _energy_].csv")
			altair_sent_by_year_US_green, altair_like_by_year_US_green, layout_US_green, data_slider_US_green = plot_map(comment_dataframe_US_green,country='US',like_prediction = like_prediction)
			return altair_sent_by_year_US_green, altair_like_by_year_US_green, layout_US_green, data_slider_US_green

		elif topic == 'Nuclear Energy':
			comment_dataframe_US_nuclear = pd.read_csv("green_mood_tracker/raw_data/US/[_nuclear_, _energy_].csv")
			altair_sent_by_year_US_nuclear, altair_like_by_year_US_nuclear, layout_US_nuclear, data_slider_US_nuclear = plot_map(comment_dataframe_US_nuclear,country='US',like_prediction = like_prediction)
			return altair_sent_by_year_US_nuclear, altair_like_by_year_US_nuclear, layout_US_nuclear, data_slider_US_nuclear

		elif topic == 'Fossil Fuels':
			comment_dataframe_US_fossil = pd.read_csv("green_mood_tracker/raw_data/US/[_fossil_, _fuels_].csv")
			altair_sent_by_year_US_fossil, altair_like_by_year_US_fossil, layout_US_fossil, data_slider_US_fossil = plot_map(comment_dataframe_US_fossil,country='US',like_prediction = like_prediction)
			return altair_sent_by_year_US_fossil, altair_like_by_year_US_fossil, layout_US_fossil, data_slider_US_fossil

		elif topic == 'Solar Energy':
			comment_dataframe_US_solar = pd.read_csv("green_mood_tracker/raw_data/US/[_solar_, _energy_].csv")
			altair_sent_by_year_US_solar, altair_like_by_year_US_solar, layout_US_solar, data_slider_US_solar = plot_map(comment_dataframe_US_solar,country='US',like_prediction = like_prediction)
			return altair_sent_by_year_US_solar, altair_like_by_year_US_solar, layout_US_solar, data_slider_US_solar

		elif topic == 'Wind Energy':
			comment_dataframe_US_wind = pd.read_csv("green_mood_tracker/raw_data/US/[_wind_, _energy_].csv")
			altair_sent_by_year_US_wind, altair_like_by_year_US_wind, layout_US_wind, data_slider_US_wind = plot_map(comment_dataframe_US_wind,country='US',like_prediction = like_prediction)
			return altair_sent_by_year_US_wind, altair_like_by_year_US_wind, layout_US_wind, data_slider_US_wind

	elif country == 'UK':
		if topic == 'Climate Change':
			comment_dataframe_UK_climate = pd.read_csv("green_mood_tracker/raw_data/UK/[_climate_, _change_].csv")
			altair_sent_by_year_UK_climate, altair_like_by_year_UK_climate,layout, data_slider = plot_map(comment_dataframe_UK_climate,country='UK',like_prediction = like_prediction)
			return altair_sent_by_year_UK_climate, altair_like_by_year_UK_climate, layout, data_slider

		elif topic == 'Energy Prices':
			comment_dataframe_UK_prices = pd.read_csv("green_mood_tracker/raw_data/UK/[_energy_, _prices_].csv")
			altair_sent_by_year_UK_prices, altair_like_by_year_UK_prices, layout, data_slider = plot_map(comment_dataframe_UK_prices,country='UK',like_prediction = like_prediction)
			return altair_sent_by_year_UK_prices, altair_like_by_year_UK_prices, layout, data_slider

		elif topic == 'Green Energy':
			comment_dataframe_UK_green = pd.read_csv("green_mood_tracker/raw_data/UK/[_green_, _energy_].csv")
			altair_sent_by_year_UK_green, altair_like_by_year_UK_green, layout, data_slider = plot_map(comment_dataframe_UK_green,country='UK',like_prediction = like_prediction)
			return altair_sent_by_year_UK_green, altair_like_by_year_UK_green, layout, data_slider

		elif topic == 'Nuclear Energy':
			comment_dataframe_UK_nuclear = pd.read_csv("green_mood_tracker/raw_data/UK/[_nuclear_, _energy_].csv")
			altair_sent_by_year_UK_nuclear, altair_like_by_year_UK_nuclear, layout, data_slider = plot_map(comment_dataframe_UK_nuclear,country='UK',like_prediction = like_prediction)
			return altair_sent_by_year_UK_nuclear, altair_like_by_year_UK_nuclear, layout, data_slider

		elif topic == 'Fossil Fuels':
			comment_dataframe_UK_fossil = pd.read_csv("green_mood_tracker/raw_data/UK/[_fossil_, _fuels_].csv")
			altair_sent_by_year_UK_fossil, altair_like_by_year_UK_fossil, layout, data_slider = plot_map(comment_dataframe_UK_fossil,country='UK',like_prediction = like_prediction)
			return altair_sent_by_year_UK_fossil, altair_like_by_year_UK_fossil, layout, data_slider

		elif topic == 'Solar Energy':
			comment_dataframe_UK_solar = pd.read_csv("green_mood_tracker/raw_data/UK/[_solar_, _energy_].csv")
			altair_sent_by_year_UK_solar, altair_like_by_year_UK_solar, layout, data_slider = plot_map(comment_dataframe_UK_solar,country='UK',like_prediction = like_prediction)
			return altair_sent_by_year_UK_solar, altair_like_by_year_UK_solar, layout, data_slider

		elif topic == 'Wind Energy':
			comment_dataframe_UK_wind = pd.read_csv("green_mood_tracker/raw_data/UK/[_wind_, _energy_].csv")
			altair_sent_by_year_UK_wind, altair_like_by_year_UK_wind, layout, data_slider = plot_map(comment_dataframe_UK_wind,country='UK',like_prediction = like_prediction)
			return altair_sent_by_year_UK_wind, altair_like_by_year_UK_wind, layout, data_slider



def format_input(pickup, dropoff, passengers=1):
	pickup_datetime = datetime.utcnow().replace(
		tzinfo=pytz.timezone('America/New_York'))
	formated_input = {
		"pickup_latitude": pickup["latitude"],
		"pickup_longitude": pickup["longitude"],
		"dropoff_latitude": dropoff["latitude"],
		"dropoff_longitude": dropoff["longitude"],
		"passenger_count": passengers,
		"pickup_datetime": str(pickup_datetime),
		"key": str(pickup_datetime)}
	return formated_input


def sl_predict(country_prediction, topic_prediction, d3):

	st.write(type(d3))
	st.write(d3)

	select_prediction_data(topic='Solar Energy', country='USA',
						   time='(datetime.date(2010, 12, 2), datetime.date(2030, 12, 2))')

	pred = twint_prediction('UK/[_climate_, _change_].csv')

	st.write(pred)


	return None


def main():
	analysis = st.sidebar.selectbox(
		"Select", ["Prediction", "Data Visualisation"])
	if analysis == 'Data Visualisation':
		st.header('Sentiment')
		year = st.slider('Year', min_value=2010, max_value=2020)
		country_prediction = st.selectbox('Select Country', ['UK', 'USA'], 1)
		topic_prediction = st.selectbox("Select Topic", ['Climate Change', 'Energy Prices', 'Fossil Fuels', 'Green Energy', 'Nuclear Energy', 'Solar Energy', 'Wind Energy'], 1)
		like_prediction = st.selectbox('Sentiment factor', ['Per Tweet', 'Likes Per Tweet'], 1)
		st.text(" \n")
		st.text(" \n")
		st.text(" \n")
		st.text(" \n")
		if like_prediction == 'Per Tweet':
			st.markdown(f'**Tweet Sentiment Polarity Rating Towards {topic_prediction} by State in the {country_prediction} in  {year}**')
		elif like_prediction == 'Likes Per Tweet':
			st.markdown(f'**Tweet Sentiment Polarity Rating Towards {topic_prediction} by State in the {country_prediction} in  {year}**')

			#data = 'green_mood_tracker/raw_data/twint_US.csv'
			#df = pd.read_csv(data)
			#df['year']= pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S', errors= 'coerce').dt.year
			#df = df[df['year'] == year]

		altair_sent_by_year, altair_like_by_year, layout, data_slider = select_data(topic=topic_prediction,country=country_prediction,like_prediction = like_prediction)
		fig = go.Figure(data=data_slider[abs(year-2020)], layout=layout)

		if country_prediction == 'UK':
			fig.update_geos(fitbounds="locations", visible=False)

		colors = ['darkgreen','darkseagreen', 'darkolivegreen']

		if like_prediction == 'Per Tweet':
			c= altair_plot_tweet(altair_sent_by_year,year)
			fig_pie = px.pie(altair_sent_by_year[abs(year-2020)].groupby('sentiment').mean().reset_index(), values='Percentage of Sentiment', names='sentiment',color_discrete_sequence=px.colors.sequential.YlGn)
			fig_pie.update_traces(hoverinfo='label+percent', textfont_size=12, textfont_color = '#000000',
				marker=dict(colors=colors, line=dict(color='#000000', width=1.5)))
		elif like_prediction == 'Likes Per Tweet':
			c = altair_plot_like(altair_like_by_year,year)
			fig_pie = px.pie(altair_like_by_year[abs(year-2020)].groupby('sentiment').mean().reset_index(), values='Percentage of Likes Per Sentiment', names='sentiment',color_discrete_sequence=px.colors.sequential.YlGn)
			fig_pie.update_traces(hoverinfo='label+percent', textfont_size=12, textfont_color = '#000000',marker=dict(colors=colors, line=dict(color='#000000', width=1.5)))

		st.plotly_chart(fig,width=4000,height=4000)

		st.text(" \n")
		st.markdown(f'**Evolution of Sentiment Share Towards {topic_prediction} in {year}**')
		st.altair_chart(c, use_container_width=True)

		st.text(" \n")
		st.markdown(f'**Total Share of Each Sentiment Towards {topic_prediction} in {year}**')
		st.plotly_chart(fig_pie)


		# st.write(df['tweet'])

		# lda_wordcloud(df,'tweet', [2], [300], 'http://clipart-library.com/images/8T6ooLLpc.jpg')
		# st.pyplot()

	if analysis == "Prediction":
		# pipeline = joblib.load('data/model.joblib')
		print("loaded model")
		st.header("Green Mood Tracker Model Predictions")
		# inputs from user
		country_prediction = st.selectbox("Select Country", ['UK', 'USA'], 1)
		topic_prediction = st.selectbox("Select Topic", [
										'Climate Change', 'Energy Prices', 'Fossil Fuels', 'Green Energy', 'Nuclear Energy', 'Solar Energy', 'Wind Energy'], 1)
		d3 = st.date_input("Select TimeFrame", [])

		# sl_predict(country_prediction, topic_prediction, d3)



		# dropoff_adress = st.text_input("dropoff adress", "434 6th Ave, New York, NY 10011")
		# Get coords from input adresses usung HERE geocoder
		# pickup_coords = geocoder_here(pickup_adress)
		# dropoff_coords = geocoder_here(dropoff_adress)
		# inputs from user
		# passenger_counts = st.selectbox("# passengers", [1, 2, 3, 4, 5, 6], 1)



		# data = pd.DataFrame([pickup_coords, dropoff_coords])
		# to_predict = [format_input(pickup=pickup_coords, dropoff=dropoff_coords, passengers=passenger_counts)]
		# X = pd.DataFrame(to_predict)
		# res = pipeline.predict(X[COLS])
		# st.write("💸 taxi fare", res[0])
		# st.map(data=data)




# print(colored(proc.sf_query, "blue"))
# proc.test_execute()
if __name__ == "__main__":
	main()
