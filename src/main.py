import streamlit as st
from password import MemorablePasswordGenerator,Pingeneratore, RandomGenerator


c1, c2 =st.columns([0.30, 0.70])

with c1:
    st.image('/home/reyhanehraisi/project/p013/src/pic/pngtree-password-security-lock-vector-png-image_12350211.png', width= 150) 

with c2:
    st.title('Password Generator')


col1, col2 = st.columns(spec=[0.3 , 0.7])

with col1:
    option = st.radio(
   '**Select a Password Generator**',
    ('Pin Code','Random Password','Memorable Password')
)

with col2:
    if option == 'Pin Code':
        st.write('**Pin Code**')
        length = st.slider('Select the Length of the Pin Code', 4, 28)
        generator = Pingeneratore(length)
        password = generator.generate()
        st.write(f'Your Password is: `{password}`')
    elif option == 'Random Password':
        st.write('**Random Password**')
        length = st.slider('Select the Length of the Random Password', 4, 28)
        include_symble = st.toggle('Include Symble')
        include_number = st.toggle('Include Number')
        generator_random = RandomGenerator(length, include_numbers= include_number, include_symbols=include_symble)
        password_1 = generator_random.generate()
        st.write(fr'Your Password is: `{password_1}` ')
    elif option == 'Memorable Password':
        st.write('**Memorable Password**')
        num_of_words = st.slider('Select the  number of word for Memorable Password', 1, 8)
        separator = st.text_input('**separator**', value= '_')
        capitalization = st.toggle('capitalization')
        generator_memorable = MemorablePasswordGenerator(num_of_words = num_of_words, separator= separator, capitalization = capitalization)
        password_2 = generator_memorable.generate()
        st.write(f'Your Password is: `{password_2}`')

