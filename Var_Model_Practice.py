#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 00:12:47 2020

@author: chandrakant
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.base.datetools import dates_from_str

mdata = sm.datasets.macrodata.load_pandas().data

dates = mdata[['year', 'quarter']].astype(int).astype(str)
quarterly = dates['year'] + 'Q' + dates['quarter']
quarterly = dates_from_str(quarterly)
