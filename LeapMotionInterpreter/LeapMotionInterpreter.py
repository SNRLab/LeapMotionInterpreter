# -*- coding: utf-8 -*-

from __main__ import vtk, qt, ctk, slicer
import os


class LeapMotionInterpreter:
    def __init__(self, parent):
        parent.title = "Leap Motion Interpreter"
        parent.categories = ["Utilities"]
        parent.contributors = ["Andrew Zheng"]
        parent.helpText = """
        This module enables the usage of 3D Slicer with the Leap Motion Controller.
        """
        parent.acknowledgementText = """
        Nobuhiko Hata, PhD, Franklin King, MS
        """        
        parent.icon = qt.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\Leap Motion GUI\icon.png')
        self.parent = parent


class LeapMotionInterpreterWidget:
    def __init__(self, parent=None):
        if not parent:
            self.parent = slicer.qMRMLWidget()
            self.parent.setLayout(qt.QVBoxLayout())
            self.parent.setMRMLScene(slicer.mrmlScene)
        else:
            self.parent = parent
            self.layout = self.parent.layout()
        if not parent:
            self.setup()
            self.parent.show()

    def setup(self):
        self.dir = os.path.dirname(os.path.realpath(__file__))
    
        self.n = 1
        self.m = 1

        self.layoutmanager = slicer.app.layoutManager()
        self.layoutmanager.setLayout(5)

        #
        # Setup
        #
        setupWindow = ctk.ctkCollapsibleButton()
        setupWindow.text = 'Setup'
        self.layout.addWidget(setupWindow)
        self.setupLayout = qt.QFormLayout(setupWindow)

        # Volume set A
        volumeset1 = ctk.ctkCollapsibleGroupBox()
        volumeset1.setTitle('Volume Set A:')
        self.setupLayout.addRow(volumeset1)
        self.volumeset1Layout = qt.QFormLayout(volumeset1)

        # Foreground volume node selector A
        self.foregroundvolumeNodeSelector0 = slicer.qMRMLNodeComboBox()
        self.foregroundvolumeNodeSelector0.nodeTypes = (("vtkMRMLVolumeNode"), "")
        self.foregroundvolumeNodeSelector0.selectNodeUponCreation = True
        self.foregroundvolumeNodeSelector0.addEnabled = False
        self.foregroundvolumeNodeSelector0.removeEnabled = False
        self.foregroundvolumeNodeSelector0.noneEnabled = True
        self.foregroundvolumeNodeSelector0.showHidden = False
        self.foregroundvolumeNodeSelector0.showChildNodeTypes = True
        self.foregroundvolumeNodeSelector0.setMRMLScene(slicer.mrmlScene)
        self.volumeset1Layout.addRow("Foreground Volume: ", self.foregroundvolumeNodeSelector0)

        # Background volume node selector A
        self.backgroundvolumeNodeSelector0 = slicer.qMRMLNodeComboBox()
        self.backgroundvolumeNodeSelector0.nodeTypes = (("vtkMRMLVolumeNode"), "")
        self.backgroundvolumeNodeSelector0.selectNodeUponCreation = True
        self.backgroundvolumeNodeSelector0.addEnabled = False
        self.backgroundvolumeNodeSelector0.removeEnabled = False
        self.backgroundvolumeNodeSelector0.noneEnabled = False
        self.backgroundvolumeNodeSelector0.showHidden = False
        self.backgroundvolumeNodeSelector0.showChildNodeTypes = True
        self.backgroundvolumeNodeSelector0.setMRMLScene(slicer.mrmlScene)
        self.volumeset1Layout.addRow("Background Volume: ", self.backgroundvolumeNodeSelector0)

        # Volume set B
        volumeset2 = ctk.ctkCollapsibleGroupBox()
        volumeset2.setTitle('Volume Set B:')
        self.setupLayout.addRow(volumeset2)
        self.volumeset2Layout = qt.QFormLayout(volumeset2)

        # Foreground volume node selector B
        self.foregroundvolumeNodeSelector1 = slicer.qMRMLNodeComboBox()
        self.foregroundvolumeNodeSelector1.nodeTypes = (("vtkMRMLVolumeNode"), "")
        self.foregroundvolumeNodeSelector1.selectNodeUponCreation = True
        self.foregroundvolumeNodeSelector1.addEnabled = False
        self.foregroundvolumeNodeSelector1.removeEnabled = False
        self.foregroundvolumeNodeSelector1.noneEnabled = True
        self.foregroundvolumeNodeSelector1.showHidden = False
        self.foregroundvolumeNodeSelector1.showChildNodeTypes = True
        self.foregroundvolumeNodeSelector1.setMRMLScene(slicer.mrmlScene)
        self.volumeset2Layout.addRow("Foreground Volume: ", self.foregroundvolumeNodeSelector1)

        # Background volume node selector B
        self.backgroundvolumeNodeSelector1 = slicer.qMRMLNodeComboBox()
        self.backgroundvolumeNodeSelector1.nodeTypes = (("vtkMRMLVolumeNode"), "")
        self.backgroundvolumeNodeSelector1.selectNodeUponCreation = True
        self.backgroundvolumeNodeSelector1.addEnabled = False
        self.backgroundvolumeNodeSelector1.removeEnabled = False
        self.backgroundvolumeNodeSelector1.noneEnabled = True
        self.backgroundvolumeNodeSelector1.showHidden = False
        self.backgroundvolumeNodeSelector1.showChildNodeTypes = True
        self.backgroundvolumeNodeSelector1.setMRMLScene(slicer.mrmlScene)
        self.volumeset2Layout.addRow("Background Volume: ", self.backgroundvolumeNodeSelector1)

        # Volume Set C
        volumeset3 = ctk.ctkCollapsibleGroupBox()
        volumeset3.setTitle('Volume Set C:')
        self.setupLayout.addRow(volumeset3)
        self.volumeset3Layout = qt.QFormLayout(volumeset3)

        # Foreground volume node selector C
        self.foregroundvolumeNodeSelector2 = slicer.qMRMLNodeComboBox()
        self.foregroundvolumeNodeSelector2.nodeTypes = (("vtkMRMLVolumeNode"), "")
        self.foregroundvolumeNodeSelector2.selectNodeUponCreation = True
        self.foregroundvolumeNodeSelector2.addEnabled = False
        self.foregroundvolumeNodeSelector2.removeEnabled = False
        self.foregroundvolumeNodeSelector2.noneEnabled = True
        self.foregroundvolumeNodeSelector2.showHidden = False
        self.foregroundvolumeNodeSelector2.showChildNodeTypes = True
        self.foregroundvolumeNodeSelector2.setMRMLScene(slicer.mrmlScene)
        self.volumeset3Layout.addRow("Foreground Volume: ", self.foregroundvolumeNodeSelector2)

        # Background volume node selector 3
        self.backgroundvolumeNodeSelector2 = slicer.qMRMLNodeComboBox()
        self.backgroundvolumeNodeSelector2.nodeTypes = (("vtkMRMLVolumeNode"), "")
        self.backgroundvolumeNodeSelector2.selectNodeUponCreation = True
        self.backgroundvolumeNodeSelector2.addEnabled = False
        self.backgroundvolumeNodeSelector2.removeEnabled = False
        self.backgroundvolumeNodeSelector2.noneEnabled = True
        self.backgroundvolumeNodeSelector2.showHidden = False
        self.backgroundvolumeNodeSelector2.showChildNodeTypes = True
        self.backgroundvolumeNodeSelector2.setMRMLScene(slicer.mrmlScene)
        self.volumeset3Layout.addRow("Background Volume: ", self.backgroundvolumeNodeSelector2)

        # Text node selector
        self.textNodeSelector = slicer.qMRMLNodeComboBox()
        self.textNodeSelector.nodeTypes = (("vtkMRMLTextNode"), "")
        self.textNodeSelector.selectNodeUponCreation = True
        self.textNodeSelector.addEnabled = False
        self.textNodeSelector.removeEnabled = False
        self.textNodeSelector.noneEnabled = False
        self.textNodeSelector.showHidden = False
        self.textNodeSelector.showChildNodeTypes = True
        self.textNodeSelector.setMRMLScene(slicer.mrmlScene)
        self.setupLayout.addRow("Controller Data: ", self.textNodeSelector)

        # Camera node selector
        self.cameraNodeSelector = slicer.qMRMLNodeComboBox()
        self.cameraNodeSelector.nodeTypes = (("vtkMRMLCameraNode"), "")
        self.cameraNodeSelector.selectNodeUponCreation = True
        self.cameraNodeSelector.addEnabled = False
        self.cameraNodeSelector.removeEnabled = False
        self.cameraNodeSelector.noneEnabled = False
        self.cameraNodeSelector.showHidden = False
        self.cameraNodeSelector.showChildNodeTypes = True
        self.cameraNodeSelector.setMRMLScene(slicer.mrmlScene)
        self.setupLayout.addRow("Scene Camera: ", self.cameraNodeSelector)

        # Display data confidence
        self.confidenceLabel = qt.QLabel("")
        self.setupLayout.addRow("Data Confidence:", self.confidenceLabel)
        self.confidenceLabel.setText("                                                                             ")
        # Show corner text
        self.cornerTextCheck = qt.QCheckBox()
        self.setupLayout.addRow("Show Corner Text:", self.cornerTextCheck)

        #
        # Connect/Disconnect Leap Motion Controller
        #
        connectWindow = ctk.ctkCollapsibleButton()
        connectWindow.text = "Leap Motion Controller Connector"
        self.layout.addWidget(connectWindow)
        self.connectLayout = qt.QFormLayout(connectWindow)

        # Connect controller
        self.controllerConnect = qt.QPushButton('Connect Leap Motion Controller')
        self.controllerConnect.clicked.connect(self.ControllerConnect)
        self.connectLayout.addWidget(self.controllerConnect)
        # Disabled until volume selected
        self.controllerConnect.setEnabled(0)
        self.controllerConnect.setText('Connect Leap Motion Controller (Load a volume first!)')

        # Disconnect controller
        self.controllerDisconnect = qt.QPushButton('Disconnect Leap Motion Controller')
        self.controllerDisconnect.clicked.connect(self.ControllerDisconnect)
        self.connectLayout.addWidget(self.controllerDisconnect)

        # Disabled until volume selected
        self.controllerDisconnect.setEnabled(0)
        self.controllerDisconnect.setText('Disconnect Leap Motion Controller (Load a volume first!)')

        #
        # Gesture Selection Visualizer
        #
        visualizerWindow = ctk.ctkCollapsibleButton()
        visualizerWindow.text = 'Gesture/Selection Visualizer'
        self.layout.addWidget(visualizerWindow)
        self.visualizerLayout = qt.QFormLayout(visualizerWindow)

        # Size policy
        qSize = qt.QSizePolicy()
        qSize.setHorizontalPolicy(qt.QSizePolicy.Ignored)
        qSize.setVerticalPolicy(qt.QSizePolicy.Preferred)

        #Gesture visualizer
        gestureVisualizerCollapsibleBox = ctk.ctkCollapsibleGroupBox()
        gestureVisualizerCollapsibleBox.setTitle("Gesture Visualizer")
        self.visualizerLayout.addRow(gestureVisualizerCollapsibleBox)
        gestureVisualizerLayout = qt.QFormLayout(gestureVisualizerCollapsibleBox)
        self.label1 = qt.QLabel()
        self.label1.setScaledContents(True)
        self.label1.setMargin(0)
        image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_overview.png")
        self.label1.setPixmap(image)
        self.label1.setSizePolicy(qSize)
        gestureVisualizerLayout.addWidget(self.label1)

        #Selection visualizer
        selectionVisualizerLayoutCollapsibleBox = ctk.ctkCollapsibleGroupBox()
        selectionVisualizerLayoutCollapsibleBox.setTitle("Selection Visualizer")
        self.visualizerLayout.addRow(selectionVisualizerLayoutCollapsibleBox)
        selectionVisualizerLayout = qt.QFormLayout(selectionVisualizerLayoutCollapsibleBox)
        self.label2 = qt.QLabel()
        self.label2.setScaledContents(True)
        self.label2.setMargin(0)
        image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_category (1).png")
        self.label2.setPixmap(image)
        self.label2.setSizePolicy(qSize)
        selectionVisualizerLayout.addWidget(self.label2)
        self.label3 = qt.QLabel()
        self.label3.setScaledContents(True)
        self.label3.setMargin(0)
        
        image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_sliceview.png")
        self.label3.setPixmap(image)
        self.label3.setSizePolicy(qSize)
        selectionVisualizerLayout.addWidget(self.label3)

        # Vertical spacer
        self.layout.addStretch(1)

        slicer.mrmlScene.AddObserver(slicer.mrmlScene.NodeAddedEvent, self.dataInterpreter)

    def ControllerConnect(self):
        if self.m == 1:
            self.client = slicer.vtkMRMLIGTLConnectorNode()
            slicer.mrmlScene.AddNode(self.client)
            self.client.SetTypeClient('localhost', 18944)
            self.client.Start()
            self.status = slicer.vtkMRMLIGTLStatusNode()
            slicer.mrmlScene.AddNode(self.status)
            self.m -= 1
        else:
            self.client.Start()

    def ControllerDisconnect(self):
        self.client.Stop()

    def dataInterpreter(self, caller, event):
        if self.backgroundvolumeNodeSelector0.currentNode() is not None:
            self.controllerConnect.setEnabled(1)
            self.controllerConnect.setText('Connect Leap Motion Controller')
            self.controllerDisconnect.setEnabled(1)
            self.controllerDisconnect.setText('Disconnect Leap Motion Controller')
        self.textNode = self.textNodeSelector.currentNode()
        self.cameraNode = self.cameraNodeSelector.currentNode()
        # Runs only once if no errors
        while self.n > 0:
            # Corner annotations of views
            self.redviewAnnotation = self.layoutmanager.sliceWidget('Red').sliceView().cornerAnnotation()
            self.greenviewAnnotation = self.layoutmanager.sliceWidget('Green').sliceView().cornerAnnotation()
            self.yellowviewAnnotation = self.layoutmanager.sliceWidget('Yellow').sliceView().cornerAnnotation()
            self.viewAnnotation = self.layoutmanager.threeDWidget(0).threeDView().cornerAnnotation()
            # Get slice offset
            self.green = self.layoutmanager.sliceWidget('Green')
            self.greenLogic = self.green.sliceLogic()
            self.greenPos = self.greenLogic.GetSliceOffset()
            self.yellow = self.layoutmanager.sliceWidget('Yellow')
            self.yellowLogic = self.yellow.sliceLogic()
            self.yellowPos = self.yellowLogic.GetSliceOffset()
            self.red = self.layoutmanager.sliceWidget('Red')
            self.redLogic = self.red.sliceLogic()
            self.redPos = self.redLogic.GetSliceOffset()
            # Get Foreground slice opacity
            self.redcompositeNode = self.redLogic.GetSliceCompositeNode()
            self.redopacity = self.redcompositeNode.GetForegroundOpacity()
            self.yellowcompositeNode = self.yellowLogic.GetSliceCompositeNode()
            self.yellowopacity = self.yellowcompositeNode.GetForegroundOpacity()
            self.greencompositeNode = self.greenLogic.GetSliceCompositeNode()
            self.greenopacity = self.greencompositeNode.GetForegroundOpacity()
            # Initial value if modifying opacity of all slices
            self.allopacity = 0
            # Avoid nonetype error
            if self.textNode is None:
                return
            self.textNode.AddObserver("ModifiedEvent", self.dataInterpreter)
            # Camera object of camera node
            self.camera = self.cameraNode.GetCamera()
            # x = yaw, roll = y, pitch = z, pertains to 3D view position
            self.x = 0
            self.y = 0
            self.z = 0
            self.zoom = self.cameraNode.GetViewAngle()
            # amp = hand velocity
            self.amp = 0
            # Slice view, scene view, window/level, viewer layout, foreground opacity, volume set selection
            self.category = 0
            self.subcategorytitle = "None"
            self.subcategory = -1
            # Layout of slice viewer
            self.layoutcount = self.layoutmanager.layout
            # Counter for volume sets 1,2,3
            self.volumesetcount = 0
            # Above code runs only once
            self.n -= 1
        # Foreground, background volume set selection
        if self.volumesetcount == 0:
            self.foregroundvolumeNode = self.foregroundvolumeNodeSelector0.currentNode()
            self.backgroundvolumeNode = self.backgroundvolumeNodeSelector0.currentNode()
        elif self.volumesetcount == 1:
            self.foregroundvolumeNode = self.foregroundvolumeNodeSelector1.currentNode()
            self.backgroundvolumeNode = self.backgroundvolumeNodeSelector1.currentNode()
        elif self.volumesetcount == 2:
            self.foregroundvolumeNode = self.foregroundvolumeNodeSelector2.currentNode()
            self.backgroundvolumeNode = self.backgroundvolumeNodeSelector2.currentNode()
        # Get foreground window/level
        if self.foregroundvolumeNode is not None:
            self.foregrounddisplaynode = self.foregroundvolumeNode.GetDisplayNode()
            if self.foregrounddisplaynode:
                self.foregrounddisplaynode.AutoWindowLevelOff()
                self.windowforeground = self.foregrounddisplaynode.GetWindow()
                self.levelforeground = self.foregrounddisplaynode.GetLevel()
        # Get background window/level
        if self.backgroundvolumeNode is not None:
            self.backgrounddisplaynode = self.backgroundvolumeNode.GetDisplayNode()
            if self.backgrounddisplaynode:
                self.backgrounddisplaynode.AutoWindowLevelOff()
                self.windowbackground = self.backgrounddisplaynode.GetWindow()
                self.levelbackground = self.backgrounddisplaynode.GetLevel()
        # Update slices to selected volume
        if self.foregroundvolumeNode is not None:
            for color in ['Red', 'Yellow', 'Green']:
                self.layoutmanager.sliceWidget(
                    color).sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(
                    self.foregroundvolumeNode.GetID())
        # Update slices to selected volume
        if self.backgroundvolumeNode is not None:
            for color in ['Red', 'Yellow', 'Green']:
                self.layoutmanager.sliceWidget(
                    color).sliceLogic().GetSliceCompositeNode().SetBackgroundVolumeID(
                    self.backgroundvolumeNode.GetID())
        # Get only string message from textnode LeapMotionData
        self.textNodeText = str(self.textNode)
        self.leapmotionData = self.textNodeText[
                              self.textNodeText.find('Text: ') + 1:self.textNodeText.find("Encoding:")]
        # Get slice nodes
        self.yellownode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeYellow")
        self.rednode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")
        self.greennode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeGreen")
        # Get data confidence
        if self.leapmotionData.find("confidence:") != -1:
            self.confidenceLabel.setText("%s                                                             "
                                         % (str(self.leapmotionData[self.leapmotionData.find("confidence:") + 12:
            len(self.leapmotionData)-1])))
        # Update gesture visualizer
        if self.leapmotionData.find("fingers: 1") != -1:
            image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_overview.png")
            self.label1.setPixmap(image)
        elif self.leapmotionData.find("fingers: 2") != -1:
            image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_overview (1).png")
            self.label1.setPixmap(image)
        elif self.leapmotionData.find("fingers: 3") != -1:
            image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_overview (2).png")
            self.label1.setPixmap(image)
        elif self.leapmotionData.find("fingers: 4") != -1:
            image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_overview.png")
            self.label1.setPixmap(image)
        elif self.leapmotionData.find("fingers: 5") != -1:
            image = qt.QPixmap(self.dir + "\Leap Motion GUI\GUI_overview.png")
            self.label1.setPixmap(image)
        # Recognize key tap gesture
        if self.leapmotionData.find("Key Tap ID:") != -1:
            # Recognize category selection key tap
            if self.leapmotionData.find("fingers: 2") != -1:
                # Increase category counter
                self.category += 1
                # Define category limit
                if self.category == 6:
                    self.category = 0
                # Reset subcategory counter
                self.subcategory = 0
            # Recognize subcategory selection key tap
            if self.leapmotionData.find("fingers: 3") != -1:
                # Increase category counter, define subcategory limit for each individual category
                self.subcategory += 1
                # Slice view
                if self.category == 0 and self.subcategory == 3:
                    self.subcategory = 0
                # Scene view
                elif self.category == 1 and self.subcategory == 4:
                    self.subcategory = 0
                # Foreground and background window/level
                elif self.category == 2 and self.subcategory == 4:
                    self.subcategory = 0
                # Foreground opacity
                elif self.category == 3 and self.subcategory == 4:
                    self.subcategory = 0
                # Viewer layout
                elif self.category == 4:
                    if self.layoutcount != 9:
                        self.layoutcount += 1
                    else:
                        self.layoutcount = 3
                    # Update viewer layout
                    self.layoutmanager.setLayout(self.layoutcount)
                # Volume set selection
                elif self.category == 5:
                    self.volumesetcount += 1
                    if self.volumesetcount == 3:
                        self.volumesetcount = 0
            # Update category GUI
            image = qt.QPixmap(
                self.dir + "\Leap Motion GUI\GUI_category (%s).png" % str(self.category + 1))
            self.label2.setPixmap(image)
            # Update subcategory GUI of slice view category
            if self.category == 0:
                image = qt.QPixmap(
                    self.dir + "\Leap Motion GUI\GUI_sliceview (%s).png" % str(self.subcategory + 1))
                self.label3.setPixmap(image)
                # Show slice widgets
                if self.subcategory == 0:
                    self.rednode.SetWidgetVisible(1)
                    self.yellownode.SetWidgetVisible(0)
                    self.greennode.SetWidgetVisible(0)
                elif self.subcategory == 1:
                    self.rednode.SetWidgetVisible(0)
                    self.yellownode.SetWidgetVisible(1)
                    self.greennode.SetWidgetVisible(0)
                elif self.subcategory == 2:
                    self.rednode.SetWidgetVisible(0)
                    self.yellownode.SetWidgetVisible(1)
                    self.greennode.SetWidgetVisible(0)
                # Set and update corner annotation titles
                self.subcategories = ['Red', 'Yellow', 'Green']
                self.subcategorytitle = ("Slice view, %s" % self.subcategories[self.subcategory])

            # Set and update subcategory GUI of scene view
            elif self.category == 1:
                image = qt.QPixmap(
                    self.dir + "\Leap Motion GUI\GUI_sceneview (%s).png" % str(self.subcategory + 1))
                self.label3.setPixmap(image)
                # Set and update corner annotation titles
                self.subcategories = ['Yaw', 'Roll', 'Pitch', 'Zoom']
                self.subcategorytitle = ("Scene view, %s" % self.subcategories[self.subcategory])
            # Set and update subcategory GUI of window/level
            elif self.category == 2:
                image = qt.QPixmap(
                    self.dir + "\Leap Motion GUI\GUI_windowlevel (%s).png" % str(self.subcategory + 1))
                self.label3.setPixmap(image)
                # Set and update corner annotation titles
                self.subcategories = ['Window, Foreground','Level, Foreground', 'Window, Background', 'Level, Background']
                self.subcategorytitle = self.subcategories[self.subcategory]
            # Set and update subcategory GUI of foreground opacity
            elif self.category == 3:
                image = qt.QPixmap(
                    self.dir + "\Leap Motion GUI\GUI_foregroundopacity (%s).png" % str(self.subcategory + 1))
                self.label3.setPixmap(image)
                self.subcategories = ['Red','Yellow', 'Green', 'All']
                # Set and update corner annotation titles
                self.subcategorytitle = ("Foreground Opacity, %s" % self.subcategories[self.subcategory])
            # Set subcategory GUI of viewer layout
            elif self.category == 4:
                image = qt.QPixmap(
                    self.dir + "\Leap Motion GUI\GUI_layout.png")
                self.label3.setPixmap(image)
                self.subcategorytitle = "Viewer Layout"
            # Set subcategory GUI of volume set selection
            elif self.category == 5:
                image = qt.QPixmap(
                    self.dir + "\Leap Motion GUI\GUI_volumesetselection (%s).png" % str(self.volumesetcount + 1))
                self.label3.setPixmap(image)
                self.subcategories = ['A', 'B', 'C']
                # Set and update corner annotation titles
                self.subcategorytitle = ("Volume Set Selection, %s" % self.subcategories[self.volumesetcount])
        # Recognize modification gesture
        if self.leapmotionData.find("Circle ID") != -1:
            # Update gesture visualizer
            image = qt.QPixmap(
                self.dir + "\Leap Motion GUI\GUI_overview (3).png")
            self.label1.setPixmap(image)
            # Get hand velocity
            self.amp = float(
                self.leapmotionData[
                self.leapmotionData.find("hand speed:") + 12:(self.leapmotionData.find(', confidence'))]) * 3 / 4

            #
            # Slice view modification
            #
            if self.subcategorytitle == "Slice view, Red":
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.redPos += 0.3 * self.amp
                else:
                    self.redPos -= 0.3 * self.amp
            elif self.subcategorytitle == "Slice view, Yellow":
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.yellowPos += 0.3 * self.amp
                else:
                    self.yellowPos -= 0.3 * self.amp
            elif self.subcategorytitle == "Slice view, Green":
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.greenPos += 0.3 * self.amp
                else:
                    self.greenPos -= 0.3 * self.amp

            #
            # Scene view modification
            #
            elif self.subcategorytitle == "Scene view, Yaw":
                self.y = 0
                self.z = 0
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.x = .8 * self.amp
                else:
                    self.x = -.8 * self.amp
            elif self.subcategorytitle == "Scene view, Roll":
                self.x = 0
                self.z = 0
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.y = .8 * self.amp
                else:
                    self.y = -.8 * self.amp
            elif self.subcategorytitle == "Scene view, Pitch":
                self.x = 0
                self.y = 0
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.z = .8 * self.amp
                else:
                    self.z = -.8 * self.amp
            elif self.subcategorytitle == "Scene view, Zoom":
                self.x = 0
                self.y = 0
                self.z = 0
                if self.leapmotionData.find("counterclockwise") == -1 and self.zoom <= 100:
                    self.zoom += 0.3 * self.amp
                else:
                    if self.zoom >= 5:
                        self.zoom -= 0.3 * self.amp

            #
            # Window/Level Modification
            #
            elif self.subcategorytitle == "Window, Foreground":
                if self.foregroundvolumeNode is not None:
                    if self.leapmotionData.find("counterclockwise") == -1:
                        self.windowforeground += 2 * self.amp
                    else:
                        self.windowforeground -= 2 * self.amp
                    self.foregrounddisplaynode.SetWindow(self.windowforeground)
            elif self.subcategorytitle == "Level, Foreground":
                if self.foregroundvolumeNode is not None:
                    if self.leapmotionData.find("counterclockwise") == -1:
                        self.levelforeground += 1 * self.amp
                    else:
                        self.levelforeground -= 1 * self.amp
                    self.foregrounddisplaynode.SetLevel(self.levelforeground)
            elif self.subcategorytitle == "Window, Background":
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.windowbackground += 2 * self.amp
                else:
                    self.windowbackground -= 2 * self.amp
                self.backgrounddisplaynode.SetWindow(self.windowbackground)
            elif self.subcategorytitle == "Level, Background":
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.levelbackground += 1 * self.amp
                else:
                    self.levelbackground -= 1 * self.amp
                self.backgrounddisplaynode.SetLevel(self.levelbackground)

            #
            # Foreground Opacity Modification
            #
            elif self.subcategorytitle == "Foreground Opacity, Red":
                if self.leapmotionData.find("counterclockwise") == -1 and self.redopacity <= 100:
                    self.redopacity += 0.01 * self.amp
                else:
                    if self.redopacity >= 0:
                        self.redopacity -= 0.01 * self.amp
                self.redcompositeNode.SetForegroundOpacity(self.redopacity)
            elif self.subcategorytitle == "Foreground Opacity, Yellow":
                if self.leapmotionData.find("counterclockwise") == -1 and self.yellowopacity <= 100:
                    self.yellowopacity += 0.01 * self.amp
                else:
                    if self.yellowopacity >= 0:
                        self.yellowopacity -= 0.01 * self.amp
                self.yellowcompositeNode.SetForegroundOpacity(self.yellowopacity)
            elif self.subcategorytitle == "Foreground Opacity, Green" and self.greenopacity <= 100:
                if self.leapmotionData.find("counterclockwise") == -1:
                    self.greenopacity += 0.01 * self.amp
                else:
                    if self.greenopacity >= 0:
                        self.greenopacity -= 0.01 * self.amp
                self.greencompositeNode.SetForegroundOpacity(self.greenopacity)
            elif self.subcategorytitle == "Foreground Opacity, All":
                if self.leapmotionData.find("counterclockwise") == -1 and self.allopacity <= 100:
                    self.allopacity += 0.01 * self.amp
                else:
                    if self.levelforeground >= 0:
                        self.allopacity -= 0.01 * self.amp
                for color in ['Red', 'Yellow', 'Green']:
                    self.layoutmanager.sliceWidget(color).sliceLogic().GetSliceCompositeNode().SetForegroundOpacity(self.allopacity)

            # Update slice offset
            self.redLogic.SetSliceOffset(self.redPos)
            self.yellowLogic.SetSliceOffset(self.yellowPos)
            self.greenLogic.SetSliceOffset(self.greenPos)
            self.cameraNode.SetViewAngle(self.zoom)
            # Update camera position
            self.camera.Azimuth(self.x)
            self.camera.Roll(self.y)
            self.camera.Elevation(self.z)
            self.x = 0
            self.y = 0
            self.z = 0
            self.camera.OrthogonalizeViewUp()

        #
        # Show corner text
        #
        if self.cornerTextCheck.checked:
            self.redviewAnnotation.SetText(
                vtk.vtkCornerAnnotation.LowerRight, "Selected: %s \n" % self.subcategorytitle)
            self.redviewAnnotation.GetTextProperty().SetColor(2, 2, 2)
            self.greenviewAnnotation.SetText(
                vtk.vtkCornerAnnotation.LowerRight, "Selected: %s \n" % self.subcategorytitle)
            self.greenviewAnnotation.GetTextProperty().SetColor(2, 2, 2)
            self.yellowviewAnnotation.SetText(vtk.vtkCornerAnnotation.LowerRight,
                                              "Selected: %s \n" % self.subcategorytitle)
            self.yellowviewAnnotation.GetTextProperty().SetColor(2, 2, 2)
            self.viewAnnotation.GetTextProperty().SetColor(2, 2, 2)
            self.viewAnnotation.SetText(vtk.vtkCornerAnnotation.LowerRight, "Selected: %s \n" % self.subcategorytitle)
            self.viewAnnotation.GetTextProperty().SetColor(2, 2, 2)
        else:
            self.redviewAnnotation.SetText(vtk.vtkCornerAnnotation.LowerRight, '')
            self.greenviewAnnotation.SetText(vtk.vtkCornerAnnotation.LowerRight, '')
            self.yellowviewAnnotation.SetText(vtk.vtkCornerAnnotation.LowerRight, '')
            self.viewAnnotation.SetText(vtk.vtkCornerAnnotation.LowerRight, '')

        # Force layoutmanager update to show/hide annotations
        self.redview = self.layoutmanager.sliceWidget('Red').sliceView()
        self.redview.forceRender()
        self.greenview = self.layoutmanager.sliceWidget('Green').sliceView()
        self.greenview.forceRender()
        self.yellowview = self.layoutmanager.sliceWidget('Yellow').sliceView()
        self.yellowview.forceRender()
        self.view = self.layoutmanager.threeDWidget(0).threeDView()
        self.view.forceRender()
