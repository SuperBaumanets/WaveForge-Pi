main_layout = """
QFrame {
    background-color: #FFFFFF;
    border: 0px solid #000000;
    border-radius: 0px;
}

QScrollArea {
    border: 0px solid #000000;      /* Убрать стандартную рамку */
    background: transparent;        /* Прозрачный фон */
}

QScrollBar::handle:hover {
    background: #495057;   
}

QScrollBar::add-page, 
QScrollBar::sub-page {
    background: none;               /* Убрать фон за полосой */
}
"""

sub_layout = """
QFrame {
    background-color: #FFFFFF;
    border: 2px solid #77767B !important;
    border-radius: 0px;
    padding: 5px;
}

QLabel {
    background-color: #FFFFFF;
    border: 0px;
    border-radius: 0px;
    padding: 0px 0px;
    font-family: "Roboto";
    font-size: 16px;
    font-weight: bold;
    color: #2E3291;
    margin: 0px 0px;
}

QPushButton {
    background-color: #008A00;
    color: #FFFFFF;
    border: 2px solid #005700;
    border-radius: 5px;
    margin: 3px 10px;
    font-family: "Roboto";
    font-size: 14px !important;
    width: 20px;
    min-height: 30px;
}

QPushButton:hover, 
QPushButton:checked {
    border: 2px solid #005700;
    background: #0E7016;
}

QTextEdit {
    background-color: #FFFFFF;
    color: #77767B;
    border: 2px solid #3D3846;
    border-radius: 5px;
    font-family: "Roboto";
    font-size: 12px;
    margin: 3px 10px;
}

QScrollBar::handle:hover {
    background: #495057;       
}

QScrollBar::add-page, 
QScrollBar::sub-page {
    background: none; 
}

QLineEdit{
    background-color: #FFFFFF;
    color: #77767B;
    border: 2px solid #3D3846;
    border-radius: 5px;
    font-family: "Roboto";
    font-size: 12px;
    margin: 3px 10px;
}

QFrame#plot_container {
    background: #FFFFFF;
    border: 0px solid #3D3846;
    border-radius: 0px;
    padding: 0px;
}

QComboBox{
    background-color: #008A00;
    border: 2px solid #005700;
    border-radius: 5px;
    font-family: "Roboto";
    font-size: 14px;
    color: #FFFFFF;
    padding-right: 10px;
    margin: 2px 5px;
    selection-background-color: #77767B;
    width: 20px;
    min-height: 30px;
}

QComboBox:hover {
    background-color: #0E7016;
    border: 2px solid #005700;
}

QComboBox:pressed {
    background-color: #005700;
}

QComboBox QAbstractItemView {
    border: 2px solid #005700;
    border-radius: 5px;
    background-color: #008A00;
    padding: 4px 0;
    margin-top: 4px;
    outline: none;
}

QComboBox QAbstractItemView::item {
    height: 32px;
    padding: 0 12px;
    color: #4A4A4A;
}

QCheckBox {
    spacing: 8px;
    font-size: 14px;
    color: #005700;
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 2px solid #005700;
    border-radius: 4px;
}
QCheckBox::indicator:checked {
    background-color: #005700;
    border: 2px solid #005700;
    image: url(src/resources/icons/check.svg);
}
QCheckBox::indicator:hover {
    border: 2px solid #005700;
    color: #0E7016;
}
"""

sub_explanations = """
QLabel {
    background-color: #FFFFFF;
    border: 0px;
    border-radius: 0px;
    padding: 0px 0px;
    font-family: "Roboto";
    font-size: 12px;
    color: #2E3291;
    margin: 3px 10px;
    qproperty-alignment: 'AlignJustify';
}
"""

status = """
QFrame {
    background-color: #FFFFFF;
    border: none;
    border-radius: 0px;
    padding: 5px;
}
"""