Imports System.Console
Module Module25
    Sub Main()
        Dim a(9) As Integer
        Dim x As Integer
        Dim y As Integer
        WriteLine("随机生成的数组a为：")
        For i = 0 To 9
            Randomize()
            a(i) = Int(100 * Rnd() + 1)
            Write("{0} ", a(i))
        Next i
        WriteLine()
        Write("请输入插入位置：")
        x = Val(ReadLine())
        Write("请输入插入元素值：")
        y = Val(ReadLine())
        ReDim Preserve a(9 + 1)
        For i = 10 To (x + 1) Step -1
            a(i) = a(i - 1)
        Next i
        a(x) = y
        WriteLine("插入后的新数组a：")
        For i = 0 To 10
            Write("{0} ", a(i))
        Next
    End Sub
End Module
