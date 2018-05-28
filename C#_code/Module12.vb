Imports System.Math
Imports System.Console
Module Module12
    Function calc(ByVal a As Double, ByVal b As Double, ByVal c As Double) As Double
        Dim x As Double
        Dim y As Double
        Dim k As Double
        x = Max(Max(a, b), c)
        y = Max(Max(a + b, b), c)
        k = Max(Max(a, b), b + c)
        calc = x / y / k
    End Function
    Sub main()
        Dim a As Double
        Dim b As Double
        Dim c As Double
        WriteLine("请输入a：")
        a = Val(ReadLine())
        WriteLine("请输入b：")
        b = Val(ReadLine())
        WriteLine("请输入c：")
        c = Val(ReadLine())
        WriteLine("m={0}", calc(a, b, c))
    End Sub
End Module
