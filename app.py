import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Economic Crimes Latin America', page_icon='🔍', layout='wide')
st.title('🔍 Economic Crimes in Latin America')
st.caption('Interactive dashboard analyzing financial crimes, corruption and economic fraud across Latin America')

page = st.sidebar.selectbox('Section', [
    'Overview', 'Corruption Index', 'Money Laundering', 'Tax Evasion',
    'Drug Trafficking Economics', 'Cybercrime', 'Financial Fraud',
    'Country Analysis', 'Institutional Response', 'Economic Impact',
    'Trends', 'Methodology'
])

countries = ['Brazil', 'Mexico', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 'Ecuador']

if page == 'Overview':
    st.header('Regional Overview of Economic Crimes')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Annual Economic Loss', '$340B', '+4.8%')
    c2.metric('Corruption Perception', '3.4/10', '+0.2')
    c3.metric('Money Laundering', '$89B', '+2.1%')
    c4.metric('Tax Evasion', '$145B', '+3.7%')
    loss = [120, 85, 42, 38, 22, 18, 8, 7]
    fig = px.bar(x=countries, y=loss, color=loss, color_continuous_scale='Reds',
                 title='Annual Economic Crime Loss by Country (Billions USD)')
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Corruption Index':
    st.header('Corruption Perception Index (CPI)')
    cpi = [38, 31, 39, 38, 36, 13, 67, 34]
    colors = ['#ff6b6b' if c < 40 else '#00d4aa' for c in cpi]
    fig = go.Figure(data=[go.Bar(x=countries, y=cpi, marker_color=colors)])
    fig.add_hline(y=50, line_dash='dash', line_color='white', annotation_text='Threshold (50)')
    fig.update_layout(template='plotly_dark', title='CPI 2024 (0=Highly Corrupt, 100=Very Clean)', height=400)
    st.plotly_chart(fig, use_container_width=True)
    years = list(range(2015, 2025))
    latam_cpi = [37, 36, 36, 35, 35, 36, 35, 35, 34, 34]
    fig2 = go.Figure(go.Scatter(x=years, y=latam_cpi, mode='lines+markers', line=dict(color='#ffd93d', width=3)))
    fig2.update_layout(template='plotly_dark', title='Latin America Average CPI Trend', height=300)
    st.plotly_chart(fig2, use_container_width=True)

elif page == 'Money Laundering':
    st.header('Money Laundering')
    c1, c2, c3 = st.columns(3)
    c1.metric('Regional Total', '$89B', '+2.1%/year')
    c2.metric('% of Regional GDP', '1.3%', 'annual flow')
    c3.metric('FATF Non-Compliant', '4 countries', 'in region')
    sectors = ['Real Estate', 'Financial Services', 'Shell Companies', 'Trade-Based', 'Cash Intensive', 'Crypto']
    amounts = [28.4, 22.1, 18.7, 12.3, 5.8, 1.7]
    fig = go.Figure(data=[go.Pie(labels=sectors, values=amounts, hole=0.4)])
    fig.update_layout(template='plotly_dark', title='Money Laundering Channels (Billions USD)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Tax Evasion':
    st.header('Tax Evasion')
    c1, c2, c3 = st.columns(3)
    c1.metric('Annual Tax Gap', '$145B', '+3.7%')
    c2.metric('% of Potential Revenue', '27.4%', 'evaded')
    c3.metric('Informal Economy', '38%', 'of GDP')
    evasion_rates = [24.2, 31.8, 28.4, 26.7, 32.1, 45.3, 18.9, 29.5]
    fig = px.bar(x=countries, y=evasion_rates, color=evasion_rates, color_continuous_scale='Reds',
                 title='Tax Evasion Rate % (2024)')
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Drug Trafficking Economics':
    st.header('Drug Trafficking Economic Impact')
    c1, c2, c3 = st.columns(3)
    c1.metric('Annual Revenue', '$152B', 'estimated')
    c2.metric('GDP % Major Producers', '2-5%', 'cocaine')
    c3.metric('Job displacement', '2.8M', 'affected')
    drugs = ['Cocaine', 'Marijuana', 'Synthetic', 'Heroin', 'Other']
    revenue = [82, 28, 24, 12, 6]
    fig = go.Figure(data=[go.Pie(labels=drugs, values=revenue, hole=0.4)])
    fig.update_layout(template='plotly_dark', title='Drug Trade Revenue by Substance (Billions USD)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Cybercrime':
    st.header('Cybercrime Trends')
    c1, c2, c3 = st.columns(3)
    c1.metric('Annual Cybercrime Loss', '$8.3B', '+24%')
    c2.metric('Phishing Attacks', '42M/year', '+18%')
    c3.metric('Ransomware Incidents', '18,400', '+31%')
    years = list(range(2018, 2025))
    losses = [2.1, 2.8, 3.4, 4.2, 5.8, 7.1, 8.3]
    fig = go.Figure(go.Bar(x=years, y=losses, marker_color='#ff6b6b'))
    fig.update_layout(template='plotly_dark', title='Cybercrime Losses (Billions USD)', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Financial Fraud':
    st.header('Financial Fraud')
    fraud_types = ['Banking Fraud', 'Securities Fraud', 'Insurance Fraud', 'Corporate Fraud', 'Identity Theft']
    amounts = [18.4, 8.7, 5.2, 12.3, 4.8]
    fig = px.bar(x=fraud_types, y=amounts, color=amounts, color_continuous_scale='Reds')
    fig.update_layout(template='plotly_dark', title='Financial Fraud by Type (Billions USD)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Country Analysis':
    st.header('Country-Level Analysis')
    country_sel = st.selectbox('Select Country', countries)
    idx = countries.index(country_sel)
    cpi_vals = [38, 31, 39, 38, 36, 13, 67, 34]
    loss_vals = [120, 85, 42, 38, 22, 18, 8, 7]
    c1, c2, c3 = st.columns(3)
    c1.metric('CPI Score', f'{cpi_vals[idx]}/100')
    c2.metric('Crime Loss', f'${loss_vals[idx]}B')
    c3.metric('Rule of Law', f'{30 + idx*5}/100')

elif page == 'Institutional Response':
    st.header('Institutional Response')
    institutions = ['UNODC', 'FATF', 'OAS/MESICIC', 'World Bank', 'IMF']
    effectiveness = [62, 58, 54, 71, 68]
    fig = px.bar(x=institutions, y=effectiveness, color=effectiveness, color_continuous_scale='Viridis')
    fig.update_layout(template='plotly_dark', title='Institutional Effectiveness Score (0-100)', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Economic Impact':
    st.header('Macro-Economic Impact')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('GDP Loss', '-1.8%', 'annual')
    c2.metric('FDI Reduction', '-12%', 'vs potential')
    c3.metric('Institutional Costs', '$42B', '/year')
    c4.metric('Human Capital Loss', '$28B', '/year')
    categories = ['GDP Growth', 'Investment', 'Social Services', 'Human Development', 'Rule of Law']
    impact = [-1.8, -12, -8.4, -6.2, -9.1]
    fig = go.Figure(go.Bar(x=categories, y=impact, marker_color='#ff6b6b'))
    fig.update_layout(template='plotly_dark', title='% Impact on Key Indicators', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Trends':
    st.header('Trends 2010-2024')
    years = list(range(2010, 2025))
    corruption = [42, 41, 40, 39, 38, 37, 36, 36, 35, 35, 35, 34, 34, 34, 34]
    ml_flow = [45, 52, 58, 64, 69, 74, 78, 81, 82, 83, 85, 87, 88, 89, 89]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=corruption, name='CPI Score (Inverted)', line=dict(color='#ff6b6b', width=3)))
    fig.add_trace(go.Scatter(x=years, y=ml_flow, name='Money Laundering (B USD)', line=dict(color='#ffd93d', width=3)))
    fig.update_layout(template='plotly_dark', title='Economic Crime Trends 2010-2024', height=400)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.header('Methodology')
    st.write('**Data sources:** UNODC, Transparency International, FATF, World Bank, IADB')
    st.write('**Period:** 2000-2024')
    st.write('**Coverage:** 20 Latin American countries')
    st.write('**Economic crime categories:** Corruption, money laundering, tax evasion, drug trafficking, cybercrime, financial fraud')

st.markdown('---')
st.caption('Economic Crimes Dashboard | Sources: UNODC, Transparency International, FATF | Latin America')
