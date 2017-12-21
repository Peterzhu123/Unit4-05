# Created by: Peter Zhu
# Created on Nov 
# Created for ICS3U
# This program calculates the volume of a cylinder.

import ui

PI = 3.14

def calculate_button(sender):
    input_height = int(view['height_textfield'].text)
    input_radius = int(view['radius_textfield'].text)
    
    final_answer = PI*2.00*input_radius*2.00*input_height
    view['answer_label'].text = str(final_answer)

view = ui.load_view()
view.present('sheet')
