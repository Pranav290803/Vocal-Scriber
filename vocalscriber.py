import time
from VScontroller import speech_to_text, gcode_converter, click, change_tab, double_click
Text ="one"
print(Text)
gcode_converter(Text)
change_tab()
time.sleep(1)
click(90, 50)
double_click(170, 235)
time.sleep(0.5)
click(230, 50)