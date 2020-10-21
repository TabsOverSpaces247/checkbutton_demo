"""
Program: checkbutton.demo.py
Author: Serghie 10/19/20

This GUI-based program allows the user to select their food options via checkboxes and then outputs their selection.
"""

from breezypythongui import EasyFrame

class CheckbuttonDemo(EasyFrame):
	""" Allows the user to place a restaurant order from a set of checkbox options."""

	def __init__(self):
		""" Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Check Button Demo")

		# Add four checkbuttons
		self.chickCB = self.addCheckbutton(text = "Chicken", row = 0, column = 0)
		self.taterCB = self.addCheckbutton(text = "French Fries", row = 0, column = 1)
		self.beanCB = self.addCheckbutton(text = "Green Beans", row = 1, column = 0)
		self.sauceCB = self.addCheckbutton(text = "Applesauce", row = 1, column = 1)

		# Add the command button
		self.addButton(text = "Place Order", row = 2, column = 0, columnspan = 2, command = self.placeOrder)

	#Event handling method
	def placeOrder(self):
		""" Displays a message box with the order summary. """
		message = ""
		if self.chickCB.isChecked():
			message += "Chicken\n\n"
		if self.taterCB.isChecked():
			message += "French Fries\n\n"
		if self.beanCB.isChecked():
			message += "Green Beans\n\n"
		if self.sauceCB.isChecked():
			message += "Applesauce\n"
		if message == "":
			message = "No food ordered!"

		# Generate a message dialog with message variable text
		self.messageBox(title = "Customer Order", message = message)

# Definition of the main function
def main():
	CheckbuttonDemo().mainloop()

# Global call to the main() function
main()