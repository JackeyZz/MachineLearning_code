Imports System.Math
Imports System.Console
Module Module13
    Function f(ByRef t As Double) As Double
        f = (1 + E ^ (-t)) / (1 + E ^ t)
    End Function
    Function g(ByVal x As Double, ByVal y As Double) As Double
        If x <= y Then
            g = f(x + y) / (f(x) + f(y))
        Else
            g = f(x - y) / (f(x) + f(y))
        End If
    End Function
    Sub main()
        Dim x As Double
        Dim y As Double
        Dim str As String = "0"
        Do Until str = "#"
            Write("x=")
            x = Val(ReadLine())
            Write("y=")
            y = Val(ReadLine())
            WriteLine()
            WriteLine("x={0},y={1},result={2}", x, y, g(x, y))
            str = ReadLine()
        Loop
    End Sub
End Module
