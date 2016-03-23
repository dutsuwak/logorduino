#include "itexteditorwindow.h"
#include "ui_itexteditorwindow.h"

ITextEditorWindow::ITextEditorWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ITextEditorWindow)
{
    ui->setupUi(this);
    this->setWindowTitle("Logorduino text code editor");
}

ITextEditorWindow::~ITextEditorWindow()
{
    delete ui;
}
