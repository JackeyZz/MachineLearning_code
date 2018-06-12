Imports System.Console
Module Module23
    Sub Main()
        Dim a(4, 4) As Integer, i%, j%
        For i = 0 To 4
            For j = 0 To 4
                If i <= j Then a(i, j) = 1 Else a(i, j) = i - j + 1
            Next j
        Next i
        For i = 0 To 4
            For j = 0 To 4
                Write("{0}  ", a(i, j))
            Next j
            WriteLine()
        Next i
    End Sub
End Module
