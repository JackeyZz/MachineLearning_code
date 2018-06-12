Imports System.Console
Module Module24
    Sub Main()
        Dim n As Integer
        Dim sum As Integer = 0
        Dim ave As Double
        Dim dev As Double
        Write("学生人数：")
        n = Val(ReadLine())
        Dim s(n) As Integer
        For i = 0 To n - 1
            Write("输入第{0}个学生的成绩：", i + 1)
            s(i) = Val(ReadLine())
            sum += s(i)
        Next i
        ave = sum / n
        sum = 0
        For i = 0 To n - 1
            sum += (s(i) - ave) ^ 2
        Next i
        dev = Math.Sqrt(sum / n)
        WriteLine("平均成绩为：{0}", ave)
        WriteLine("均方差成绩为：{0}", dev)
    End Sub
End Module
