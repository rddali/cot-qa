from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

 
