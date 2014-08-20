from Products.Archetypes.public import ImageField, ImageWidget, StringField, StringWidget
from Products.ATContentTypes.interface import IATEvent
from Products.Archetypes.atapi import *
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender
from zope.interface import implements, Interface
from zope.component import adapts, provideAdapter
from interfaces import IEventExtenderLayer

class _ExtensionImageField(ExtensionField, ImageField): pass
class _ExtensionStringField(ExtensionField, StringField): pass

class eventsImageExtender(object):
    adapts(IATEvent)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)
    
    layer = IEventExtenderLayer

    fields = [
        _ExtensionImageField(
            "eventimage",
                widget = ImageWidget(
                label=u"Event Image",
                description=u"Image to display with the Event",
            ),
        ),
        _ExtensionStringField(
            "folderimagetitle",
            widget = StringWidget(
                label=u"Image Title",
                description=u"Title of image to display with the Event",
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields