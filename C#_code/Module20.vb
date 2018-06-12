Imports System.Console
Module Module20
    Sub main()
        Dim f(10) As Integer
        f(0) = 1 : f(1) = 1
        For i = 2 To 10
            f(i) = f(i - 2) + f(i - 1)
        Next i
        For i = 0 To 10
            If Int(i / 4) = i / 4 Then WriteLine()
            Write("f({0})={1}  ", i, f(i))
        Next i
    End Sub
End Module
