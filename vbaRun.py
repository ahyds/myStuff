import win32com.client

# 调用pywin32库,连接excel程序
excel = win32com.client.Dispatch("Excel.Application")

# 打开excel文件 （文件名路径包含扩展名）
wb = excel.Workbooks.Open(r"C:\Users\Administrator\Desktop\testVBA.xlsm")

# 运行vba宏 （引用宏名称，即sub后的名字）
excel.Application.Run("helloW1")
# Sub helloW1()
# MsgBox "Hello world"
# End Sub ##

# 关闭文件
wb.Close(True)

# 退出ecxcel
excel.Quit()