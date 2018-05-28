Imports System.Console
Imports System.Math
Module Module17
    Sub f(ByVal a As Integer, ByVal b As Integer)
        If b = 0 Then
            WriteLine("最大公约数为：{0}", a)
        Else
            f(b, a Mod b)
        End If
    End Sub
    Sub main()
        Dim a As Integer
        Dim b As Integer
        Write("a=")
        a = Val(ReadLine())
        Write("b=")
        b = Val(ReadLine())
        f(a, b)
    End Sub
End Module
