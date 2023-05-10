:: Transfer user session to a console session
for /f "skip=1 tokens=3" %%s in ('query user %USERNAME%') do (
  %windir%\System32\tscon.exe %%s /dest:console
)

:: Start AFK script 
"C:\Users\%USERNAME%\Desktop\RblxAFK.exe"