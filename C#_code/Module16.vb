Imports System.Console
Imports System.Math
Module Module16
    Sub f(ByRef value As Integer)
        Write(value Mod 10)
        If value \ 10 <> 0 Then
            f(value \ 10)
        End If
    End Sub
    Sub Main()
        f(456654)
    End Sub
End Module
