import streamlit as st
from PIL import Image
import base64
from io import BytesIO
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
# Set up page configuration
st.set_page_config(layout='wide')


# Create a transparent background pie chart using Plotly
labels = ['Video Games', 'School', 'Housework', 'Gym and Swimming']
sizes = [35, 25, 10, 30]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=0.3)])

# Update layout to have a transparent background
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0)
)

# CSS for circular image
css_code = """
<style>
.circle-image {
    width: 400px;
    height: 400px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
}
.circle-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>
"""

# Include CSS
st.markdown(css_code, unsafe_allow_html=True)

# Load images
circ_image = Image.open("C:\\Users\\Nitro-5\\Desktop\\Biography\\gym.jpg")
image = Image.open("c:\\Users\\Nitro-5\\Desktop\\Biography\\rob.png")
work_image1 = Image.open ("c:\\Users\\Nitro-5\\Desktop\\Biography\\work-1.png")
work_image2 = Image.open ("C:\\Users\\Nitro-5\\Desktop\\Biography\\work-2.png")
work_image3 = Image.open ("C:\\Users\\Nitro-5\\Desktop\\Biography\\landinggggg.png")

# Convert image to base64
def image_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode()

# Get base64 string of the circular image
circ_image_base64 = image_to_base64(circ_image)

# Create container with title
with st.container():
    col6, col7, col8 = st.columns([3, 5, 1])
    with col7:
        st.title("WELCOME TO MY DOMAIN ")

# Navigation menu
selected = option_menu(
    menu_title=None,
    options=['About me', 'Projects', 'Hidden Secrets'],
    icons=['person', 'code-slash', 'bi-incognito'],
    orientation='horizontal'
)

# Display content based on the selected menu item
if selected == 'About me':
    with st.container():
        st.write("# About Me")
        col1, col2, col3 = st.columns([1, 1, 4])

        # Text content
        with col3:
            st.markdown("""
                # Hello! I’m Rob Borinaga
                Currently residing on Carmel Drive in Talamban, Cebu City. My educational journey began at Talamban Elementary School and continued at Cebu City National Science High School, where I built a strong academic foundation. I’m now in my 4th year at Cebu Institute of Technology, diligently working towards my goals.
                
                ## Swimming Journey
                Swimming has always been a significant part of my life.
                I once aspired to become an Olympian, dedicating countless hours to training and pushing my limits. Although that dream has evolved, the dedication and discipline I gained from those experiences remain with me. Today, I enjoy swimming for both fun and fitness, and I’ve also developed a passion for working out at the gym.
            """)

        # Image content
        with col1:
            st.image(image, width=400)

        # Circular image
        with st.container():
            col4, col5, col6 = st.columns([2, 1,2])
            with col4:
                st.markdown("""
                    ## More About My Journey
                    I’m driven by the desire to excel in everything I do, whether it’s in the classroom or 
                            in my personal pursuits. My focus has shifted from athletic ambitions to academic and professional ones. 
                            I approach every challenge with a commitment to excellence, channeling the same energy and determination that once fueled my athletic dreams.
                             I’m dedicated to making the most of the opportunities before me, constantly seeking to grow and improve. 
                            This drive extends beyond my studies to my personal and professional life, as I strive to achieve my goals and make a meaningful impact in all that I undertake.
                """)

            with col6:
                st.markdown(f"""
                    <div class="circle-image">
                        <img src="data:image/jpeg;base64,{circ_image_base64}" alt="Circular Image">
                    </div>
                """, unsafe_allow_html=True)

if selected == 'Projects':
    with st.container():
        col9, col11, col12 = st.columns([1,1,1])

        with col9:
            st.image(work_image1, width= 250)
            st.write (" A mobile app that effortlessly connects users with their future pets through simplified browsing and adoption processes.")
        with col11:
            st.image(work_image2, width= 250)
            st.write (" An E-commerce mobile app offering a seamless shopping experience with user-friendly navigation, secure transactions, and personalized recommendations for a tailored shopping journey.")
        with col12:
            st.image(work_image3, width= 340)
            st.write ("")
            st.write (" A web-based Pet Adoption platform streamlining the process of connecting prospective pet owners with shelters through intuitive browsing and adoption application features.")
if selected == 'Hidden Secrets':
    st.write("## On a more personal note, I have a hidden side to me that I like to keep private: I spend a lot of time playing Dota and other computer games. It’s my way of unwinding and enjoying some downtime, and I prefer to keep this aspect of my life just for myself, Below is a pie graph representing how I allocate my time.")
    with st.container():
        col13, col14, col15 = st.columns([1,2,1])
        with col14:
            st.plotly_chart(fig, use_container_width=True)