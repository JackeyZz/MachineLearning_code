Imports System.Console
Module Module14
    Sub saveArray(ByRef A() As Integer)
        Dim U As Integer
        Dim i As Integer
        U = UBound(A)
        If U = 0 Then
            Exit Sub
        End If
        For i = 0 To U - 1
            Randomize()
            A(i) = Int((100 * Rnd()) + 1)
        Next i
    End Sub
    Sub insertArray(ByRef A() As Integer, ByVal i As Integer, ByVal value As Integer)
        Dim U As Integer
        Dim j As Integer
        U = UBound(A)
        ReDim Preserve A(U + 1)
        For j = U To i Step -1
            A(j) = A(j - 1)
        Next j
        A(i - 1) = value
    End Sub
    Sub deleteArray(ByRef A() As Integer, ByVal i As Integer)
        Dim U As Integer
        U = UBound(A)
        Dim j As Integer
        For j = i - 1 To U - 1
            A(j) = A(j + 1)
        Next
        ReDim Preserve A(U - 1)
    End Sub
    Sub showArray(ByRef A() As Integer)
        Dim i As Integer
        Dim U As Integer
        U = UBound(A)
        Write("A({0})=[", U)
        For i = 0 To U - 2
            Write("{0},", A(i))
        Next i
        Write("{0}]", A(U - 1))
        WriteLine()

    End Sub
    Sub main()
        Dim n As Integer
        Write("n=")
        n = Val(ReadLine())
        WriteLine()
        Dim A(n) As Integer
        saveArray(A)
        showArray(A)
        insertArray(A, 3, 5)
        showArray(A)
        deleteArray(A, 5)
        showArray(A)
    End Sub
End Module
