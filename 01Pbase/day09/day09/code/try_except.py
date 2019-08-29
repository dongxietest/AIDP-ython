def fn():
    a = input("请输入一个值:")  # aaaaa
    b = int(a) # ValueError类型的错误


    b /= 0  # ZeroDivisionError类型的错误
    #  ModuleNotFoundError 类型的错误
    # import aaaaa

try:
    fn()
except ValueError as err:
    print("出现字符串不能转为整数的错误")
finally:
    print("finally 子句里的语句被执行")

# try:
#     fn()
# except ValueError as err:
#     print("出现字符串不能转为整数的错误")
#     print("err =", err)
# except:
#     print("其它类型的错误被捕获!")
# else:
#     print("try语句内部没有发生任何异常")





# try:
#     fn()
# except (ValueError, ZeroDivisionError, ModuleNotFoundError):
#     print("程序出错")
# # except ValueError:
# #     print("程序出错")
# # except ZeroDivisionError:
# #     print("程序出错")
# # except ModuleNotFoundError:
# #     print("程序出错")



# try:
#     fn()
# except ValueError as err:
#     print("出现字符串不能转为整数的错误")
#     print("err =", err)
# except ZeroDivisionError:
#     print("fn函数内发生了除以零的错误")
# except ModuleNotFoundError:
#     print("导入模块aaaaa 失败")

print("程序正常退出")