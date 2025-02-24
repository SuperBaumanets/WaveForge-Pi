subtab = """
QPushButton {
    background-color: #FFFFFF;     /* Цвет фона */
    color: #000000;                /* Цвет текста */
    border: 3px solid #77767B;     /* Граница (ширина стиль цвет) */
    border-radius: 0;              /* Скругление углов */
    padding: 12px 24px;            /* Внутренние отступы */
    margin: 0;                     /* Внешние отступы */
    font-family: "Roboto";          /* Шрифт */
    font-size: 18px;               /* Размер шрифта */
    font-weight: normal;             /* Жирность текста */
    text-align: left;              /* Выравнивание текста */
    width: 300px;              
    height: 20px;              
      
}

QPushButton:checked {
    border: 3px solid #008A00;
    color: #FFFFFF;
    font-weight: normal;            
    background: #008A00;
    margin: 0;
}

QPushButton:disabled {
    border: 3px solid #77767B;
    background: #FFFFFF;
    font-weight: normal; 
    margin: 0;
}

QPushButton:checked:disabled {
    border: 3px solid #008A00;
    color: #FFFFFF;
    font-weight: normal;            
    background: #008A00;
    margin: 0;
}
"""

tab = """
QPushButton {
    background-color: #FFFFFF;
    color: #000000;
    border: 3px solid #77767B;
    border-radius: 3px;
    padding: 12px 24px 12px 5px;
    margin: 0;
    font-family: "Roboto";
    font-size: 18px;
    font-weight: bold;
    text-align: left;
    width: 300px;
    min-height: 20px;
}

QPushButton::icon {
    width: 20px;
    height: 20px;
    left: 15px;
}

QPushButton:!checked {
    qproperty-icon: url(src/resources/icons/triangle-right.svg);
}

QPushButton:checked {
    qproperty-icon: url(src/resources/icons/triangle-down.svg);
}

QPushButton:hover, 
QPushButton:checked {
    border: 3px solid #77767B;
    background: #F2F2F2;
}
"""

panel = """
QWidget {
    background-color: #FFFFFF;
}  
"""