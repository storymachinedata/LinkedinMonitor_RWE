import pandas as pd
import streamlit as st
from datetime import datetime
import re


def get_actual_date(url: str):
    unix_timestamp = int(format(int(url.split(":")[-1]), "b")[:41], 2)
    time_stamp = datetime.fromtimestamp(unix_timestamp / 1000).strftime(
        "%Y-%m-%d %H:%M:%S %Z"
    )
    return time_stamp


mapper = {
    "liked": "Liked a Comment",
    "likes": "Liked",
    "Reacted": "Reacted this Post",
    "commented": "Commented",
    "replied": "Replied",
    "reposted": "Reposted",
}


def rename_reactions(reactions):
    if "liked" in reactions:
        return mapper["liked"]
    elif "likes" in reactions:
        return mapper["likes"]
    elif "commented" in reactions:
        return mapper["commented"]
    elif "replied" in reactions:
        return mapper["replied"]
    elif "celebrates" in reactions:
        return "Reacted"
    elif "supports" in reactions:
        return "Reacted"
    elif "insightful" in reactions:
        return "Reacted"
    elif "curious" in reactions:
        return "Reacted"
    elif "loves" in reactions:
        return "Reacted"
    elif "reposted" in reactions:
        return "Reposted"
    else:
        return reactions
