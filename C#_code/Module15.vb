Imports System.Console
Module Module15
    Sub saveArray(ByRef A() As Integer, ByVal index As Integer, ByVal step1 As Integer)
        Dim U As Integer
        U = UBound(A)
        A(0) = index
        For i = 1 To U - 1
            A(i) = A(i - 1) + step1
        Next i
    End Sub
    Sub togetherArray(ByRef result() As Integer, ByRef A() As Integer, ByRef B() As Integer)
        Dim i As Integer = 0
        Dim j As Integer = 0
        Dim k As Integer = 0
        Dim UA As Integer
        Dim UB As Integer
        UA = UBound(A)
        UB = UBound(B)
        While i <= (UA - 1) And j <= (UB - 1)
            If A(i) > B(j) Then
                result(k) = B(j)
                k += 1
                j += 1
            Else
                result(k) = A(i)
                k += 1
                i += 1
            End If
        End While
        If i > (UA - 1) Then
            Dim x As Integer
            For x = j To UB - 1
                result(k) = B(x)
                k += 1
            Next
        End If
        If j > (UB - 1) Then
            Dim x As Integer
            For x = i To UA - 1
                result(k) = A(x)
                k += 1
            Next
        End If
    End Sub
    Sub showArray(ByRef A() As Integer, ByVal str As String)
        Dim i As Integer
        Dim U As Integer
        U = UBound(A)
        Write("{0}({1})=[", str, U)
        For i = 0 To U - 2
            Write("{0},", A(i))
        Next i
        Write("{0}]", A(U - 1))
        WriteLine()
    End Sub

    Sub main()
        Dim A(5) As Integer
        Dim B(6) As Integer
        Dim C(7) As Integer
        Dim temp(11) As Integer
        Dim result(18) As Integer
        saveArray(A, 1, 3)
        showArray(A, "A")
        saveArray(B, 2, 3)
        showArray(B, "B")
        saveArray(C, 3, 3)
        showArray(C, "C")
        togetherArray(temp, A, B)
        showArray(temp, "temp")
        togetherArray(result, temp, C)
        showArray(result, "result")
    End Sub
End Module
