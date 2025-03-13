connection_panel = """
    QFrame {
        background-color: #A9A9A9;
        border: none;
        border-radius: 0px;
        margin: 0;
        padding: 0px;
    }    
    QLabel {
        color: #000000;
        font: 16px "Segoe UI";
        margin: 0;
        padding: 0;
    }
    QLineEdit{
        background-color: #808080;
        color: #000000;
        padding: 5px;
        border: 1px solid #808080;
        border-radius: 10px;
    }
    QTextEdit {
        background-color: #808080;
        color: #000000;
        padding: 5px;
        border: 1px solid #808080;
        border-radius: 10px;
    }
    QPushButton {
        background-color: #dee2e6;
        color: #696969;
        border: 2px solid #dee2e6;
        border-radius: 5px;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #bdc2c7;
    }
"""

connection_panel_title = """
    QLabel {
        color: #ffffff;
        font: 18px "Segoe UI";
        margin: 0;
        padding: 0px;
        border: none;
        border-bottom: 2px solid #dee2e6;  
        border-radius: 0px;
    }
"""

connection_panel_subpanels_text = """    
    QLabel {
        color: #000000;
        font: 14px "Segoe UI";
        margin: 5px 0;
        padding: 5px;
        height: 60px;
        border: none;
        qproperty-alignment: 'AlignJustify';
    }
"""

connection_panel_subpanels_title = """    
   QLabel {
        color: #000000;
        font: 16px "Segoe UI";
        margin: 0;
        padding: 0;
        border: none;
    }
"""

connection_panel_subpanels = """    
    QFrame {
        background-color: #A9A9A9;
        border: 2px solid #dee2e6;
        border-radius: 5px;
        padding: 0px;
        margin: 0px;
    }  
"""

status_indicator_connected = "background-color: #008000; border-radius: 10px; border: 1px solid #000000;"
status_indicator_disconnected = "background-color: #800000; border-radius: 10px; border: 1px solid #000000;"

strim_panel = """
    QFrame {
        background-color: #495057;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 10px;
    }
"""