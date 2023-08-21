from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Demo" 

image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'

fig = px.line(x=["a","b","c","d","e"], y=[1,3,2,2,3], title="Sample figure")	

df = px.data.iris()
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

app.layout = html.Div(
    [html.Img(src=image_path),	                
    html.H1("Data Visualization"),
    html.H2("Dashboard showing multiple graphs"),
    html.Div([dcc.Graph(figure = fig),
    dcc.Graph(figure = fig2)], style={'display': 'flex', 'flex-direction': 'row'})]
)

if __name__ == '__main__':
    app.run_server(debug=True)
