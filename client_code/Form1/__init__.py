from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  answer = ""
  def Submit_click(self, **event_args):
    answer = anvil.server.call('query',self.text_area_1.text )

  text_area_2.text = answer

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

 
