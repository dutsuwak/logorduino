#-------------------------------------------------
#
# Project created by QtCreator 2016-03-22T10:02:34
#
#-------------------------------------------------

QT       += core gui
QT       += network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = ClientDesktopApp
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    itexteditorwindow.cpp \
    ibashcode.cpp \

HEADERS  += mainwindow.h \
    itexteditorwindow.h \
    ibashcode.h

FORMS    += mainwindow.ui \
    itexteditorwindow.ui \
    ibashcode.ui

RESOURCES += \
    resources.qrc
