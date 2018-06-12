Imports System.Console
Module Module26
    Sub main()
        Dim a(19) As Integer
        Dim max As Integer = 0
        Dim index As Integer = 0
        For i = 0 To 19
            Randomize()
            a(i) = Int(90 * Rnd() + 10)
            Write("{0} ", a(i))
            If a(i) > max Then
                max = a(i)
                index = i
            End If
        Next i
        WriteLine()
        WriteLine("最大值是：{0}；位置在：{1}", max, index)
    End Sub

End Module
