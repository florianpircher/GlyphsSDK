# encoding: utf-8


from plugin import *
from AppKit import *



class ____PluginClassName____(ReporterPlugin):

	def settings(self):
		self.menuName = 'My Plugin'
		self.generalContextMenus = [
			["Do Something", self.doSomething],
		]
		
	def drawForeground(self, layer):
		NSColor.blueColor().set()
		NSBezierPath.fillRect_(layer.bounds)
		self.drawTextAtPoint(layer.parent.name, NSPoint(0, 0))

	def drawBackgroundForInactiveLayers(self, layer):
		NSColor.redColor().set()
		if layer.paths:
			layer.bezierPath().fill()
		if layer.components:
			for component in layer.components:
				component.bezierPath().fill()

	def drawPreview(self, layer):
		NSColor.blueColor().set()
		layer.bezierPath().fill()
	
	def doSomething(self):
		print 'Just did something'
		
	def conditionalContextMenus(self):

		# Empty list of context menu items
		contextMenus = []

		# Execute only if layers are actually selected
		if Glyphs.font.selectedLayers:
			layer = Glyphs.font.selectedLayers[0]
			
			# Exactly one object is selected and it’s an anchor
			if len(layer.selection) == 1 and type(layer.selection[0]) == GSAnchor:
					
				# Add context menu item
				contextMenus.append(["Do something else", self.doSomethingElse])

		# Return list of context menu items
		return contextMenus

	def doSomethingElse(self):
		print 'Just did something else'
