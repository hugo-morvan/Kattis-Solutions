import os
from dotenv import load_dotenv
from autokattis import OpenKattis

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWORD")
kt = OpenKattis(user, password)
kt.plot_problems(filepath='./plot.png',show_partial=False)       # save to a filepath
