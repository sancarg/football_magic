from cProfile import label
from typing import List
import streamlit as st
import os
from pathlib import Path
import pandas as pd
from inflection import dasherize, titleize
from datetime import datetime, timedelta

import base64

import sys
cwd = os.getcwd()
sys.path.insert(0, cwd)
