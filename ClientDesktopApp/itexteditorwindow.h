#ifndef ITEXTEDITORWINDOW_H
#define ITEXTEDITORWINDOW_H

#include <QMainWindow>

namespace Ui {
class ITextEditorWindow;
}

class ITextEditorWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit ITextEditorWindow(QWidget *parent = 0);
    ~ITextEditorWindow();

private:
    Ui::ITextEditorWindow *ui;
};

#endif // ITEXTEDITORWINDOW_H
