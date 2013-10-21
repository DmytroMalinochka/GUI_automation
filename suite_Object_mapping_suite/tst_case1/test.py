
def main():
    startApplication("qagui")
    snooze(7)



    clickButton(":MainWindow.button_CheckUnchekSuppressions")
    snooze(1)
    activateItem(waitForObjectItem(":MainWindow_QMenu", "Show comment suppressed diagnostics"))
    snooze(1)