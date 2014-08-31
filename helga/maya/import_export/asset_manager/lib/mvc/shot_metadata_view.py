
"""
shot_metadata_view
==========================================

Subclass of QTableView to display shot metadata
"""




#Import
#------------------------------------------------------------------
#python
import logging
#PySide
from PySide import QtGui
from PySide import QtCore





#Import variable
do_reload = True


#asset_manager

#lib.mvc

#asset_manager_view_functionality
from lib.mvc import asset_manager_view_functionality
if(do_reload):reload(asset_manager_view_functionality)






#ShotMetadataView class
#------------------------------------------------------------------
class ShotMetadataView(QtGui.QTableView):
    """
    Subclass of QTableView.
    """

    def __new__(cls, *args, **kwargs):
        """
        ShotMetadataView instance factory.
        """

        #shot_metadata_view_instance
        shot_metadata_view_instance = super(ShotMetadataView, cls).__new__(cls, args, kwargs)

        return shot_metadata_view_instance
    
    
    def __init__(self, 
                logging_level = logging.DEBUG,
                parent=None):
    	"""
    	Customize instance.
    	"""
        
        #super class constructor
        super(ShotMetadataView, self).__init__(parent)


        #instance variables
        #------------------------------------------------------------------

        #view_functionality
        self.view_functionality = asset_manager_view_functionality.AssetManagerViewFunctionality(view = self)
        
        #logger
        #------------------------------------------------------------------
        #logger
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logging_level = logging_level
        self.logger.setLevel(self.logging_level)


    


    













