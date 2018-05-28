Imports System.Math
Imports System.Console
Module Module11
    Private Sub calc(ByVal m As Integer, ByVal n As Integer)
        Dim a As Integer = 1
        Dim b As Integer = 1
        Dim c As Integer = 1
        For i = 1 To m
            a = a * i
        Next i
        For j = 1 To n
            b = b * j
        Next j
        For k = 1 To (m - n)
            c = c * k
        Next k
        WriteLine("m={0},n={1},组合数为:{2}", m, n, a / b / c)
    End Sub
    Sub main()
        Dim m As Integer
        Dim n As Integer
        WriteLine("输出m：")
        m = Val(ReadLine())
        WriteLine("输出n：")
        n = Val(ReadLine())
        If m < n Then
            WriteLine("输入错误！！")
        Else
            calc(m, n)
        End If
    End Sub
End Module
