import pandas as pd
import streamlit as st
import altair as alt #for graph
from PIL import Image #for showing an image


image=Image.open('dna-log.jpg') #load the image we want

st.image(image,use_column_width=True) #display on streamlit, expand it to column width
st.write("""
#DNA Neucleotide Count Web app
This app counts neucleotide compostion of query dna 
***
""")

st.header('Enter DNA Sequence')
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence=st.text_area('Sequence Input',sequence_input,height=250) #define the text box
sequence=sequence.splitlines()
sequence=sequence[1:]
sequence=''.join(sequence) #get one line

st.write("""
***
""")


#prints the dna sequence
st.header('Input dna query')
sequence

st.header('Output dna neuclotide count')

##print dictionary
st.subheader('1.Print Dictionary')
def DNA_n_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

    X=DNA_n_count(sequence)

    X_label=list(X)
    X_values=list(X.values())


##print text
    st.subheader('Print text')


    st.write('There are  ' + str(X['A']) + ' adenine (A)')
    st.write('There are  ' + str(X['T']) + ' thymine (T)')
    st.write('There are  ' + str(X['G']) + ' guanine (G)')
    st.write('There are  ' + str(X['C']) + ' cytosine (C)')


### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)