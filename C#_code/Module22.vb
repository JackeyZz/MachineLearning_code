Imports System.Console
Module Module22
    Sub main()
        Dim a(9) As Integer
        Dim b(3, 3) As Integer
        Dim i%, j%
        For i = 1 To 9
            a(i) = i
        Next i
        For i = 1 To 3
            For j = 1 To 3
                b(i, j) = a(i * j)
                If j <= i Then Write("{0}  ", b(i, j))
            Next j
            WriteLine()
        Next i
    End Sub
End Module
