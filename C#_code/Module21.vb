Imports System.Console
Imports System.Math
Module Module21

    Sub main()
        Dim i, s(5), t As Integer
        For i = 0 To 5
            s(i) = i
        Next i
        For i = 0 To 2
            For j = 3 To 5
                t = s(i) : s(i) = s(j) : s(j) = t
            Next j
        Next i
        For i = 0 To 5
            Write("s({0})={1} ", i, s(i))
        Next i
    End Sub
End Module