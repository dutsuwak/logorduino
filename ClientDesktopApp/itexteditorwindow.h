#ifndef ITEXTEDITORWINDOW_H
#define ITEXTEDITORWINDOW_H

#include <QMainWindow>
#include <QTcpSocket>
#include <QThread>
#include <QtGui>
#include <QtCore>
#include <QFileDialog>

namespace Ui {class ITextEditorWindow;}

class ITextEditorWindow : public QMainWindow{
    Q_OBJECT

public:
    explicit ITextEditorWindow(QWidget *parent = 0);
    ~ITextEditorWindow();
    bool passConfigAndInit(QString pIp, int pPort);

private slots:
    void on_actionExit_triggered();

    void on_actionCheck_triggered();

    void on_actionRun_triggered();

    void on_actionNew_triggered();

    void on_actionOpen_triggered();

    void on_actionSave_triggered();

    void on_actionCopy_triggered();

    void on_actionPaste_triggered();

    void on_actionUndo_triggered();

    void on_actionRedo_triggered();

    void on_actionSave_as_triggered();

    void on_actionPaste_2_triggered();

    void on_actionCut_triggered();

    void on_actionInformation_triggered();

private:
    Ui::ITextEditorWindow *ui;
    QTcpSocket* mySocket;
    bool sendCode(QString pCode,bool act);
    void setTitlename(QString pName);

    QString mFilename;
};

#endif // ITEXTEDITORWINDOW_H
