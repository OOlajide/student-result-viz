import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

senior_subjects = ['English Language', 'Mathematics', 'Physics', 'Chemistry', \
            'Biology', 'Geography', 'Government', 'Commerce', 'Civic Education', \
                   'Economics', 'Literature In English', 'Technical Drawing', \
                   'Accounting', 'Data Processing', 'Further Mathematics']
junior_subjects = ['English Language', 'Mathematics', 'Civic Education', \
                   'Computer Studies', 'Basic Science', 'Basic Science', \
                   'Business Studies', 'Home Economics', 'Basic Technology', \
                   'Physical Health Education', 'Agricultural Science', \
                   'Technical Drawing', 'Creative and Cultural Arts']

st.title('Student\'s Result Visualization Dashboard')
st.write('Use the menu on the left to enter and vizualize your result (click on > if closed).')
expander = st.sidebar.beta_expander('About')
expander.write("This web app allows secondary school students to visualize their result, providing an easy to understand chart.")
st.sidebar.subheader('Select Section')
section = st.sidebar.radio('', ['Junior Secondary', 'Senior Secondary'])
if section == 'Junior Secondary':
    with st.sidebar.form(key ='form'):
        name = st.text_input('Student name')
        st.subheader('Select 6 or more subjects')
        subjects = st.multiselect('Select Subjects', junior_subjects)
        st.subheader('Enter score for each selected subject')
        scores = st.text_input('In the order they were selceted, enter score for each subject separated by \",\" e.g 10,20,50')
        submit = st.form_submit_button('Submit and Visualize')
elif section == 'Senior Secondary':
    with st.sidebar.form(key ='form'):
        name = st.text_input('Student name')
        st.subheader('Select 6 or more subjects')
        subjects = st.multiselect('Select Subjects', senior_subjects)
        st.subheader('Enter score for each selected subject')
        scores = st.text_input('In the order they were selceted, enter score for each subject separated by \",\" e.g 10,20,50')
        submit = st.form_submit_button('Submit and Visualize')

if submit:
    if len(name) >=1 and type(name)==str and len(subjects) >= 6:
        st.subheader(f'{name}\'s result')
        df = pd.DataFrame({
            'Score': [int(x) for x in scores.split(',')]
            }, index=list(subjects))
        plt.rc('font', size=20)          # controls default text sizes
        plt.rc('axes', titlesize=15)     # fontsize of the axes title
        plt.rc('axes', labelsize=20)     # fontsize of the x and y labels
        plt.rc('xtick', labelsize=13)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=13)    # fontsize of the tick labels
        plt.rc('legend', fontsize=10)    # legend fontsize
        plt.rc('figure', titlesize=12)   # fontsize of the figure title
        plt.rcParams['font.family'] = 'Comic Sans MS'
        plt.style.use('seaborn-dark-palette')
        table = st.table(df)
        plot = df.sort_values(by=['Score']).plot.barh(grid=False, ylabel='Subjects', xticks=[0,20,40,60,80,100])
        left, right = plt.xlim()
        plt.xlim(left, right + 100)
        plt.legend(loc='lower right')
        plt.title('Horizontal Bar Chart of Result')
        for i, v in enumerate(df['Score'].sort_values()):
            plt.text(v + 1, i, str(v), color='black', fontsize=10, ha='left', va='center')
        fig = plot.get_figure()
        fig.set_facecolor('grey')
        st.pyplot(fig)
    else:
        st.error('Kindly select 5 or more subjects and make sure the \'Student name\' field is not empty, then try again.')
