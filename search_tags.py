import pandas as pd
import streamlit as st
from typing import List, Tuple
from streamlit_searchbox import st_searchbox

tech_tags = pd.read_csv('data/stack_exchange_tags_with_stackshare.csv')
tech_tags = tech_tags[tech_tags['is_valid'] ==
                      True].sort_values(by=['count'], ascending=False)
tech_tags['display_name'] = tech_tags['display_name'].astype(str)


def search_list(searchterm: str) -> List[Tuple[str, str]]:
    if searchterm is None:
        return []
    hits = tech_tags[tech_tags['display_name'].str.contains(
        searchterm.lower())].head(10)
    if hits.shape[0] > 0:
        return [(row['display_name'].title(), {'name': row['display_name'].title(), 'url': row['stackshare_url']}) for _, row in hits.iterrows()]
    else:
        return []


selected_value = st_searchbox(
    search_list, key="search list", placeholder="Search ...")
if selected_value:
    st.markdown(f"[Open {selected_value['name']}]({selected_value['url']})")
