import os, sys 
import pandas as pd 
import numpy as np
import streamlit as st
import streamlit_authenticator as stauth
import yaml 
from yaml.loader import SafeLoader
from dotenv import load_dotenv

sys.path.append(os.path.abspath('src'))

from src.utils import list_catalog_schema_tables, create_erd_diagram, process_llm_response_for_mermaid, mermaid


load_dotenv()


st.set_page_config(
    page_title="QuerySmart",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded",
)

# The App 
st.markdown("<h1 style='text-align: center; color: orange;'> QuerySmart &#128640; </h1>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center; color: white;'> Productivity Improvement tool for Product Managers, Business stakeholders and even intermediate-coders when it comes to working with data stored in a traditional SQL database. </h6>", unsafe_allow_html=True)


with open('authenticator.yml') as f:
    config = yaml.load(f, Loader=SafeLoader)


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, user_name = authenticator.login()


if authentication_status:
    authenticator.logout('Logout','main')
    st.write(f"Welcome *{name}*!")

    # Selecting the Catalog, Schema and Table in the Target Database
    st.sidebar.image('artifacts/Databricks_Logo_2.png')
    result_tables = list_catalog_schema_tables()
    df_databricks = pd.DataFrame(result_tables).iloc[:,:4]
    df_databricks.columns=["catalog","schema","table","table_type"]

    # getting catalog to schema mapping for dynamically selecting only relevant schema for a given catalog
    catalog_schema_mapping_df = df_databricks.groupby(["catalog"]).agg({'schema': lambda x: list(np.unique(x))}).reset_index()

    # getting schema to table mapping for dynamically selecting only relevant tables for a given catalog and schema
    schema_table_mapping_df = df_databricks.groupby(["schema"]).agg({'table': lambda x: list(np.unique(x))}).reset_index()

    # Selecting the catalog
    catalog = st.sidebar.selectbox("Select the catalog", options=df_databricks['catalog'].unique().tolist())

    # Selecting the schema 
    schema_candidate_list = catalog_schema_mapping_df[catalog_schema_mapping_df["catalog"]==catalog]["schema"].values[0]
    schema_candidate_list = [val for val in schema_candidate_list if val != "dev_tools"]
    schema = st.sidebar.selectbox("Select the schema", options=schema_candidate_list)

    # Selecting the Tables
    table_candidate_list = schema_table_mapping_df[schema_table_mapping_df["schema"]==schema]["table"].values[0]
    table_list = st.sidebar.multiselect("Select the table", options= ["All"]+table_candidate_list)


    if "All" in table_list:
        table_list = table_candidate_list


    if st.sidebar.checkbox(":orange[Proceed]"):        
        with st.expander(":red[View the ERD Diagram]"):
            response = create_erd_diagram(catalog,schema,table_list)
            if st.button("Regenerate"):
                # Creating the ERD Diagram
                create_erd_diagram.clear()
                response = create_erd_diagram(catalog,schema,table_list)
                mermaid_code = process_llm_response_for_mermaid(response)
                mermaid(mermaid_code)
            else:
                mermaid_code = process_llm_response_for_mermaid(response)
                mermaid(mermaid_code)

        
            


else:
    st.write(f"Please login to continue!")




# --> next step is to make sure we have all the context for the llm to work on 
# --> generate the query
# --> can have an extra add on query to the previous one (more in depth)  
# --> validate the query if it is wrong
# --> if it is wrong, rebuilt the query such that it works correctly
# --> if it is right, then move ahead to further deeper analysis  

# Instruction based (give set of instructions)
# Role based promiting (act as cutomer service)

# Langchain - chaining, memory for conversation, Tools(connect to internet) , Data parsing 


