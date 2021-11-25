<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>330</width>
    <height>408</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>157</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Financial analyser</string>
    </property>
    <property name="textFormat">
     <enum>Qt::PlainText</enum>
    </property>
   </widget>
   <widget class="QListWidget" name="listWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>130</y>
      <width>81</width>
      <height>51</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Transport</string>
     </property>
     <property name="checkState">
      <enum>Unchecked</enum>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Products</string>
     </property>
     <property name="checkState">
      <enum>Unchecked</enum>
     </property>
     <property name="flags">
      <set>ItemIsSelectable|ItemIsEditable|ItemIsUserCheckable|ItemIsEnabled</set>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Flat</string>
     </property>
     <property name="checkState">
      <enum>Unchecked</enum>
     </property>
     <property name="flags">
      <set>ItemIsSelectable|ItemIsEditable|ItemIsDragEnabled|ItemIsUserCheckable|ItemIsEnabled</set>
     </property>
    </item>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>50</y>
      <width>71</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Import amoumt</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>110</y>
      <width>71</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Import item</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>190</y>
      <width>56</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>OK</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>70</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>330</width>
     <height>18</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
