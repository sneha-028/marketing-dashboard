
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(page_title="Marketing Performance Dashboard", layout="wide")

# st.title("Marketing Performance Dashboard")

# df = pd.read_csv('marketing_data_with_metrics.csv')
# df['Date'] = pd.to_datetime(df['Date'])

# st.sidebar.header("Filters")
# selected_campaign = st.sidebar.multiselect("Select Campaign", df['Campaign_Name'].unique(), default=df['Campaign_Name'].unique())
# selected_channel = st.sidebar.multiselect("Select Channel", df['Channel'].unique(), default=df['Channel'].unique())
# date_range = st.sidebar.date_input("Date Range", [df['Date'].min(), df['Date'].max()])

# filtered_df = df[
#     (df['Campaign_Name'].isin(selected_campaign)) &
#     (df['Channel'].isin(selected_channel)) &
#     (df['Date'] >= pd.to_datetime(date_range[0])) &
#     (df['Date'] <= pd.to_datetime(date_range[1]))
# ]

# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Total Impressions", f"{filtered_df['Impressions'].sum():,}")
# col2.metric("Total Clicks", f"{filtered_df['Clicks'].sum():,}")
# col3.metric("Total Conversions", f"{filtered_df['Conversions'].sum():,}")
# col4.metric("Total Cost", f"${filtered_df['Cost'].sum():,.2f}")

# col5, col6, col7 = st.columns(3)
# col5.metric("Avg CTR", f"{filtered_df['CTR'].mean():.2f}%")
# col6.metric("Avg Conversion Rate", f"{filtered_df['Conversion_Rate'].mean():.2f}%")
# col7.metric("Avg ROI", f"{filtered_df['ROI'].mean():.2f}%")

# st.subheader("Channel-wise Performance")
# channel_performance = filtered_df.groupby('Channel').agg({
#     'Conversions': 'sum',
#     'Clicks': 'sum',
#     'Cost': 'sum'
# }).reset_index()
# fig1 = px.bar(channel_performance, x='Channel', y='Conversions', title='Conversions by Channel', color='Channel')
# st.plotly_chart(fig1, use_container_width=True)

# st.subheader("Campaign Performance")
# campaign_performance = filtered_df.groupby('Campaign_Name').agg({
#     'Conversions': 'sum',
#     'ROI': 'mean',
#     'CTR': 'mean'
# }).reset_index().sort_values('Conversions', ascending=False)
# st.dataframe(campaign_performance)

# st.subheader("Trends Over Time")
# daily_trends = filtered_df.groupby('Date').agg({
#     'Conversions': 'sum',
#     'Clicks': 'sum'
# }).reset_index()
# fig2 = px.line(daily_trends, x='Date', y='Conversions', title='Conversions Trend Over Time')
# st.plotly_chart(fig2, use_container_width=True)

# st.subheader("Business Insights")
# best_campaign = filtered_df.loc[filtered_df['ROI'].idxmax(), 'Campaign_Name']
# best_channel = filtered_df.groupby('Channel')['ROI'].mean().idxmax()
# st.write(f"Best performing campaign by ROI: **{best_campaign}**")
# st.write(f"Best converting channel: **{best_channel}**")
# st.write(f"Average ROI across all campaigns: **{filtered_df['ROI'].mean():.2f}%**")
# st.write(f"Total conversions achieved: **{filtered_df['Conversions'].sum():,}**")
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(page_title="Marketing Performance Dashboard", layout="wide")

# st.title("Marketing Performance Dashboard")

# df = pd.read_csv('marketing_data_with_metrics.csv')
# df['Date'] = pd.to_datetime(df['Date'])

# st.sidebar.header("Filters")
# selected_campaign = st.sidebar.multiselect("Select Campaign", df['Campaign_Name'].unique(), default=df['Campaign_Name'].unique())
# selected_channel = st.sidebar.multiselect("Select Channel", df['Channel'].unique(), default=df['Channel'].unique())
# date_range = st.sidebar.date_input("Date Range", [df['Date'].min(), df['Date'].max()])

# filtered_df = df[
#     (df['Campaign_Name'].isin(selected_campaign)) &
#     (df['Channel'].isin(selected_channel)) &
#     (df['Date'] >= pd.to_datetime(date_range[0])) &
#     (df['Date'] <= pd.to_datetime(date_range[1]))
# ]

# st.subheader("Key Performance Indicators")

# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Total Impressions", f"{filtered_df['Impressions'].sum():,}")
# col2.metric("Total Clicks", f"{filtered_df['Clicks'].sum():,}")
# col3.metric("Total Conversions", f"{filtered_df['Conversions'].sum():,}")
# col4.metric("Total Cost", f"${filtered_df['Cost'].sum():,.2f}")

# filtered_df['Revenue'] = filtered_df['Conversions'] * 10
# filtered_df['Profit'] = filtered_df['Revenue'] - filtered_df['Cost']

# col5, col6, col7, col8 = st.columns(4)
# col5.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,.2f}")
# col6.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
# col7.metric("Avg CTR", f"{filtered_df['CTR'].mean():.2f}%")
# col8.metric("Avg ROI", f"{filtered_df['ROI'].mean():.2f}%")

# st.subheader("Best and Worst Performing Campaigns")

# campaign_summary = filtered_df.groupby('Campaign_Name').agg({
#     'ROI': 'mean',
#     'Conversions': 'sum',
#     'Profit': 'sum'
# }).reset_index()

# best_roi = campaign_summary.loc[campaign_summary['ROI'].idxmax()]
# worst_roi = campaign_summary.loc[campaign_summary['ROI'].idxmin()]
# best_conversion = campaign_summary.loc[campaign_summary['Conversions'].idxmax()]

# col_a, col_b, col_c = st.columns(3)
# col_a.metric("🏆 Best ROI Campaign", best_roi['Campaign_Name'], f"{best_roi['ROI']:.2f}% ROI")
# col_b.metric("📉 Worst ROI Campaign", worst_roi['Campaign_Name'], f"{worst_roi['ROI']:.2f}% ROI")
# col_c.metric("🔥 Most Conversions", best_conversion['Campaign_Name'], f"{best_conversion['Conversions']:,} conversions")

# st.subheader("Channel Performance")

# channel_data = filtered_df.groupby('Channel').agg({
#     'Conversions': 'sum',
#     'Cost': 'sum',
#     'ROI': 'mean'
# }).reset_index()

# col_chart1, col_chart2 = st.columns(2)

# with col_chart1:
#     fig_pie = px.pie(channel_data, values='Conversions', names='Channel', title='Conversion Distribution by Channel')
#     st.plotly_chart(fig_pie, use_container_width=True)

# with col_chart2:
#     fig_cost = px.bar(channel_data, x='Channel', y='Cost', title='Cost per Channel', color='Channel')
#     st.plotly_chart(fig_cost, use_container_width=True)

# st.subheader("Campaign Performance Table")
# st.dataframe(campaign_summary.sort_values('ROI', ascending=False))

# st.subheader("Trends Over Time")
# daily_trends = filtered_df.groupby('Date').agg({
#     'Conversions': 'sum',
#     'Profit': 'sum'
# }).reset_index()
# fig_trend = px.line(daily_trends, x='Date', y='Conversions', title='Conversions Trend Over Time')
# st.plotly_chart(fig_trend, use_container_width=True)

# st.subheader("Business Insights Summary")
# st.write(f"✅ Best channel by ROI: **{channel_data.loc[channel_data['ROI'].idxmax(), 'Channel']}**")
# st.write(f"💰 Total profit generated: **${filtered_df['Profit'].sum():,.2f}**")
# st.write(f"📊 Average ROI across all campaigns: **{filtered_df['ROI'].mean():.2f}%**")


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Marketing Performance Dashboard", layout="wide", page_icon="📊")

st.markdown("""
<style>
    .stApp {
        background-color: #f5f7fa;
    }
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
    }
    .main-header p {
        color: rgba(255,255,255,0.9);
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        border-left: 4px solid #667eea;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #7f8c8d;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .insight-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    hr {
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>📊 Marketing Performance Dashboard</h1>
    <p>Real-time insights | Campaign Analytics | ROI Tracking</p>
</div>
""", unsafe_allow_html=True)

df = pd.read_csv('marketing_data_with_metrics.csv')
df['Date'] = pd.to_datetime(df['Date'])

with st.sidebar:
    st.markdown("## 🎛️ Filters")
    st.markdown("---")
    selected_campaign = st.multiselect("Select Campaign", df['Campaign_Name'].unique(), default=df['Campaign_Name'].unique())
    selected_channel = st.multiselect("Select Channel", df['Channel'].unique(), default=df['Channel'].unique())
    date_range = st.date_input("Date Range", [df['Date'].min(), df['Date'].max()])

filtered_df = df[
    (df['Campaign_Name'].isin(selected_campaign)) &
    (df['Channel'].isin(selected_channel)) &
    (df['Date'] >= pd.to_datetime(date_range[0])) &
    (df['Date'] <= pd.to_datetime(date_range[1]))
]

filtered_df['Revenue'] = filtered_df['Conversions'] * 10
filtered_df['Profit'] = filtered_df['Revenue'] - filtered_df['Cost']

st.markdown("## 📈 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{filtered_df['Impressions'].sum():,}</div>
        <div class="metric-label">Total Impressions</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{filtered_df['Clicks'].sum():,}</div>
        <div class="metric-label">Total Clicks</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{filtered_df['Conversions'].sum():,}</div>
        <div class="metric-label">Total Conversions</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${filtered_df['Cost'].sum():,.2f}</div>
        <div class="metric-label">Total Cost</div>
    </div>
    """, unsafe_allow_html=True)

col5, col6, col7, col8 = st.columns(4)
with col5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${filtered_df['Revenue'].sum():,.2f}</div>
        <div class="metric-label">Total Revenue</div>
    </div>
    """, unsafe_allow_html=True)
with col6:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${filtered_df['Profit'].sum():,.2f}</div>
        <div class="metric-label">Total Profit</div>
    </div>
    """, unsafe_allow_html=True)
with col7:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{filtered_df['CTR'].mean():.2f}%</div>
        <div class="metric-label">Avg CTR</div>
    </div>
    """, unsafe_allow_html=True)
with col8:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{filtered_df['ROI'].mean():.2f}%</div>
        <div class="metric-label">Avg ROI</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 🏆 Campaign Highlights")
campaign_summary = filtered_df.groupby('Campaign_Name').agg({
    'ROI': 'mean',
    'Conversions': 'sum',
    'Profit': 'sum'
}).reset_index()

best_roi = campaign_summary.loc[campaign_summary['ROI'].idxmax()]
worst_roi = campaign_summary.loc[campaign_summary['ROI'].idxmin()]
best_conversion = campaign_summary.loc[campaign_summary['Conversions'].idxmax()]

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown(f"""
    <div class="metric-card" style="border-left-color: #00ff88;">
        <div class="metric-value"> {best_roi['Campaign_Name']}</div>
        <div class="metric-label">Best ROI Campaign | {best_roi['ROI']:.2f}% ROI</div>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown(f"""
    <div class="metric-card" style="border-left-color: #ff6b6b;">
        <div class="metric-value">📉 {worst_roi['Campaign_Name']}</div>
        <div class="metric-label">Worst ROI Campaign | {worst_roi['ROI']:.2f}% ROI</div>
    </div>
    """, unsafe_allow_html=True)
with col_c:
    st.markdown(f"""
    <div class="metric-card" style="border-left-color: #ffa502;">
        <div class="metric-value"> {best_conversion['Campaign_Name']}</div>
        <div class="metric-label">Most Conversions | {best_conversion['Conversions']:,} total</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## Channel Performance")
channel_data = filtered_df.groupby('Channel').agg({
    'Conversions': 'sum',
    'Cost': 'sum',
    'ROI': 'mean'
}).reset_index()

col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    fig_pie = px.pie(channel_data, values='Conversions', names='Channel', title='Conversion Distribution by Channel', color_discrete_sequence=px.colors.qualitative.Set2)
    fig_pie.update_layout(bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pie, use_container_width=True)
with col_chart2:
    fig_cost = px.bar(channel_data, x='Channel', y='Cost', title='Cost per Channel', color='Channel', color_discrete_sequence=px.colors.qualitative.Set3)
    fig_cost.update_layout(bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_cost, use_container_width=True)

st.markdown("## Campaign Performance Table")
st.dataframe(campaign_summary.sort_values('ROI', ascending=False), use_container_width=True)

st.markdown("## 📈 Trends Over Time")
daily_trends = filtered_df.groupby('Date').agg({
    'Conversions': 'sum',
    'Profit': 'sum'
}).reset_index()
fig_trend = px.line(daily_trends, x='Date', y='Conversions', title='Conversions Trend Over Time', markers=True, color_discrete_sequence=['#667eea'])
fig_trend.update_layout(bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("""
<div class="insight-box">
    <h3>💡 Key Business Insights</h3>
    <ul>
        <li>✅ Best performing channel: <strong>Email</strong> with highest ROI</li>
        <li> Total profit generated: <strong>${:,.2f}</strong></li>
        <li> Average ROI across all campaigns: <strong>{:.2f}%</strong></li>
        <li> Most conversions achieved by: <strong>{}</strong> campaign</li>
    </ul>
</div>
""".format(filtered_df['Profit'].sum(), filtered_df['ROI'].mean(), best_conversion['Campaign_Name']), unsafe_allow_html=True)
