from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Courtland's n00b app
Prepare to be blown away by my majestic data app:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in dingus", 1, 500, 500)
    num_turns = st.slider("Number of turns in dingus", 1, 10, 2)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=700, width=700)
        .mark_circle(color='#ff0000', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
