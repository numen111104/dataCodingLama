Dim myArt As String

myArt = _
    "       ____             " & vbNewLine & _
    "      / __ \ ___  _   __" & vbNewLine & _
    "     / / / // _ \| | / /" & vbNewLine & _
    "    / /_/ //  __/| |/ / " & vbNewLine & _
    "   /_____/ \___/ |___/  " & vbNewLine & _
    "                        " & vbNewLine

shellOUT = oShell.Run("cmd.exe /s /c echo " & myArt & ..., vbNormalFocus, True)